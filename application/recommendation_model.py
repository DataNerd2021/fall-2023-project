import pandas as pd
from pandasql import sqldf
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

training_data = pd.read_parquet('../training_data.parquet')


X = training_data.drop(columns=['price', 'make', 'model', 'trim', 'exterior_color', 'interior_color', 'usage_type', 'city', 'state'])
y = training_data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
recommendation_model = DecisionTreeRegressor()
recommendation_model.fit(X_train, y_train)
print('Model Trained')

def RecommendationModelInference(year:int,make:str,model:str,trim:str,mileage:int,exterior_color:str,interior_color:str,num_accidents:int,num_owners:int,usage_type:str,city:str,state:str) -> str:
    '''This function is used to output an inference from the input values \n
    Parameters
    ------------
        year (int): selected year from the "year" slider on the Streamlit App. \n
        make (str): selected make from the "make" drop-down menu on the Streamlit App. This will be mapped to a label-encoded value on the backend. \n
        model (str): selected model from the "model" drop-down menu on the Streamlit App. This will be mapped to a label-encoded value on the backend. \n 
        trim (str): selected trim from the "trim" drop-down menu on the Streamlit App. This will be mapped to a label-encoded value on the backend.'''
    import streamlit as st 
    # get encoded "make" value
    make_encoded = sqldf(f"SELECT DISTINCT make_encoded FROM training_data WHERE make = '{make}'")
    make_encoded = make_encoded.values[0][0]
    # get encoded "model" value
    model_encoded = sqldf(f"SELECT DISTINCT model_encoded FROM training_data WHERE make = '{make}' AND model = '{model}'")
    model_encoded = model_encoded.values[0][0]
    # get encoded "trim" value
    trim_encoded = sqldf(f"SELECT DISTINCT trim_encoded FROM training_data WHERE trim = '{trim}'")
    trim_encoded = trim_encoded.values[0][0]
    # get encoded "exterior_color" value
    exterior_color_encoded = sqldf(f"SELECT DISTINCT exterior_color_encoded FROM training_data WHERE exterior_color = '{exterior_color}'")
    exterior_color_encoded = exterior_color_encoded.values[0][0]
    # get encoded "interior_color" value
    interior_color_encoded = sqldf(f"SELECT DISTINCT interior_color_encoded FROM training_data WHERE interior_color = '{interior_color}'")
    interior_color_encoded = interior_color_encoded.values[0][0]
    # get encoded "usage_type" value
    usage_type_encoded = sqldf(f"SELECT DISTINCT usage_type_encoded FROM training_data WHERE usage_type = '{usage_type}'")
    usage_type_encoded = usage_type_encoded.values[0][0]
    # get encoded "city" value
    city_encoded = sqldf(f"SELECT DISTINCT city_encoded FROM training_data WHERE city = '{city}'")
    city_encoded = city_encoded.values[0][0]
    # get encoded "state" value
    try:
        state_encoded = sqldf(f"SELECT DISTINCT state_encoded FROM training_data WHERE state = '{state}'")
        state_encoded = state_encoded.values[0][0]
    except:
        state_encoded = 0
    recommendation = recommendation_model.predict(X=[[year,make_encoded,model_encoded,trim_encoded,mileage,exterior_color_encoded,interior_color_encoded,num_accidents,num_owners,usage_type_encoded,city_encoded,state_encoded]])
    st.markdown(f'<h1>${recommendation[0]}</h1>', unsafe_allow_html=True)