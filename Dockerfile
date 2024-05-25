FROM python:3.10-alpine

WORKDIR /app
RUN python3 -m pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
ENTRYPOINT [ "python3", "run.py" ] 