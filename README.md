🚀 Wait, Is AI Regulation Actually Moving the Market?
Exploring the intersection of AI policies and stock market trends in the tech world.

📜 Description
Artificial Intelligence (AI) is the rockstar of tech right now, but not all the buzz is about shiny new products. Governments worldwide are stepping in with discussions around rules, ethics, and regulations. The big question is: are these discussions moving the stock market? 🚨

In this project, we analyze whether news about AI regulations affects the stock prices of tech giants like Microsoft and NVIDIA. By combining news sentiment analysis, stock market data, and a fully automated ETL pipeline, we explore whether policy headlines create real market movement. Let’s uncover whether the hype about AI regulations drives real market changes or is just noise! 💥

🎯 Objectives
This project aims to explore the connection between news headlines and stock market trends by:

Collecting news articles related to AI regulations and ethics.
Tracking stock data for major tech companies driving AI innovation (e.g., Microsoft, NVIDIA).
Analyzing the correlation between sentiment in the news and stock price movement.
Automating the entire pipeline from data extraction to visualization using Docker and Apache Airflow.
🛠️ Technology Stack
Components and Tools
Component	Technology	Purpose
Data Sources	NewsAPI, Yahoo Finance (yfinance)	Fetch news and stock market data.
ETL Orchestration	Apache Airflow	Automates and schedules the ETL pipeline.
Data Transformation	Python (pandas, textblob)	Handles data cleaning, aggregation, and sentiment analysis.
Data Storage	PostgreSQL	Centralized database for structured data storage and querying.
Containerization	Docker	Ensures consistent environment setup across systems.
Visualization	Python (matplotlib, seaborn)	Creates visualizations for data analysis and insights.
🗄️ Database Schema
We use PostgreSQL as the data warehouse. Here’s the schema:

sql
Copy code
CREATE TABLE news (
    id SERIAL PRIMARY KEY,
    date DATE,
    title TEXT,
    description TEXT,
    sentiment_score FLOAT,
    source VARCHAR(255)
);

CREATE TABLE stock (
    id SERIAL PRIMARY KEY,
    date DATE,
    close_price FLOAT,
    volume BIGINT
);
🌐 End-to-End ETL Pipeline
Workflow Breakdown
Extract Phase (Data Ingestion)

News Data: Collected from NewsAPI using relevant keywords (e.g., "AI regulations").
Stock Data: Historical stock data fetched from Yahoo Finance for key companies (e.g., Microsoft, NVIDIA).
Transform Phase (Data Processing)

News Data:
Sentiment analysis is applied using TextBlob.
Data is aggregated by date to calculate average sentiment and news count.
Stock Data:
Data is cleaned, aligned, and transformed for date-based analysis.
Load Phase (Data Storage)

Processed datasets are loaded into PostgreSQL tables for centralized storage and querying.
Analysis Phase

Sentiment scores and stock performance are merged for correlation analysis.
Time series analysis is performed to explore trends over time.
Visualization Phase

Insights are presented through scatterplots, trend lines, and correlation charts.
📊 Insights from Predictive Modeling
Sentiment and Stock Performance

Sentiment analysis provided meaningful predictors for stock movement.
Lagged features and moving averages improved model accuracy.
Model Results

Mean Squared Error (MSE): 0.0155
Predictions closely align with actual stock prices, demonstrating the model's reliability.
Key Correlations

Positive sentiment correlates with increased stock prices.
News frequency impacts trading volume.
⚙️ How to Run the Project
1. Set Up Docker
Ensure Docker is installed on your system. Build the Docker image:

bash
Copy code
docker build -t etl-ai-market .
Run the container:

bash
Copy code
docker run --rm -v $(pwd):/app etl-ai-market
2. Verify Output
PostgreSQL Database:
Check the tables (news and stock) to ensure data is correctly loaded.

CSV Export:
Transformed data will also be saved in output_data.csv for verification.

📚 Resources
Presentation Video: [Add Link Here]
Notion Documentation: [Add Link Here]
Colab Notebook: [Add Link Here]
🚀 Future Enhancements
Expand Scope
Analyze additional companies (e.g., Google, Amazon) for broader insights.
Advanced Modeling
Incorporate machine learning models like Random Forest or XGBoost for improved prediction accuracy.
Dashboard Integration
Build an interactive dashboard using tools like Streamlit or Tableau for real-time insights.
📬 Contact
For questions or contributions, reach out to the team:

Gavind Muhammad Pramahita
Emir Abe Putra Agastha
Muhammad Zidane Septian Irsyadi
