FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

COPY . . 

EXPOSE 8000
