'''This will be the Front End Application'''
import streamlit as st
from PIL import Image

st.title('Prediction App')

image = Image.open(r'C:\Users\Chase\OneDrive\Documents\fall-2023-project\images\2011\dodge\challenger\000001.jpg')
st.image(image, width=250)