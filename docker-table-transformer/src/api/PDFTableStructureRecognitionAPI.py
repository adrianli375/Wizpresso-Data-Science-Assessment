import pandas as pd
import numpy as np
from transformers import TableTransformerForObjectDetection, DetrFeatureExtractor
import torch
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
try:
    torch.cuda.set_per_process_memory_fraction(gpu_memory_limit_ratio)
except (AssertionError, RuntimeError) as _:
    pass
print(datetime.now(), 'Loading Table Structure Recognition Model...')
model = TableTransformerForObjectDetection.from_pretrained("microsoft/table-transformer-structure-recognition")
try:
    device = torch.device('cuda')
    model.to(device)
except (AssertionError, RuntimeError) as _:
    pass
feature_extractor = DetrFeatureExtractor(do_resize=False)
print(datetime.now(), 'Finished loading Table Structure Recognition Model...')


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


@app.route('/process-table-structure', methods=['POST'])
def process_table_structure():
    try:
        data = request.json
        image_path = data.get('image_path')
        table_image = Image.open(image_path)

        # Model Predictions
        print(datetime.now(), 'Start Building Encodings...')
        encoding = feature_extractor(table_image, return_tensors="pt")
        print(datetime.now(), 'Finished Building Encodings...')
        try:
            encoding.to(device)
        except (AssertionError, RuntimeError) as _:
            pass
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
            border_size=30), axis=1)
        print('Finished processing Table...')
        # Free up Memory
        del encoding
        del outputs
        del results_tensor_dict
        del table_image
        torch.cuda.empty_cache()
        gc.collect()
        if len(pdf_coordinates) > 0:
            results_df[['start_x', 'end_x', 'start_y', 'end_y']] = pd.DataFrame(list(map(tuple, zip(*pdf_coordinates)))).T
            return results_df.to_dict()
        else:
            return pd.DataFrame().to_dict()
    except Exception as e:
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8815)
