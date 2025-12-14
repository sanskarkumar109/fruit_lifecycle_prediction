import streamlit as st
import cv2
import tempfile
from predict import predict_days

# -------- Page Config (MUST be first Streamlit call) --------
st.set_page_config(
    page_title="Fruit Freshness Predictor",
    page_icon="🍎",
    layout="centered"
)

st.title("🍎 Fruit Freshness Predictor")
st.write("Upload a fruit image or capture with your webcam to know how many days it will last!")

# -------- Upload option --------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.read())
        days = predict_days(tmp_file.name)
        st.image(uploaded_file, caption="Uploaded Fruit", use_column_width=True)
        st.success(f"✅ Estimated Shelf Life: {days} days")

# -------- Camera option --------
camera_input = st.camera_input("Or take a picture")
if camera_input:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(camera_input.read())
        days = predict_days(tmp_file.name)
        st.image(camera_input, caption="Captured Fruit", use_column_width=True)
        st.success(f"✅ Estimated Shelf Life: {days} days")
