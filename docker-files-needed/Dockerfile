# Gunakan image Python versi 3.10 sebagai dasar
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt dan install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh file ke dalam container
COPY . .

# Command default saat container dijalankan
CMD ["python", "main.py"]
