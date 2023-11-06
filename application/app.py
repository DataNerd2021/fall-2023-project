'''This will be the Front End Application'''
import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file \
("../used-car-summer-2023-project-dfbd48707f94.json")

bigquery_client = bigquery.Client(credentials=credentials, project='used-car-summer-2023-project')

st.title('Prediction App')
