FROM python:3

WORKDIR /usr/app

COPY testing_api_dog.py ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["pytest", "-v", "testing_api_dog.py"]