#Using streamlit
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

data = pd.read_csv(r"C:\Users\HP\Desktop\task 4 ML Model\mail_data.csv")

data.columns = data.columns.str.strip().str.lower()

data.drop_duplicates(inplace=True)

data['category'] = data['category'].str.lower().replace({'ham': 'not spam', 'spam': 'spam'})

data['message'] = data['message'].fillna('')

messages = data['message']
categories = data['category']

X_train, X_test, y_train, y_test = train_test_split(messages, categories, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(lowercase=True, stop_words='english', ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(X_train)

model = MultinomialNB(alpha=0.1)
model.fit(X_train_tfidf, y_train)


def predict(message):
    message_tfidf = vectorizer.transform([message])
    return model.predict(message_tfidf)[0]

st.title("📩 Spam Detection App")
input_message = st.text_input("🔍 Enter your message:")
if st.button("🚀 Validate"):
    result = predict(input_message)
    st.write(f'✅ **The message is:** {result}')


#terminal: streamlit run task4.py (command)

