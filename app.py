import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ocr_module import preprocess_image, extract_text_from_image

st.title("License Plate Number Identification")

uploaded_file = st.file_uploader("Upload a vehicle image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img_np = np.array(image)
    processed_img = preprocess_image(img_np)
    st.image(processed_img, caption="Processed Image (Edge Detection)", channels="GRAY")

    plate_text = extract_text_from_image(img_np)
    st.subheader("Detected License Plate Number:")
    st.code(plate_text)
