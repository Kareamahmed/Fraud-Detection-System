# Fraud Detection System 🛡️

A Machine Learning-based solution designed to detect fraudulent transactions in real-time using advanced classification techniques and a Streamlit-powered dashboard.

## 🚀 Project Overview
Fraudulent transactions cost businesses billions and erode customer trust. This project implements an automated pipeline to flag suspicious activity using historical transaction data. By addressing the severe class imbalance typical in fraud datasets, this model provides reliable predictions for security review teams.

## ✨ Key Features
* **Imbalanced Data Mastery:** Solved class imbalance using **Under-sampling** to ensure the model accurately identifies the minority (fraud) class.
* **Robust Classification:** Implemented a **Random Forest** model optimized for high-precision detection.
* **Real-Time Predictions:** Developed a **Streamlit** web interface where analysts can test new transaction samples.
* **Comprehensive Evaluation:** Validated using Confusion Matrices and F1-Scores to ensure performance beyond simple accuracy.

## 📊 Model Evaluation
The model's performance was evaluated primarily using Accuracy and a Confusion Matrix to observe the distribution of correct and incorrect predictions.

* **Overall Accuracy:** ~99.5%

### Confusion Matrix
The confusion matrix demonstrates the model's high success rate in distinguishing between legitimate and fraudulent transactions, with exceptionally low false negatives (only 8 missed fraud cases):
<img width="687" height="539" alt="image" src="https://github.com/user-attachments/assets/71dc8326-e950-49c2-ad4d-57ceb9fb5389" />

## Wep App 
 - https://fraud-detection-system-8a.streamlit.app/
