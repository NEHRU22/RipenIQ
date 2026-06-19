# 🍌 RipenIQ – Banana Ripeness & Shelf-Life Estimator

## Overview

RipenIQ is an AI-powered web application that analyzes banana images and predicts their ripeness stage using Deep Learning. The system helps users identify whether a banana is Unripe, Ripe, Overripe, or Rotten and provides shelf-life recommendations.

The application consists of:

* Deep Learning model built with TensorFlow/Keras
* FastAPI backend for prediction APIs
* HTML, CSS, and JavaScript frontend
* Render cloud deployment

---

## Features

* Upload a banana image
* Predict banana ripeness stage
* Display prediction confidence
* Estimate remaining shelf life
* Provide consumption recommendations
* Responsive web interface
* Cloud-hosted API using Render

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* FastAPI
* Python

### Machine Learning

* TensorFlow
* Keras
* NumPy
* Pillow

### Deployment

* GitHub
* Render

---

## Project Structure

```text
RipenIQ/
│
├── backend/
│   ├── app.py
│   ├── predictor.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── models/
│   └── banana_model.keras
│
├── results/
│   ├── confusion_matrix.png
│   ├── classification_report.txt
│   └── training_history.csv
│
└── README.md
```

---

## Model Classes

The current model predicts:

1. Unripe
2. Ripe
3. Overripe
4. Rotten

Future versions will include a **Not Banana** class to reject non-banana images.

---

## Results

* Deep Learning image classification model
* Trained on banana ripeness dataset
* Evaluation using:

  * Accuracy
  * Confusion Matrix
  * Classification Report

---

## API Endpoint

### Predict Banana Ripeness

```http
POST /predict
```

Input:

* Banana image

Output:

* Prediction
* Confidence Score
* Shelf Life
* Recommendation

---

## Future Enhancements

* Not Banana Detection
* Mobile Application
* Real-time Camera Prediction
* Multi-fruit Ripeness Detection
* Advanced Shelf-Life Analytics

---

## Author

Nehru

Developed as a Deep Learning and Full Stack AI Project.
