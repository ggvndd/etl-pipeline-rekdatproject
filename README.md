#Project ETL Pipeline Data Engineering 
Proyek ini bertujuan untuk mencari korelasi antara trending topics di X atau Twitter dengan trending topic yang ada di Google. Proyek ini menggunakan Docker sebagai virtual environment untuk memastikan adanya kesamaan dalam lingkungan pengerjaan pipeline. 
##Team Members
Gavind Muhammad Pramahita
Emir Abe Putra Agastha
Muhammad Zidane Septian Irsyadi
##Dependencies Needed
[Docker](https://docs.docker.com/engine/install/) 
[Python](https://www.python.org/downloads/)
Python Libraries: pandas, requests, apache-airflow, psycopg2, pytrends, tweepy
[Postgresql](https://www.postgresql.org/download/)
##Database Establishment
CREATE DATABASE etl_db;
CREATE TABLE trending_topics (
    id SERIAL PRIMARY KEY,
    platform VARCHAR(50),
    topic VARCHAR(255),
    source VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);




