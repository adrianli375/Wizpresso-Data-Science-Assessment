# Requirements for the PDF Table Structure Recognition API

This document outlines the details on the implementation of the PDF Table Structure Recognition API. 

## Basic Information
- The endpoint of your API should be `/process-table-structure` and the method of the API is `POST`. 
- The service should be accepting json as an input. The json format should look like ```{'image_path': PATH_TO_IMAGE}```. 
- Please expose your service to port number `8815`. 

## Libraries, Modules and Models Used
- You need to import `TableTransformerForObjectDetection` and `DetrFeatureExtractor` from the `transformers` library. Other libraries, that are not listed here, may also be necessary.
- The model to be used is a pre-trained model named `microsoft/table-transformer-structure-recognition`. 
- The feature extractor to be used is `DetrFeatureExtractor`, no resize is needed.

## API Workflow
1. Read the input json file and open the image using the image path. 
2. Get the encodings of the image and obtain a PyTorch tensor. 
3. With suitable model predictions, generate the predicted coordinates and the corresponding labels.
4. Output your results as another json.  