FROM python:3.8-slim
WORKDIR /app
COPY flask_app/requirements.txt ./
RUN pip install -r requirements.txt
COPY flask_app/ .
ENTRYPOINT ["python", "app.py"]
