FROM python:3.10-slim-bullseye as base

WORKDIR /app
COPY . /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
CMD ["python3", "telpot.py"]