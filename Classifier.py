# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:30:39 2024

@author: Sans
"""
# Library Inclusion
import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model

# Multipage
st.set_page_config(
    page_title="Multipage App",
)

# Background Image
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://plus.unsplash.com/premium_photo-1664303017917-71ebeb42343d?q=80&w=1973&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;    
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
</style>
"""

# Markdown for Background Image
st.markdown(page_bg_img, unsafe_allow_html=True)

# Loading the model
model = load_model('weather_model.h5')

# Title text
st.title("Weather Classifier")

# File Upload Widget
file = st.file_uploader("Upload your Image here", type=["jpg", "png", "jpeg"])

classes = {
    0: 'Rain',
    1: 'Shine',
    2: 'Cloudy',
    3: 'Sunrise'
}


# Show uploaded image
if file is not None:
    st.image(file, caption='Uploaded Image', use_column_width=True)

# Running the model
    try:
        image = Image.open(file)
        image = image.resize((32, 32), 3)
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        
        predict = model.predict(image)
        predict_class = np.argmax(predict, axis=1)[0]
        
        if predict_class in classes:
            prediction = classes[predict_class]
            st.success(f"Prediction: {prediction}")
        else:
            st.warning("Cannot Predict")
            
    except Exception as e:
        st.warning("Invalid image")


# Sidebar contentss
st.sidebar.header("Weather Classifier")

st.sidebar.write("This app aims to classify images according to the following categories:")

for index, item in classes.items():
    st.sidebar.write(f"- {item}")















#