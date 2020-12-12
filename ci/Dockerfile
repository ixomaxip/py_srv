# https://raw.githubusercontent.com/docker-library/python/21d2ab0a50100ebdaf32f4bbb214bf21f857d1da/3.8/buster/Dockerfile
FROM python:3.7-buster

RUN apt-get update -y
RUN apt-get install -y git wget cmake libboost-all-dev swig

RUN pip install numpy \
                nltk==3.2.5 \
                resampy \
                pandas \
                six \
                joblib \
                librosa \
                python_speech_features \
                matplotlib \
                sentencepiece \
                sacrebleu \
                h5py \
                tqdm 

RUN pip install asyncio aiofiles aiohttp
# ENV PYTHONIOENCODING=utf-8
WORKDIR /srv
EXPOSE 80
CMD python -u ./srv.py