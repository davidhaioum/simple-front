FROM python:3.10-alpine

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0" ]