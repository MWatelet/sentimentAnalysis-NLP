# Sentiment Analysis with Pre-trained AI Models

This project provides a Flask web application and supporting scripts for sentiment analysis using pre-trained AI models. It allows users to analyze the sentiment of text inputs through a user-friendly interface or a REST API, and also includes tools for benchmarking and analyzing sentiment predictions.

## Project Structure

### `main.py`
This is the main Flask application that exposes two endpoints:

1. **HTML Page Endpoint**  
   - URL: `/`  
   - A web interface where users can enter text and get sentiment analysis results.  
   - The page displays the sentiment predictions (positive or negative) from multiple pre-trained models.

2. **REST API Endpoint**  
   - URL: `/api/get_sentiment`  
   - Accepts JSON input with a `text` field.  
   - Returns a JSON response with sentiment predictions (positive or negative) from the pre-trained models.

### Supporting Scripts

1. **Benchmarking Script**  
   - **File**: `graph_benchmark.py`  
   - **Functionality**:  
     - Uses a CSV data file containing reviews and sentiment labels (positive or negative).  
     - Benchmarks the pre-trained models on the data, generating two graphs:  
       - Successes (correct predictions)  
       - Misses (incorrect predictions)  
     - Outputs the graphs for visual comparison of model performance.

2. **Data Analysis Script**  
   - **File**: `reviews_csv_extractor.py`  
   - **Functionality**:  
     - Reads a CSV file with a column of text reviews and a column of sentiment (positive or negative).  
     - Analyzes the reviews using the pre-trained models.  
     - Adds the sentiment predictions from each model as new columns in a resulting DataFrame.  
     - Outputs the updated DataFrame to a new CSV file.

## Requirements

- Python 3.11 or higher
- Docker
- Flask
- Pandas
- Matplotlib (for graph generation)
- Pre-trained sentiment analysis models (in this case so far : TextBlob, VADER, Flair, and Transformer)

## Setup and Usage

1. **Build the Docker Image**
   ```bash
   docker build -t sentiment-analysis .
