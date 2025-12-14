🍎 Fruit Lifecycle Prediction using AI/ML

  This project predicts how many days a fruit will take to get spoiled (waste) based on its image.
  It uses a deep learning regression model trained on fruit images with lifecycle labels and provides a Streamlit frontend where users can either:

📂 Upload an image of a fruit

📸 Capture a live photo using their webcam

The model then predicts the remaining shelf-life in days.

🚀 Features

Deep learning–based fruit freshness prediction

Regression approach instead of simple classification

Supports image upload and camera input

Clean and interactive Streamlit web interface

CPU-friendly (no GPU required)

📂 Project Structure
fruit_lifecycle/
│── app.py                  # Streamlit frontend
│── train_fruit_freshness.py # Model training script
│── predict.py              # Helper functions for inference
│── fruit_freshness.keras   # Trained model (generated locally)
│── requirements.txt        # Project dependencies
│── README.md               # Project documentation
│── dataset/                # Fruit freshness dataset
│   ├── train/
│   └── test/

📊 Dataset (Included in Repository)

The dataset used for this project is already included in the repository under the dataset/ directory.

Dataset Source

The dataset was originally sourced from Kaggle:

🔗 Kaggle Dataset Link:
👉 https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification

Dataset Description

Fruit Categories: Apples, Bananas, Oranges

Labels: Fresh / Rotten

Usage in Project:

Fresh fruits are mapped to higher shelf-life values

Rotten fruits are mapped to zero remaining days

This enables regression-based lifecycle prediction

Dataset Structure
dataset/
├── train/
│   ├── freshapples/
│   ├── freshbanana/
│   ├── freshoranges/
│   ├── rottenapples/
│   ├── rottenbanana/
│   └── rottenoranges/
└── test/
    └── (same structure as train)

🛠️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/sanskarkumar109/fruit_lifecycle_prediction.git
cd fruit_lifecycle_prediction

2️⃣ Create a virtual environment (recommended)
py -3.10 -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ (Optional) Train the model

If you want to retrain the model using the included dataset:

python train_fruit_freshness.py


This will generate:

fruit_freshness.keras

5️⃣ Run the Streamlit app
python -m streamlit run app.py


Open your browser at:

http://localhost:8501

🎯 Usage

Open the Streamlit web app

Choose one option:

Upload a fruit image 📂

Capture an image using webcam 📸

The app displays:

Estimated shelf life (days remaining)

🧠 Model Details

Architecture: MobileNetV2 (ImageNet pretrained)

Learning Type: Transfer Learning

Task: Regression (predicting days-to-waste)

Loss Function: Huber Loss

Optimizer: Adam

Output: Continuous value (0–5 days)

✅ Example

Input: Image of a fresh apple 🍏

Output:

Estimated Shelf Life: 4.8 days

📌 Future Improvements

Add more fruit categories

Multi-stage freshness levels (Fresh / Mid / Rotten)

Grad-CAM visualization

Cloud deployment (Streamlit Cloud / Hugging Face Spaces)

Mobile app integration

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue to discuss improvements.

👤 Author

Sanskar Kumar
MCA – VIT Chennai
AI & Computer Vision Enthusiast
