# assume the version of the env is Python 3.8
FROM python:3.8

# install wget, git 
RUN apt-get update && apt-get install -y wget && apt-get install -y git

# Set environment variables for Miniconda installation
ENV CONDA_HOME /opt/miniconda
ENV PATH ${CONDA_HOME}/bin:$PATH

# install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh

# Install Miniconda using the installer script
RUN bash /tmp/miniconda.sh -b -p ${CONDA_HOME} && \
    rm /tmp/miniconda.sh

# optional: use the new conda solver for a more efficient performance
# (credits to Stefan)
RUN conda install -n base conda-libmamba-solver
RUN conda config --set solver libmamba

# set working directory and get cloned files
WORKDIR /app
# ideally, the code file should be contained in a directory called "src"
COPY ./src /app

# run conda to create env and install libraries
# optional for candidates: specify the correct library version
RUN conda create --name pdf_table_recognition_api python=3.8
RUN conda install pandas numpy -y
RUN pip install torch torchvision torchaudio
RUN pip install Pillow Flask
RUN conda init bash

# optional for candidates: set proper timezone
ENV TZ=Asia/Hong_Kong

# expose the application to the appropriate port number
EXPOSE 8815

# run the API app
CMD ["conda", "run", "--no-capture-output", "-n", "pdf_table_recognition_api", \
     "python", "PDFTableStructureRecognitionAPI.py"]
