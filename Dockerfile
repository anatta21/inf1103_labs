FROM python:3.14
WORKDIR /app 
COPY persistence_auditor.py .
CMD ["python", "persistence_auditor.py"]