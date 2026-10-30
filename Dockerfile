FROM python:3.14-slim
WORKDIR /app
COPY main_oop.py .
CMD ["python", "main_oop.py"]
