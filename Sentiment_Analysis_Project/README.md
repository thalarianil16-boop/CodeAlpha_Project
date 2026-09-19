# Sentiment Analysis Project

## Overview

This project performs sentiment analysis on product reviews using Natural Language Processing (NLP) techniques.

The reviews are classified into three sentiment categories:

* Positive
* Negative
* Neutral

The project also detects specific emotions from the review text using keyword-based emotion detection.

## Technologies Used

* Python
* Pandas
* NLTK
* VADER Sentiment Analyzer
* Matplotlib

## Dataset

The project uses a small dataset of product reviews stored in:

`reviews.csv`

The dataset contains 12 product reviews.

## Analysis Performed

### 1. Sentiment Analysis

VADER Sentiment Analyzer is used to calculate sentiment scores for each review.

Each review is classified as:

* Positive
* Negative
* Neutral

### 2. Emotion Detection

A keyword-based approach is used to detect emotions such as:

* Happy
* Sad
* Angry
* Neutral

### 3. Sentiment Distribution

The project calculates the number and percentage of Positive, Negative, and Neutral reviews.

### 4. Data Visualization

The project creates visualizations including:

* Sentiment distribution bar chart
* Sentiment distribution pie chart
* Sentiment score chart
* Emotion analysis bar chart
* Emotion vs Sentiment chart

### 5. Overall Sentiment

The average sentiment score is calculated to determine the overall sentiment of the reviews.

## Results

The analysis produced the following results:

| Sentiment | Number of Reviews |
| --------- | ----------------: |
| Positive  |                 6 |
| Negative  |                 5 |
| Neutral   |                 1 |

Emotion analysis:

| Emotion | Number of Reviews |
| ------- | ----------------: |
| Happy   |                 5 |
| Neutral |                 5 |
| Sad     |                 1 |
| Angry   |                 1 |

The average sentiment score for this sample is approximately **0.1802**, resulting in an overall **Positive** sentiment classification.

## Output File

The final analysis results are saved in:

`sentiment_results.csv`

The output file contains:

* Review
* Sentiment Score
* Sentiment
* Emotion

## How to Run

1. Install Python.
2. Install the required libraries:

```bash
pip install pandas nltk matplotlib
```

3. Run:

```bash
python sentiment_analysis.py
```

4. The analysis results will be displayed in the console and saved to `sentiment_results.csv`.

## Project Purpose

This project demonstrates how NLP and sentiment analysis can be used to understand customer opinions from product reviews.

The results can help identify customer satisfaction, negative feedback, and common emotions expressed in reviews.
