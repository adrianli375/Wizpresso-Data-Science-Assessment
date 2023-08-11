import pandas as pd
import numpy as np
from transformers import TableTransformerForObjectDetection, DetrFeatureExtractor
import torch
import sys
import json
import base64
import io
import os
import gc
from PIL import Image
from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)
# Set the maximum GPU memory fraction to 0.05
gpu_memory_limit_ratio = 0.05
# Set the environment variable to limit the visible GPUs
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
print('Limiting GPU memory ratio to ', gpu_memory_limit_ratio)
torch.cuda.set_per_process_memory_fraction(gpu_memory_limit_ratio)
print('Loading Table Structure Recognition Model...', datetime.now())
model = TableTransformerForObjectDetection.from_pretrained("microsoft/table-transformer-structure-recognition")
device = torch.device('cuda')
model.to(device)
feature_extractor = DetrFeatureExtractor(do_resize=False)
print('Finished loading Table Structure Recognition Model...', datetime.now())


from PDFPixelCoordinateConverter import convert_pdf_coordinates_to_pixel, convert_pixel_to_pdf_coordinates


LABELS_MAPPING = {
    0: 'table',
    1: 'table column',
    2: 'table row',
    3: 'table column header',
    4: 'table projected row header',
    5: 'table spanning cell'
}

@app.route('/')
def welcome():
    return 'Welcome to PDF Table Structure Recognition API'


@app.route('/process_table_structure', methods=['POST'])
def process_table_structure():
    data = request.json
    data = json.loads(data.replace("'", "\""))
    archivefilename = data.get('archivefilename')
    page = data.get('page')
    coordinates = tuple(data.get('coordinates'))
    origin = tuple(data.get('origin'))
    file_jpg_byte = data.get('file_jpg_bytes')
    print('Processing Table...', archivefilename, page, datetime.now())
    # coordinates = [float(x) for x in coordinates]
    rotate = data.get('rotate')
    image_path = None if data.get('image_path') is None else data.get('image_path')
    border_size = 30 if data.get('border_size') is None else data.get('border_size')

    if image_path:
        image = ""
    else:
        image = Image.open(io.BytesIO(base64.b64decode(file_jpg_byte)))
    # Create the new image with the desired size
    pixels = convert_pdf_coordinates_to_pixel(image, coordinates[0], coordinates[1], coordinates[2], coordinates[3],
                                              origin[0], origin[1])
    table_image = image.crop((pixels[0] - border_size, pixels[2] - border_size, pixels[1] + border_size, pixels[3] + border_size))
    # Model Predictions
    print('Start Building Encodings...', datetime.now())
    encoding = feature_extractor(table_image, return_tensors="pt")
    print('Finished Building Encodings...', datetime.now())
    encoding.to(device)
    with torch.no_grad():
        outputs = model(**encoding)
    results_tensor_dict = feature_extractor.post_process_object_detection(outputs, threshold=0.7, target_sizes=[table_image.size[::-1]])[0]
    # Result Post Processing
    results_array_dict = {k: v.cpu().numpy() for k, v in results_tensor_dict.items()}
    coordinates_list = [np.ravel(x) for x in np.split(results_array_dict['boxes'], results_array_dict['boxes'].shape[1], axis=1)]
    results_df = pd.DataFrame.from_dict({'scores': results_array_dict['scores'], 'labels': results_array_dict['labels']})
    results_df[['pixel_start_x', 'pixel_start_y', 'pixel_end_x', 'pixel_end_y']] = pd.DataFrame(np.array(coordinates_list).T)
    results_df['mapped_labels'] = results_df['labels'].map(LABELS_MAPPING)
    pdf_coordinates = results_df.apply(lambda x: convert_pixel_to_pdf_coordinates(
        table_image, x['pixel_start_x'], x['pixel_end_x'], x['pixel_start_y'], x['pixel_end_y'],
        (coordinates[0], coordinates[2]), border_size), axis=1)
    print('Finished processing Table...', archivefilename, page, datetime.now())
    # Free up Memory
    del encoding
    del outputs
    del results_tensor_dict
    del image
    del pixels
    del table_image
    del file_jpg_byte
    torch.cuda.empty_cache()
    gc.collect()
    if len(pdf_coordinates) > 0:
        results_df[['start_x', 'end_x', 'start_y', 'end_y']] = pd.DataFrame(list(map(tuple, zip(*pdf_coordinates)))).T
        return results_df.to_dict()
    else:
        return pd.DataFrame().to_dict()


if __name__ == '__main__':
    # recognition_model = TableTransformerForObjectDetection.from_pretrained("microsoft/table-transformer-structure-recognition")
    app.run(host='0.0.0.0', debug=False, port=8815)
    print('')
