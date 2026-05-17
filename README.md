# 💸 Banknote Authentication using Naive Bayes Classifier

An interactive Machine Learning web application developed using **Python** and **Streamlit** to classify whether a banknote is **Real** or **Fake** using the **Naive Bayes Algorithm**.

This project demonstrates the practical implementation of supervised machine learning for fraud detection and classification tasks.

---

## 🚀 Project Overview

The application allows users to:

- ✅ Upload and analyze the dataset
- ✅ Train the Naive Bayes model
- ✅ Visualize dataset patterns
- ✅ Calculate model accuracy
- ✅ Predict whether a banknote is Real or Fake
- ✅ Interact with a user-friendly Streamlit interface

---

## 📌 Problem Statement

Counterfeit currency detection is an important real-world problem in banking and finance systems.

This project uses statistical features extracted from banknote images to classify notes as:

- **Real Note ✅**
- **Fake Note ❌**

using the **Naive Bayes Machine Learning Algorithm**.

---

## 🧠 Machine Learning Algorithm

## Naive Bayes Classifier

Naive Bayes is a supervised machine learning algorithm based on **Bayes’ Theorem**.

It works by calculating the probability of a banknote belonging to a specific class based on input feature values.

### Why Naive Bayes?
- Fast and efficient
- Works well for classification problems
- Handles probabilistic predictions effectively
- Suitable for smaller datasets

---

## 📂 Dataset Information

### Dataset: Banknote Authentication Dataset

The dataset contains statistical features extracted from banknote images.

| Feature | Description |
|---|---|
| Variance | Measures spread of image pixel values |
| Skewness | Measures asymmetry of pixel distribution |
| Curtosis | Measures sharpness of distribution |
| Entropy | Measures randomness in the image |
| Class | 0 = Fake Note, 1 = Real Note |

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Statistics Module
- Math Module

---

## 📁 Project Structure

```bash
naive-bayes-banknote-classifier/
│
├── app.py
├── model.py
├── data_banknote_authentication.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/naive-bayes-banknote-classifier.git
```

### 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

---

## 📊 Model Performance

The Naive Bayes model achieves approximately:

# ✅ Accuracy: 86% – 99%

depending on the train-test split and dataset conditions.

### Accuracy Formula

```text
Accuracy = (Correct Predictions / Total Predictions) × 100
```

---

## 💻 Application Features

✨ Interactive Streamlit Dashboard  
✨ Dataset Upload Support  
✨ Real-time Prediction System  
✨ Automatic Model Training  
✨ Accuracy Evaluation  
✨ Data Visualization  
✨ Banknote Classification System  

---

## 🔍 Sample Prediction

### Input Values

```text
Variance  = 3.6216
Skewness  = 8.6661
Curtosis  = -2.8073
Entropy   = -0.44699
```

### Prediction Result

```text
Fake Note ❌
```

---

## 📸 Screenshots

Add project screenshots here:

- Dataset Preview
- Accuracy Output
- Prediction Interface
- Graph Visualization

---

## 📚 Learning Outcomes

Through this project, I learned:

- Basics of Machine Learning
- Naive Bayes Classification
- Probability-based Prediction
- Dataset Preprocessing
- Model Evaluation Techniques
- Streamlit Web App Development
- Data Visualization Concepts

---

## 🏆 Certifications & Learning

Along with this project, I completed learning modules and certifications related to:

- Machine Learning Fundamentals
- Python Programming
- Data Visualization
- Power BI Basics
- AI & Data Analytics Concepts

These helped strengthen my understanding of:
- Classification Algorithms
- Data Analysis
- Predictive Modeling
- Interactive Application Development

---

## 🌟 Future Enhancements

- Add Confusion Matrix Visualization
- Implement Multiple ML Algorithms
- Improve UI/UX Design
- Deploy using Streamlit Cloud
- Add Real-time Analytics Dashboard
- Integrate Database Support

---

## 👩‍💻 Author

### Gayathri J

B.E CSE (Data Science) Student  
Aspiring Data Analyst | Machine Learning Enthusiast | AI Learner

---

## ⭐ Support

If you found this project useful, consider giving this repository a ⭐ on GitHub.
