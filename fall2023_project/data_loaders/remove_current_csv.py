from google.cloud import storage

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def remove_object():
    storage_client = storage.Client.from_service_account_json('used-car-summer-2023-project-dfbd48707f94.json')
    bucket = storage.Bucket(storage_client, 'data_lake_fall_2023_project')
    blob = bucket.blob('Fall 2023 Project/raw_listings.csv')
    blob.delete()
    print('Old Training Set Removed')

