# Fraud Detection System 🛡️

A Machine Learning-based solution designed to detect fraudulent transactions in real-time using advanced classification techniques and a Streamlit-powered dashboard.

## 🚀 Project Overview
Fraudulent transactions cost businesses billions and erode customer trust. This project implements an automated pipeline to flag suspicious activity using historical transaction data. By focusing on data authenticity and balanced distribution, the system provides high-reliability predictions for security teams.

## ✨ Key Technical Highlights
* **Strategic Under-sampling:** To resolve severe class imbalance, I specifically utilized **Under-sampling**. This ensures the model learns from **authentic, real-world patterns** only, avoiding the "fake" or synthetic noise often introduced by over-sampling methods (like SMOTE).
* **Robust Classification:** Implemented a **Random Forest** model, chosen for its ensemble learning capabilities and high precision in identifying rare-event fraud patterns.
* **Real-Time Inference:** Integrated a **Streamlit** frontend, allowing analysts to input transaction details and receive instant fraud-risk predictions.

## 📊 Model Evaluation
The model's performance was evaluated using overall Accuracy and a Confusion Matrix to ensure the minority (fraud) class was captured effectively.

* **Overall Accuracy:** ~99.5%

### Confusion Matrix
The matrix demonstrates the model's success in distinguishing between legitimate and fraudulent transactions, with only **8 missed fraud cases** (False Negatives) out of the entire test set.

<img width="687" height="539" alt="Confusion Matrix" src="https://github.com/user-attachments/assets/71dc8326-e950-49c2-ad4d-57ceb9fb5389" />

## 🌐 Live Demo
**[Fraud Detection Web App](https://fraud-detection-system-8a.streamlit.app/)**

