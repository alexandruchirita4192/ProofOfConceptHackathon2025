FROM python:3.8-slim
WORKDIR /app
COPY python_etl/requirements.txt ./
RUN pip install -r requirements.txt
COPY python_etl/etl.py ./
ENTRYPOINT ["python", "etl.py"]
