FROM python:3
ENV PYTHONUNBUFFED 1
RUN mkdir /my_diary
WORKDIR /my_diary
ADD requirements.txt /my_diary/
RUN pip install -r requirements.txt 
ADD . /my_diary/