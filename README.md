# ETL Pipeline Data Engineering Project

Proyek ini bertujuan untuk menganalisis korelasi antara **trending topics di platform X (Twitter)** dengan **trending topics di Google**. Pipeline ini dirancang menggunakan **Docker** untuk memastikan konsistensi lingkungan kerja pada setiap pengembang.

---

## 📚 Team Members
- **Gavind Muhammad Pramahita**
- **Emir Abe Putra Agastha**
- **Muhammad Zidane Septian Irsyadi**

---

## 🛠️ Dependencies
Pastikan semua dependency berikut telah diinstal:

### Software
- [Docker](https://docs.docker.com/engine/install/)  
  Untuk virtual environment dan manajemen container.
- [Python](https://www.python.org/downloads/)  
  Bahasa pemrograman utama proyek ini.
- [PostgreSQL](https://www.postgresql.org/download/)  
  Database yang digunakan sebagai data warehouse.

### Python Libraries
Tambahkan library berikut ke dalam environment:
- `pandas`
- `requests`
- `apache-airflow`
- `psycopg2`
- `pytrends`
- `tweepy`

Semua library ini secara otomatis akan diinstal saat Docker container dibuat (terdefinisi di `requirements.txt`).

---

## 🗄️ Database Establishment
Gunakan PostgreSQL untuk membuat database dan tabel dengan langkah berikut:

1. Buat database:
   CREATE DATABASE etl_db;
2. Buat tabel:
CREATE TABLE trending_topics (
    id SERIAL PRIMARY KEY,
    platform VARCHAR(50),
    topic VARCHAR(255),
    source VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

---

## 🚀 How to Run the Project
Build Docker Image
Jalankan perintah berikut untuk membangun Docker image:

docker build -t etl-project .
Run Docker Container
Jalankan proyek di dalam container:

docker run --rm -v $(pwd):/app etl-project

###Verify Output

Hasil proses ETL akan disimpan di file CSV (output_data.csv) atau dimuat langsung ke PostgreSQL.

---

## 💡 Purpose
Pipeline ini dirancang untuk:

Mengambil data trending topics dari Twitter menggunakan API.
Mengambil data trending topics dari Google Trends.
Membersihkan, menggabungkan, dan menganalisis data untuk menemukan keselarasan atau korelasi.
Menyimpan hasil analisis ke dalam PostgreSQL sebagai data warehouse.
