# Use the official Airflow image as a base
FROM apache/airflow:2.5.1

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
