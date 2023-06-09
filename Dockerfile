# syntax=docker/dockerfile:1

FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY read-secret.py read-secret.py 
CMD [ "python3", "read-secret.py"]