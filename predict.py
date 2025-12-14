import tensorflow as tf
import numpy as np
import cv2

# Load model ONCE (important for Streamlit performance)
model = tf.keras.models.load_model("fruit_freshness.keras")

IMG_SIZE = 224

def predict_days(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)[0][0]
    pred = np.clip(pred, 0, 5)

    return round(float(pred), 1)
