# Wait, Is AI Regulation Actually Moving the Market?
🚀 Exploring the intersection of AI policies and stock market trends in the tech world.

##📚 Team Members
Gavind Muhammad Pramahita
Emir Abe Putra Agastha
Muhammad Zidane Septian Irsyadi
##🛠️ Dependencies
Software
Docker
For virtual environment and container management.
Python
Main programming language for this project.
PostgreSQL
Used as the data warehouse to store processed data.
Python Libraries
Make sure the following libraries are installed in your environment:

pandas
requests
apache-airflow
psycopg2
yfinance
textblob
matplotlib
All libraries will be automatically installed when the Docker container is built (defined in requirements.txt).

💡 Project Description
Artificial Intelligence (AI) is the rockstar of tech right now, but not all the buzz is about shiny new products. Governments worldwide are starting to step in, talking about rules, ethics, and regulations. But here’s the juicy part: are these discussions actually moving the stock market? 🚨

This project explores whether news about AI regulations impacts the share prices of tech giants like Microsoft and NVIDIA. Using news sentiment analysis, stock market data, and an automated ETL pipeline, we investigated the connection between headlines and bottom lines.

🎯 Objectives
Our goal was to design an automated solution that connects news headlines with stock data to determine if AI regulations influence the market. We focused on:

Collecting News Data: Articles discussing AI regulations and ethics.
Tracking Stock Data: Historical data for major tech companies involved in AI (e.g., Microsoft, NVIDIA).
Analyzing Impact: Exploring correlations between news sentiment and stock market performance.
Ultimately, we sought to answer:

❓ Is the hype about AI regulations driving real market changes, or is it just talk?

🛠️ Technology Architecture Design
1. End-to-End Workflow
The project workflow is broken into distinct phases, each contributing to the ETL pipeline:

Extract Phase
News Data:
Retrieved via NewsAPI.
Extracted fields include: title, description, source, and publication date.
Stock Data:
Retrieved using the yfinance library.
Extracted fields include: closing price, volume, and date.
Transform Phase
News Data:
Performed sentiment analysis using TextBlob.
Aggregated daily sentiment scores and article counts.
Stock Data:
Filtered relevant columns (e.g., closing price, volume) and ensured date alignment.
Output:
Two datasets: news_summary and transformed_stock.
Load Phase
Processed data is stored in a PostgreSQL database with two tables:
news: For aggregated news data (e.g., sentiment scores, article count).
stock: For stock market data (e.g., closing prices, trading volume).
Analysis Phase
Correlation analysis between sentiment and stock price.
Time-series visualization of trends in sentiment and stock performance.
🗄️ Database Structure
PostgreSQL Database:
The data is stored in two tables:

news

Column	Data Type	Description
id	SERIAL	Primary key
date	TIMESTAMP	Date of the news headline
avg_sentiment	FLOAT	Average sentiment score of articles
news_count	INTEGER	Number of articles on the date
stock

Column	Data Type	Description
id	SERIAL	Primary key
date	TIMESTAMP	Date of stock data
close_price	FLOAT	Closing stock price
volume	INTEGER	Trading volume
🚀 How to Run the Project
1. Build the Docker Image
bash
Copy code
docker build -t etl-project .
2. Run the Docker Container
bash
Copy code
docker run --rm -v $(pwd):/app etl-project
3. Verify the Output
The processed data will be saved in a CSV file (output_data.csv) or loaded into the PostgreSQL database.
🌐 Architecture Overview
Components
Data Sources:
NewsAPI: Provides news data related to "AI regulations."
Yahoo Finance: Provides stock data for relevant companies (e.g., Microsoft, NVIDIA).
ETL Pipeline:
Extract: Collects raw data from APIs.
Transform: Cleans, enriches, and aligns data for analysis.
Load: Stores processed data in a PostgreSQL database.
Analysis and Visualization:
Correlation analysis between sentiment and stock prices.
Generated visualizations of trends and patterns.
📊 Analysis Process
Step 1: Load and Inspect Data
Data is loaded into pandas DataFrames.
Data types and missing values are inspected to ensure completeness.
Step 2: Data Cleaning
Removes duplicates and fills missing values.
Ensures proper date formatting for merging datasets.
Step 3: Merge Datasets
News and stock data are merged on the date column.
Step 4: Feature Engineering
Added new features like:
Price change (price_change).
Rolling averages for sentiment and stock prices.
Lagged features to capture historical trends.
Step 5: Predictive Modeling
Trained a linear regression model to predict stock prices using:
Sentiment scores.
Historical stock performance data.
🛠️ Results and Insights
Key Findings
Model Performance:
Regression model achieved a low Mean Squared Error (MSE) (~0.0155).
Correlation Analysis:
Strong positive correlation between news sentiment and stock prices.
Increased news volume coincided with higher trading activity.
Visualizations
Line charts showing sentiment vs. stock prices over time.
Scatterplots visualizing the correlation between sentiment and stock performance.
🎥 Links
Presentation Video: (Add link here)
Colab Notebook: (Add link here)
Notion Documentation: (Add link here)
🛠️ Monitoring and Debugging
Airflow Monitoring
Monitor DAG execution and logs using the Airflow UI.
Error Handling
Automatically retries failed tasks.
Alerts the user if errors persist.
