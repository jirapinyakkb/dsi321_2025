FROM python:3.10-slim

# ติดตั้ง pip และ dependencies
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Prefect needs to be configured later
CMD ["prefect", "orion", "start"]
