import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

print("Sentiment Analysis Project Started")

df = pd.read_csv("reviews.csv")
print(df)

print("\nNumber of reviews: ", len(df))
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

print("\nVADER Analyzer created Successfully")

review = df["Review"][0]

score = sia.polarity_scores(review)

print("\nFirst Review: ")
print(review)

print("\nSentiment Scores: ")
print(score)

def get_sentiment(compound):
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"


sentiment = get_sentiment(score["compound"])

print("\nSentiment:")
print(sentiment)

df["Sentiment_Score"] = df["Review"].apply(
    lambda x: sia.polarity_scores(x)["compound"]
)

df["Sentiment"] = df["Sentiment_Score"].apply(get_sentiment)

print("\nAll Reviews with Sentiment:")
print(df)

sentiment_counts = df["Sentiment"].value_counts()

print("\nSentiment Counts:")
print(sentiment_counts)

plt.figure(figsize=(8, 5))

sentiment_counts.plot(kind="bar")

plt.title("Sentiment Analysis of Product Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

sentiment_percentage = (sentiment_counts / len(df)) * 100

print("\nSentiment Percentage:")
print(sentiment_percentage)

plt.figure(figsize=(7, 7))

plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sentiment Distribution")

plt.tight_layout()
plt.show()

most_positive = df.loc[df["Sentiment_Score"].idxmax()]

most_negative = df.loc[df["Sentiment_Score"].idxmin()]

print("\nMost Positive Review:")
print(most_positive["Review"])
print("Score:", most_positive["Sentiment_Score"])

print("\nMost Negative Review:")
print(most_negative["Review"])
print("Score:", most_negative["Sentiment_Score"])

plt.figure(figsize=(10, 5))

plt.bar(range(len(df)), df["Sentiment_Score"])

plt.title("Sentiment Score for Each Review")
plt.xlabel("Review Number")
plt.ylabel("Sentiment Score")

plt.axhline(0, linewidth=1)

plt.xticks(range(len(df)))

plt.tight_layout()
plt.show()

positive_count = sentiment_counts.get("Positive", 0)
negative_count = sentiment_counts.get("Negative", 0)
neutral_count = sentiment_counts.get("Neutral", 0)

print("\n===== SENTIMENT ANALYSIS SUMMARY =====")

print("Total Reviews:", len(df))
print("Positive Reviews:", positive_count)
print("Negative Reviews:", negative_count)
print("Neutral Reviews:", neutral_count)

print("======================================")

df.to_csv("sentiment_results.csv", index=False)

print("\nSentiment results saved successfully!")

emotion_keywords = {
    "Happy": ["amazing", "love", "excellent", "happy", "wonderful", "great"],
    "Angry": ["hate", "terrible"],
    "Sad": ["disappointing", "poor"],
}

def detect_emotion(review):
    review = review.lower()

    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in review:
                return emotion

    return "Neutral"

df["Emotion"] = df["Review"].apply(detect_emotion)

print("\nReviews with Emotion:")
print(df[["Review", "Sentiment", "Emotion"]])

df.to_csv("sentiment_results.csv", index=False)

print("\nSentiment and emotion results saved successfully!")

emotion_counts = df["Emotion"].value_counts()

print("\nEmotion Counts:")
print(emotion_counts)

plt.figure(figsize=(8, 5))

emotion_counts.plot(kind="bar")

plt.title("Emotion Analysis of Product Reviews")
plt.xlabel("Emotion")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

df.to_csv("sentiment_results.csv", index=False)

print("\nFinal sentiment and emotion results saved successfully!")

average_score = df["Sentiment_Score"].mean()

print("\nAverage Sentiment Score:", average_score)

if average_score > 0:
    overall_sentiment = "Positive"
elif average_score < 0:
    overall_sentiment = "Negative"
else:
    overall_sentiment = "Neutral"

print("Overall Sentiment:", overall_sentiment)

emotion_sentiment = pd.crosstab(
    df["Emotion"],
    df["Sentiment"]
)

print("\nEmotion vs Sentiment:")
print(emotion_sentiment)

emotion_sentiment.plot(kind="bar", figsize=(9, 5))

plt.title("Emotion vs Sentiment")
plt.xlabel("Emotion")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

print("\n========================================")
print("       SENTIMENT ANALYSIS PROJECT")
print("========================================")

print("Total Reviews:", len(df))
print("Positive Reviews:", positive_count)
print("Negative Reviews:", negative_count)
print("Neutral Reviews:", neutral_count)

print("\nEmotion Counts:")
print(emotion_counts)

print("\nAverage Sentiment Score:", average_score)
print("Overall Sentiment:", overall_sentiment)

print("\nAnalysis completed successfully!")
print("========================================")