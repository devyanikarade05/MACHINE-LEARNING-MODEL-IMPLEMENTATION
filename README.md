# MACHINE-LEARNING-MODEL-IMPLEMENTATION

- **Company:** CODTECH IT SOLUTIONS  
- **Name:** Devyani Karade  
- **Intern ID:** CT08LTW  
- **Domain:** Machine Learning (Python)  
- **Batch Duration:** February 5th, 2025 - March 5th, 2025  
- **Mentor:** Neela Santhosh  

This repository contains a **Spam Detection Chatbot** built using **Python**, **Machine Learning (Naive Bayes)**, and **Streamlit**. The chatbot is trained on a dataset of emails/messages and predicts whether a given message is spam or not.

## Features

✅ Detects whether a message is **Spam** or **Not Spam**  
✅ Uses **TF-IDF Vectorization** to preprocess text data  
✅ Implements **Multinomial Naive Bayes (NB)** for classification  
✅ Supports both **terminal-based** and **web-based (Streamlit)** interaction  
✅ Simple and easy-to-use interface  

## 1. Terminal-Based Spam Detection

The model runs in the terminal and supports:

- Detecting spam messages based on trained data
- Taking user input and classifying it as spam or not spam
- Providing real-time predictions

## 2. Streamlit-Based Spam Detection App

The chatbot can also run on a **Streamlit Web Interface**, allowing users to enter text messages and receive classification results instantly.

### Running the Streamlit App

```sh
streamlit run task4.py
```

## Technologies Used

- **Python** - Core programming language  
- **Pandas** - Data preprocessing  
- **Scikit-learn** - Machine learning model (Naive Bayes)  
- **NLTK** - Natural language processing  
- **TF-IDF Vectorization** - Feature extraction from text data  
- **Streamlit** - Web-based UI for spam detection  

## Usage

### 1. Terminal-Based Spam Detection:
   - Run `jupyterNotebook_task_4.py` in the terminal.
   - Enter a message to check if it is spam or not.
   - The model will return **"Spam"** or **"Not Spam"** as output.

### 2. Streamlit-Based Spam Detection:
   - Run `task4.py` using `streamlit run task4.py`.
   - Enter a message in the input field.
   - Click **"Validate"** to check if the message is spam or not.
   - The result will be displayed instantly.

## Example Interactions

### **Terminal-Based Prediction:**
```
📩 Spam Detection!!!
🔍 Enter your message: Win a free iPhone now!!!
✅ The message is: Spam
```

### **Streamlit-Based Prediction:**
- **User enters:** "Congratulations! You have won a lottery! Click here."
- **ChatBot Response:** ✅ The message is: **Spam**


## OUTPUT of Spam Detector:

![Image](https://github.com/user-attachments/assets/032abe8d-a4b1-4d3f-9a92-ad8f8b7a136f)
