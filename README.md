Naive Bayes Classifier for Banknote Authentication 💸

A Machine Learning web application built using Python and Streamlit to classify whether a banknote is Real or Fake using the Naive Bayes Algorithm.

📌 Project Overview

This project uses the Banknote Authentication Dataset and applies the Naive Bayes Classification Algorithm to predict the authenticity of banknotes based on four statistical features:

Variance
Skewness
Curtosis
Entropy

The application provides:

Dataset upload
Dataset visualization
Model training
Accuracy calculation
Real-time prediction through a web interface
🧠 Algorithm Used
Naive Bayes Classifier

Naive Bayes is a probabilistic machine learning algorithm based on Bayes Theorem.

It assumes that:

All features are independent of each other.

The model calculates probabilities for each class and predicts the class with the highest probability.

📂 Dataset Used
Banknote Authentication Dataset

Features:

Feature	Description
Variance	Measures spread of pixel values
Skewness	Measures asymmetry
Curtosis	Measures sharpness/tailedness
Entropy	Measures randomness
Class	0 = Fake Note, 1 = Real Note

Dataset Source: Kaggle

🚀 Technologies Used
Python
Streamlit
Pandas
Statistics Module
Math Module
📁 Project Structure
naive_bayes_project/
│
├── app.py
├── model.py
├── requirements.txt
├── data_banknote_authentication.csv
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone <your-github-repo-link>
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit App
streamlit run app.py
📊 Model Accuracy

The model achieves approximately:

86% - 99% Accuracy

depending on the train-test split.

Accuracy Formula:

Accuracy=
Total Predictions
Correct Predictions
	​

×100

💻 Features of the Application

✅ Upload CSV Dataset
✅ Train Naive Bayes Model
✅ View Dataset Preview
✅ Visualize Feature Distribution
✅ Predict Real/Fake Banknotes
✅ Interactive Streamlit UI
✅ Accuracy Evaluation

🎯 Sample Prediction
Input
Variance  = 3.6216
Skewness  = 8.6661
Curtosis  = -2.8073
Entropy   = -0.44699
Output
Fake Note ❌
📸 Screenshots

Add screenshots of:

Dataset Preview
Accuracy Output
Prediction Interface
📚 Learning Outcomes

Through this project, I learned:

Machine Learning basics
Naive Bayes Classification
Probability-based prediction
Dataset preprocessing
Streamlit web application development
Model evaluation using accuracy
👩‍💻 Author

Gayathri J

Engineering Student | Machine Learning Enthusiast

⭐ Future Improvements
Add Confusion Matrix
Add Graphical Analytics
Deploy using Streamlit Cloud
Improve UI Design
Add Multiple ML Algorithms
📜 License

This project is created for educational and learning purposes.
