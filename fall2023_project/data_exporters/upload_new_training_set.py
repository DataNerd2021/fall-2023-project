from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

credentials = service_account.Credentials.from_service_account_file(r"C:\Users\Chase\Downloads\used-car-summer-2023-project-b4807c4731d7.json")

bigquery_client = bigquery.Client(credentials=credentials, project='used-car-summer-2023-project')

@data_exporter
def upload_object():
    
    bucket_name = 'data_lake_fall_2023_project'
    dataset_id = 'training_data'
    table_id = 'raw_listings'

    destination_uri = "gs://{}/Fall 2023 Project/{}".format(bucket_name, "raw_listings.csv")
    dataset_ref = bigquery.DataSetReference(project, dataset_id)
    table_ref = dataset_ref.table(table_id)

    bigquery_client.extract_table(table_ref, destination_uri, location='US')

    print('New Training Set Uploaded to Cloud Storage Bucket')

