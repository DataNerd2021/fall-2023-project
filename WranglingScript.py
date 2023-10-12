
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import findspark

findspark.init()
findspark.find()

credentials = service_account.Credentials.from_service_account_file(r"C:\Users\Chase\Downloads\used-car-summer-2023-project-b4807c4731d7.json")

bigquery_client = bigquery.Client(credentials=credentials, project='used-car-summer-2023-project')


query = bigquery_client.query('SELECT * FROM `training_data.raw_listings`').result()

staged_listings = query.to_dataframe()

from pyspark.sql import SparkSession, Row
from pyspark.sql.types import *
from pyspark.sql.functions import *

spark = (
            SparkSession
            .builder
            .appName("UsedCarDataWranglingApp")
            .master("local[4]")
            .config("spark.dynamicAllocation.enabled", "false")
            .config("spark.sql.adaptive.enabled", "false")
            .getOrCreate()
)

sc = spark.sparkContext

#@data_loader
def load_data(*args, **kwargs):
    # create DataFrame object
    staged_listings = (
                    spark
                    .createDataFrame
                    (staged_listings,
                     "page_num: integer, vin: string, header: string, trim: string, price: string, mileage: string, location: string, colors: string, condition: string")
    )
    # drop duplicate values
    staged_listings = (
                    staged_listings
                    .dropDuplicates(subset=['vin', 'header', 'mileage'])
    )
    # remove unnecessary columns
    staged_listings = (
                    staged_listings
                    .drop('page_num', 'vin')
    )
    
    staged_listings = (
                    staged_listings
                    .filter(~col('header').contains('Land'))
                    .filter(~col('header').contains('Alfa'))
                    .filter(~col('header').contains('Aston'))
    )
    
    staged_listings.show()
# Specify your data loading logic here

load_data()
