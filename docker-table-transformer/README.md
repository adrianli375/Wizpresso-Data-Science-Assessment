# Data Science Assessment - Table Structure Recognition

At Wizpresso, one of the most important values is to transform unstructured data into useful insights. Particularly, PDF documents from annual reports often have tabular data present. Our team transforms these data into machine-readable format through the use of machine learning algorithms and/or models. 

As part of the assessment, you will act as a role of a Data Scientist at Wizpresso, facilitating the deployment of this product into our workflow. 

## Directory Structure
The directory structure for this task is
```
|- src
    |- api
        |- img
            |- TestCase1_Tencent.jpg
            |- TestCase2_Tesla.jpg
            |- TestCase3_NVIDIA.jpg
            ...
            |- (more photos hidden)
        |- PDFTableStructureRecognition.py
        |- PDFTableStructureRecognitionAPI.py (to be implemented)
```

where you are provided with several images and a Python script for testing purposes. 

## Requirements

### 1. Building an API for PDF Table Structure Recognition

You are required to create the file `PDFTableStructureRecognitionAPI.py` for the API service. 

You are allowed to use any API frameworks, but Flask and/or FastAPI is preferred. 

For more details on building the API, visit [api_requirements.md](src/api/api_requirements.md) which is located in the same directory. 

### 2. Building a `Dockerfile` for the API service

The next task is to build a `Dockerfile` in the `api` directory to deploy the application inside a Docker container. 

If you are new to Docker, you may download the Docker application in the [official website of Docker](https://www.docker.com/products/docker-desktop/) and read the instructions and tutorials. 

After you have built the `Dockerfile`, please push your latest changes to your personal GitHub repo and share the repo with us. 

## Bonus
To test if the API works, you can try to run `PDFTableStructureRecognition.py` inside the Docker container. If the API works, you will see that all test cases will pass.

Successful sample: 
```
# python PDFTableStructureRecognition.py
..............................
----------------------------------------------------------------------
Ran 30 tests in 25.080s

OK
```
