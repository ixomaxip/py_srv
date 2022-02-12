FROM python:3.8-buster

RUN apt-get update -y
RUN apt-get install -y git wget cmake libboost-all-dev swig

RUN pip install \
    aiohttp==3.8.1 \
    aiofiles==0.8.0 \
    python-json-logger==2.0.1 \
    PyYAML==5.4.1 \
    omegaconf==2.1.1

# RUN pip install numpy \
#                 nltk==3.2.5 \
#                 resampy \
#                 pandas \
#                 six \
#                 joblib \
#                 librosa \
#                 python_speech_features \
#                 matplotlib \
#                 sentencepiece \
#                 sacrebleu \
#                 h5py \
#                 tqdm 

# ENV PYTHONIOENCODING=utf-8
WORKDIR /srv
EXPOSE 80
CMD python -u ./srv.py