# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:37:22 2024

@author: Sans
"""

import streamlit as st
from PIL import Image

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://t4.ftcdn.net/jpg/05/06/20/13/360_F_506201358_3AxMTSbWHoT1H5qwWYJgppSgRVeiU6Jp.jpg");
background-size: cover;    
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
                                  
                                  
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

chel = Image.open('Chel.jpg')
sans = Image.open("Sans.jpg")

chel = chel.resize((1024, 1024))
sans = sans.resize((1024, 1024))

st.title("About Us")

col1, col2 = st.columns(2)
col1.image(chel, use_column_width=True)
col1.title("Rachel Joy Pineda")
col1.subheader("Back End Developer")
col1.subheader("3rd Year CpE Student")
col1.subheader("qrjdpineda@tip.edu.ph")


col2.image(sans, use_column_width=True)
col2.title("Jon Aviv Cloydd Gamundoy")
col2.subheader("Front End Developer")
col2.subheader("3rd Year CpE Student")
col2.subheader("qjacsgamundoy@tip.edu.ph")


st.sidebar.title("Emerging Techonologies 2")
st.sidebar.header("Final Examination")
st.sidebar.subheader("Instructor:")
st.sidebar.write(" Engr. Roman Richard")
st.sidebar.subheader("\n")
st.sidebar.subheader("Section:")
st.sidebar.write("CpE32S3")
st.sidebar.subheader("\n")

st.sidebar.subheader("Date Submitted:")
st.sidebar.write("05/18/2024")

