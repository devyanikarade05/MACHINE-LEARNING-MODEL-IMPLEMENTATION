import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("mail_data.csv")

data.columns = data.columns.str.strip().str.lower()

data.drop_duplicates(inplace=True)
data['category'] = data['category'].str.lower().replace({'ham': 'not spam', 'spam': 'spam'})
data['message'] = data['message'].fillna('')

X = data['message']
y = data['category']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB(alpha=0.1)
model.fit(X_train_tfidf, y_train)


def predict_spam(message):
    message_tfidf = vectorizer.transform([message])
    return model.predict(message_tfidf)[0]

print("📩 Spam Detection!!!")
input_message = input("🔍 Enter your message: ")
result = predict_spam(input_message)

print(f"✅ The message is: {result}")
