'''This will be the Front End Application'''
import streamlit as st
import polars as pl
import os
from PIL import Image

st.set_page_config(page_title='Price Recommendation App')
st.title('Selling Price Recommendation App')
training_data = pl.read_parquet('../training_data.parquet')
year_selection = st.slider(label='Year', min_value=2011, max_value=2023)

col1, col2, col3 = st.columns([1,1,1])

# makes query
filtered_year_data = training_data.filter(pl.col('year') == year_selection)
makes = filtered_year_data.select(pl.col('make'))
makes = makes.unique()
makes = makes.sort(by=['make'])
makes_series = pl.Series(makes.to_series())
makes_list = makes_series.to_list()



with col1:
    make_selection = st.selectbox(label='Make', options=[make for make in makes_list])
    st.text('')
    st.text('')
    mileage_input = st.number_input(label='Mileage', min_value=0, max_value=128000, value=0, step=1000)

filtered_model_data = training_data.filter((pl.col('year') == year_selection) & (pl.col('make') == make_selection))
models = filtered_model_data.select(pl.col('model'))
models = models.unique()
models = models.sort(by=['model'])
models_series = pl.Series(models.to_series())
models_list = models_series.to_list()

with col2:
    model_selection = st.selectbox(label='Model', options=[model for model in models_list])
    st.text('')
    st.text('')
    accidents_input = st.number_input(label="\# of Accidents", min_value=0, max_value=3, value=0)
    
filtered_trim_data = filtered_model_data.filter(pl.col('model') == model_selection)
trims = filtered_trim_data.select(pl.col('trim'))
trims = trims.unique()
trims = trims.sort(by=['trim'])
trims_series = pl.Series(trims.to_series())
trims_list = trims_series.to_list()

with col3:
    trim_selection = st.selectbox(label='Trim', options=[trim for trim in trims_list])
    st.text('')
    st.text('')
    owners_input = st.number_input(label="\# of Owners", min_value=0, max_value=5, value=1)
    
filtered_ext_color_data = training_data.filter((pl.col('year') == year_selection) & (pl.col('make') == make_selection) & (pl.col('model') == model_selection))
ext_colors = filtered_ext_color_data.select(pl.col('exterior_color'))
ext_colors = ext_colors.unique()
ext_colors = ext_colors.sort(by=['exterior_color'])
ext_color_series = pl.Series(ext_colors.to_series())
ext_color_list = ext_color_series.to_list()

with col1:
    st.text('')
    st.text('')
    st.selectbox(label='Exterior Color', options=[ext_color for ext_color in ext_color_list])

filtered_int_color_data = training_data.filter((pl.col('year') == year_selection) & (pl.col('make') == make_selection) & (pl.col('model') == model_selection))
int_colors = filtered_int_color_data.select(pl.col('interior_color'))
int_colors = int_colors.unique()
int_colors = int_colors.sort(by=['interior_color'])
int_color_series = pl.Series(int_colors.to_series())
int_color_list = int_color_series.to_list()

with col2:
    st.text('')
    st.text('')
    st.selectbox(label='Interior Color', options=[int_color for int_color in int_color_list])


col4, col5, col6 = st.columns([1,1,1])
try:
    path = f'../images/{year_selection}/{make_selection.lower()}/{model_selection.lower()}'
    file_path1 = os.listdir(path)[0]
    file_path2 = os.listdir(path)[1]
    file_path3 = os.listdir(path)[2]
    with col4:
        image1 = Image.open(path+"\\"+file_path1)
        st.image(image1, use_column_width='always', caption='src: Google Images')
    with col5:
        image2 = Image.open(path+"\\"+file_path2)
        st.image(image2, use_column_width='always', caption='src: Google Images')
    with col6:
        image3 = Image.open(path+"\\"+file_path3)
        st.image(image3, use_column_width='always', caption='src: Google Images')
except FileNotFoundError:
    st.text('No Images Available')
except IndexError:
    st.text('No Images Available')