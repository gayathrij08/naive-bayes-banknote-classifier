import streamlit as st
import pandas as pd
import random
from model import train_model, predict, accuracy

#  Page config
st.set_page_config(page_title="Banknote Classifier", layout="wide")

st.title("💸 Banknote Authentication using Naive Bayes")

# 📂 Sidebar Navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Home", "Prediction"])

# 📂 Upload dataset (Sidebar)
file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

if file is not None:
    columns = ["variance", "skewness", "curtosis", "entropy", "class"]

    df = pd.read_csv(file,header=None,names=columns)

    # Ensure last column is 'class'
    if df.columns[-1] != "class":
        df.rename(columns={df.columns[-1]: "class"}, inplace=True)

    dataset = df.values.tolist()

    # Split dataset
    train_size = int(0.7 * len(dataset))
    train_data = random.sample(dataset, train_size)
    test_data = [x for x in dataset if x not in train_data]

    # Train model
    summaries = train_model(train_data)

    # Predictions
    predictions = [predict(summaries, row) for row in test_data]
    acc = accuracy(test_data, predictions)

    # ================= HOME PAGE =================
    if option == "Home":
        st.subheader("📊 Dataset Preview")
        st.dataframe(df)

        st.write(f"🔹 Training samples: {len(train_data)}")
        st.write(f"🔹 Testing samples: {len(test_data)}")

        st.subheader("📈 Data Visualization")
        st.line_chart(df.iloc[:, :-1])

        st.subheader("📊 Model Accuracy")
        st.progress(int(acc))
        st.success(f"{acc:.2f}% Accuracy")

    # ================= PREDICTION PAGE =================
    elif option == "Prediction":
        st.subheader("Predict Banknote")

        # 2-column layout
        col1, col2 = st.columns(2)

        with col1:
            variance = st.number_input("Variance", value=0.0)
            skewness = st.number_input("Skewness", value=0.0)

        with col2:
            curtosis = st.number_input("Curtosis", value=0.0)
            entropy = st.number_input("Entropy", value=0.0)

        input_data = [variance, skewness, curtosis, entropy]

        if st.button("🔍 Predict"):
            result = predict(summaries, input_data)

            label_map = {
                0: "❌ Fake Note",
                1: "✅ Real Note"
            }

            if result == 1:
                st.success(label_map[result])
            else:
                st.error(label_map[result])

        # Download dataset
        st.subheader("📥 Download Dataset")
        st.download_button(
            label="Download CSV",
            data=df.to_csv(index=False),
            file_name="banknote_data.csv",
            mime="text/csv"
        )

else:
    st.warning("⚠️ Please upload a dataset from the sidebar to continue.")