'''This will be the Front End Application'''
import streamlit as st
import time
import polars as pl
import os
from PIL import Image
from recommendation_model import RecommendationModelInference
import os
from openai import OpenAI

client = OpenAI(api_key='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')



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
    
ext_colors = training_data.select(pl.col('exterior_color'))
ext_colors = ext_colors.unique()
ext_colors = ext_colors.sort(by=['exterior_color'])
ext_color_series = pl.Series(ext_colors.to_series())
ext_color_list = ext_color_series.to_list()

with col1:
    st.text('')
    st.text('')
    exterior_color_selector = st.selectbox(label='Exterior Color', options=[ext_color for ext_color in ext_color_list])

int_colors = training_data.select(pl.col('interior_color'))
int_colors = int_colors.unique()
int_colors = int_colors.sort(by=['interior_color'])
int_color_series = pl.Series(int_colors.to_series())
int_color_list = int_color_series.to_list()

with col2:
    st.text('')
    st.text('')
    interior_color_selector = st.selectbox(label='Interior Color', options=[int_color for int_color in int_color_list])

usage_types = training_data.select(pl.col('usage_type'))
usage_types = usage_types.unique()
usage_types = usage_types.sort(by=['usage_type'])
usage_type_series = pl.Series(usage_types.to_series())
usage_type_list = usage_type_series.to_list()
with col3:
    st.text('')
    st.text('')
    usage_type_selector = st.selectbox(label='Use Type', options=[use_type for use_type in usage_type_list])

states = training_data.select(pl.col('state'))
states = states.unique()
states = states.sort(by=['state'])
states_series = pl.Series(states.to_series())
state_list = states_series.to_list()

with col1:
    st.text('')
    st.text('')
    state_selector = st.selectbox(label='State', options=[state for state in state_list])

cities = training_data.filter(pl.col('state') == state_selector)
cities = cities.select(pl.col('city'))
cities = cities.unique()
cities = cities.sort(by=['city'])
city_series = pl.Series(cities.to_series())
city_list = city_series.to_list()

with col2:
    st.text('')
    st.text('')
    city_selector = st.selectbox(label='City', options=[city for city in city_list])

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

col7, col8 = st.columns([1,5])
with col7:
    submit_btn = st.button(label='Submit')
with col8:
    message = f'Give me specifications on the {year_selection} {make_selection} {model_selection} {trim_selection}'

    specs_btn = st.button(label='Get Specifications')
    if specs_btn:
        with st.spinner('Getting specifications...'):
            completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a motor vehicle journalist giving a brief overview of vehicles you are reviewing."},
                {"role": "user", "content": f"{message}"}
            ]
            )
            area = st.text_area(label='Output', value=completion.choices[0].message.content, height=500)

if submit_btn:
    with st.spinner('Running inference...'):
        RecommendationModelInference(year_selection,make_selection,model_selection,trim_selection,mileage_input,exterior_color_selector,interior_color_selector,accidents_input,owners_input,usage_type_selector,city_selector,state_selector)