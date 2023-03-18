FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt .
COPY create_s3.py .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "create_s3:app", "--host", "0.0.0.0", "--port", "80"]