# 📈 Is AI Regulation Actually Moving the Market?

Exploring the intersection of AI policies and stock market trends in the tech world.

---

## 📚 Team Members
- **Gavind Muhammad Pramahita**
- **Emir Abe Putra Agastha**
- **Muhammad Zidane Septian Irsyadi**

---

## 🛠️ Dependencies

### **Software**
- **Docker**: For virtual environment and container management.
- **Python**: Main programming language for this project.
- **PostgreSQL**: Used as the data warehouse to store processed data.

### **Python Libraries**
The following libraries are required for this project:
- `pandas`
- `requests`
- `apache-airflow`
- `psycopg2`
- `yfinance`
- `textblob`
- `matplotlib`

> Note: All required libraries will be automatically installed when building the Docker container (defined in `requirements.txt`).

---

## 💡 Project Description

Artificial Intelligence (AI) is the rockstar of the tech world, but not all the buzz is about shiny new products. Governments worldwide are stepping in, talking about rules, ethics, and regulations.

### The Big Question:
**Are these discussions actually moving the stock market?** 🚨

This project explores whether news about AI regulations impacts the share prices of tech giants like Microsoft and NVIDIA. By leveraging news sentiment analysis, stock market data, and an automated ETL pipeline, we investigated the connection between headlines and bottom lines.

---

## 🎯 Objectives

Our goal was to design an automated solution that connects news headlines with stock data to determine whether AI regulations influence the market. We focused on:
1. **Collecting News Data**: Articles discussing AI regulations and ethics.
2. **Tracking Stock Data**: Historical data for major tech companies involved in AI (e.g., Microsoft, NVIDIA).
3. **Analyzing Impact**: Exploring correlations between news sentiment and stock market performance.

### Key Question:
**Is the hype about AI regulations driving real market changes, or is it just talk?**

---

## 🛠️ Technology Architecture Design

### 1️⃣ End-to-End Workflow

The project is organized into several phases that together build the ETL pipeline:

#### **Extract Phase**
- **News Data**:  
  Retrieved via NewsAPI.  
  Extracted fields: `title`, `description`, `source`, `publication date`.
- **Stock Data**:  
  Retrieved using the `yfinance` library.  
  Extracted fields: `closing price`, `volume`, `date`.

#### **Transform Phase**
- **News Data**:  
  Sentiment analysis was performed using `TextBlob`.  
  Daily sentiment scores and article counts were aggregated.
- **Stock Data**:  
  Filtered for relevant columns (e.g., closing price, volume) and aligned with date.
- **Output**:  
  Two processed datasets: `news_summary` and `transformed_stock`.

#### **Load Phase**
Data is stored in a PostgreSQL database with two tables:
1. **`news`**: For aggregated news data (e.g., sentiment scores, article count).
2. **`stock`**: For stock market data (e.g., closing prices, trading volume).

#### **Analysis Phase**
- Performed correlation analysis between sentiment and stock price.
- Visualized trends in sentiment and stock performance using time-series charts.

---

## 🗄️ Database Structure

### PostgreSQL Database

#### 1. **`news` Table**
| Column         | Data Type  | Description                              |
|----------------|------------|------------------------------------------|
| `id`           | SERIAL     | Primary key                              |
| `date`         | TIMESTAMP  | Date of the news headline                |
| `avg_sentiment`| FLOAT      | Average sentiment score of articles      |
| `news_count`   | INTEGER    | Number of articles on the date           |

#### 2. **`stock` Table**
| Column         | Data Type  | Description                              |
|----------------|------------|------------------------------------------|
| `id`           | SERIAL     | Primary key                              |
| `date`         | TIMESTAMP  | Date of stock data                       |
| `close_price`  | FLOAT      | Closing stock price                      |
| `volume`       | INTEGER    | Trading volume                           |

---


## 🌐 Architecture Overview

### **Components**
1. **Data Sources**:
   - **NewsAPI**: Provides news data related to "AI regulations."
   - **Yahoo Finance**: Provides stock data for relevant companies (e.g., Microsoft, NVIDIA).

2. **ETL Pipeline**:
   - **Extract**: Collects raw data from APIs.
   - **Transform**: Cleans, enriches, and aligns data for analysis.
   - **Load**: Stores processed data in a PostgreSQL database.

3. **Analysis and Visualization**:
   - **Correlation Analysis**: Between sentiment and stock prices.
   - **Visualizations**: Trends and patterns are explored through charts and graphs.

---

## 📊 Analysis Process

### **Step 1: Load and Inspect Data**
- Data is loaded into `pandas` DataFrames.
- Inspected for missing values and data types.

### **Step 2: Data Cleaning**
- Removed duplicates and filled missing values.
- Formatted dates for merging datasets.

### **Step 3: Merge Datasets**
- News and stock data were merged on the `date` column.

### **Step 4: Feature Engineering**
New features were added, including:
- **Price Change (`price_change`)**: Difference in stock prices between days.
- **Rolling Averages**: For sentiment and stock prices.
- **Lagged Features**: Historical trends for better predictive analysis.

### **Step 5: Predictive Modeling**
A **linear regression model** was trained to predict stock prices using:
- Sentiment scores.
- Historical stock performance data.

---

## 🛠️ Results and Insights

### **Key Findings**
1. **Model Performance**:
   - The regression model achieved a low **Mean Squared Error (MSE)** (~0.0155).
2. **Correlation Analysis**:
   - Strong positive correlation between news sentiment and stock prices.
   - Increased news volume coincided with higher trading activity.

### **Visualizations**
- **Line Charts**: Showing sentiment vs. stock prices over time.
- **Scatterplots**: Visualizing the correlation between sentiment and stock performance.

---

## 🎥 Links
- **[Presentation Video](#)**  
- **[Colab Notebook](#https://colab.research.google.com/drive/1HosNsGa7rWSpeI4nCgMkadAOLlCKzzRi?usp=sharing)**  
- **[Notion Documentation](#https://www.notion.so/mzidane/Wait-Is-AI-Regulation-Actually-Moving-the-Market-1430bc51572380f3b896f552975b163c#1430bc5157238001bc7ae3d4582ccbf3)**  

---

## 🛠️ Monitoring and Debugging

### **Airflow Monitoring**
- Monitor DAG execution and logs using the **Airflow UI**.

### **Error Handling**
- Automatically retries failed tasks.
- Alerts the user if errors persist.

---
