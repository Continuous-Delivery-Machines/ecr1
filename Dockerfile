FROM python:3.6

RUN pip install boto3

COPY h5.py /app/my.py

CMD sleep 20