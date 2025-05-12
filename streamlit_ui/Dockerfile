FROM python:3.8-slim
WORKDIR /app
COPY streamlit_ui/requirements.txt ./
RUN pip install -r requirements.txt
COPY streamlit_ui/ .
ENTRYPOINT ["streamlit", "run", "dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
