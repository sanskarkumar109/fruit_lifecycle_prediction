# 🍎 Fruit Lifecycle Prediction using AI/ML

This project predicts **how many days a fruit will take to get spoiled (waste)** based on its image.  
It uses a **deep learning regression model** trained on fruit images with lifecycle labels, and provides a **Streamlit frontend** where users can either:

- 📂 Upload an image of a fruit  
- 📸 Capture a live photo using their webcam  

The model then predicts the **remaining shelf-life in days**.

---

## 🚀 Features
- Trains a deep learning model on fruit lifecycle dataset.  
- Supports **image upload** and **camera input** in Streamlit.  
- Predicts fruit freshness in **number of days left before waste**.  
- User-friendly **web interface** built with Streamlit.  

---

## 📂 Project Structure
fruit_lifecycle/
│── app.py # Streamlit frontend
│── models.py # Model training & saving
│── predict.py # Helper functions for inference
│── requirements.txt # Dependencies
│── README.md # Project documentation
│── dataset/ # Dataset folder
│ ├── train/ # Training images
│ └── test/ # Testing images
│── saved_model/ # Trained model will be saved here

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fruit-lifecycle-prediction.git
cd fruit-lifecycle-prediction
2. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux
3. Install dependencies
pip install -r requirements.txt
4. Run training (optional if you want to retrain)
python models.py
5. Start the Streamlit app
streamlit run app.py
🎯 Usage
Open the Streamlit app (usually at http://localhost:8501).

Choose either:

Upload a fruit image, or

Capture a live image with your webcam.

Click Predict.

The app will display the predicted days left before the fruit becomes waste.

📊 Model Details
Architecture: Transfer Learning with ResNet50 (pretrained on ImageNet).

Task: Regression (predicting days-to-waste).

Loss Function: Mean Squared Error (MSE).

Optimizer: Adam.

✅ Example
Input: Image of a fresh apple 🍏

Output: Predicted: 5.3 days before waste

📌 Future Improvements
Add support for more fruit categories.

Improve accuracy with advanced architectures (EfficientNet, Vision Transformers).

Deploy the app on Streamlit Cloud / Hugging Face Spaces.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.
