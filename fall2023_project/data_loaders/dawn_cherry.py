import datetime
from bs4 import BeautifulSoup
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import requests


credentials = service_account.Credentials.from_service_account_file(r"C:\Users\Chase\Downloads\used-car-summer-2023-project-b4807c4731d7.json")

bigquery_client = bigquery.Client(credentials=credentials, project='used-car-summer-2023-project')

@data_loader
def load_data(*args, **kwargs):
    if datetime.datetime.now().minute < 10:
        page_num = 1
        max_page_num = 25
    elif datetime.datetime.now().minute < 20:
        page_num = 26
        max_page_num = 50
    elif datetime.datetime.now().minute < 30:
        page_num = 51
        max_page_num = 75
    elif datetime.datetime.now().minute < 40:
        page_num = 76
        max_page_num = 100
    elif datetime.datetime.now().minute < 50:
        page_num = 101
        max_page_num = 125
    else:
        page_num = 126
        max_page_num = 150
    while page_num <= max_page_num:
        # define make to scrape
        if (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 1):
            make = 'chrysler'
            model = 'pacifica'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 2):
            make = 'mitsubishi'
            model = 'mirage'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 3):
            make = 'nissan'
            model = 'altima'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 4):
            make = 'subaru'
            model = 'crosstrek'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 5):
            make = 'acura'
            model = 'mdx'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 6):
            make = 'dodge'
            model = 'grand-caravan'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 7):
            make = 'ram'
            model = '1500'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 8):
            make = 'hyundai'
            model = 'santa-fe'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 9):
            make = 'kia'
            model = 'sorento'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 10):
            make = 'buick'
            model = 'enclave'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 11):
            make = 'audi'
            model = 'q5'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 12):
            make = 'hyundai'
            model = 'kona'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 13):
            make = 'mazda'
            model = 'mx-5-miata'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 14):
            make = 'toyota'
            model = 'avalon'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 15):
            make = 'chevrolet'
            model = 'tahoe'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 16):
            make = 'hyundai'
            model = 'sonata'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 17):
            make = 'volkswagen'
            model = 'golf'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 18):
            make = 'dodge'
            model = 'durango'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 19):
            make = 'lexus'
            model = 'is'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 20):
            make = 'infiniti'
            model = 'q50'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 21):
            make = 'mini'
            model = 'cooper'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 22):
            make = 'lincoln'
            model = 'navigator'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 23):
            make = 'bmw'
            model = '3-series'
        elif (datetime.datetime.now().weekday() == 1) & (datetime.datetime.now().hour == 0):
            make = 'mercedes-benz'
            model = 'c-class'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 1):
            make = 'chrysler'
            model = '300'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 2):
            make = 'mitsubishi'
            model = 'outlander'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 3):
            make = 'nissan'
            model = 'sentra'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 4):
            make = 'subaru'
            model = 'outback'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 5):
            make = 'acura'
            model = 'rdx'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 6):
            make = 'mazda'
            model = 'cx-30'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 7):
            make = 'ram'
            model = '2500'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 8):
            make = 'hyundai'
            model = 'tucson'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 9):
            make = 'kia'
            model = 'sportage'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 10):
            make = 'buick'
            model = 'encore'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 11):
            make = 'audi'
            model = 'q7'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 12):
            make = 'ford'
            model = 'f-250'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 13):
            make = 'chevrolet'
            model = 'colorado'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 14):
            make = 'toyota'
            model = 'tundra'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 15):
            make = 'ford'
            model = 'edge'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 16):
            make = 'toyota'
            model = 'land-cruiser'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 17):
            make = 'chevrolet'
            model = 'malibu'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 18):
            make = 'dodge'
            model = 'journey'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 19):
            make = 'lexus'
            model = 'ls'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 20):
            make = 'infiniti'
            model = 'qx50'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 21):
            make = 'mini'
            model = 'hardtop'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 22):
            make = 'lincoln'
            model = 'aviator'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 23):
            make = 'bmw'
            model = '5-series'
        elif (datetime.datetime.now().weekday() == 2) & (datetime.datetime.now().hour == 0):
            make = 'mercedes-benz'
            model = 'e-class'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 1):
            make = 'nissan'
            model = 'murano'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 2):
            make = 'mitsubishi'
            model = 'outlander-sport'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 3):
            make = 'nissan'
            model = 'frontier'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 4):
            make = 'subaru'
            model = 'impreza'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 5):
            make = 'acura'
            model = 'ilx'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 6):
            make = 'mazda'
            model = 'cx-9'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 7):
            make = 'ram'
            model = '3500'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 8):
            make = 'hyundai'
            model = 'elantra'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 9):
            make = 'kia'
            model = 'sedona'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 10):
            make = 'buick'
            model = 'encore-gx'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 11):
            make = 'audi'
            model = 'q3'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 12):
            make = 'ford'
            model = 'fusion'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 13):
            make = 'chevrolet'
            model = 'traverse'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 14):
            make = 'toyota'
            model = 'sienna'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 15):
            make = 'honda'
            model = 'pilot'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 16):
            make = 'honda'
            model = 'odyssey'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 17):
            make = 'volkswagen'
            model = 'taos'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 18):
            make = 'dodge'
            model = 'challenger'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 19):
            make = 'lexus'
            model = 'lx'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 20):
            make = 'infiniti'
            model = 'qx80'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 21):
            make = 'mini'
            model = 'countryman'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 22):
            make = 'lincoln'
            model = 'mkz'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 23):
            make = 'bmw'
            model = 'x3'
        elif (datetime.datetime.now().weekday() == 3) & (datetime.datetime.now().hour == 0):
            make = 'mercedes-benz'
            model = 'glc'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 1):
            make = 'nissan'
            model = 'titan'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 2):
            make = 'mitsubishi'
            model = 'eclipse-cross'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 3):
            make = 'nissan'
            model = 'versa'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 4):
            make = 'subaru'
            model = 'forester'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 5):
            make = 'acura'
            model = 'tlx'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 6):
            make = 'mazda'
            model = 'mazda3'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 7):
            make = 'ford'
            model = 'expedition'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 8):
            make = 'hyundai'
            model = 'accent'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 9):
            make = 'honda'
            model = 'ridgeline'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 10):
            make = 'buick'
            model = 'century'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 11):
            make = 'audi'
            model = 'a6'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 12):
            make = 'chevrolet'
            model = 'cruze'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 13):
            make = 'chevrolet'
            model = 'camaro'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 14):
            make = 'volkswagen'
            model = 'passat'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 15):
            make = 'gmc'
            model = 'canyon'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 16):
            make = 'jeep'
            model = 'renegade'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 17):
            make = 'jeep'
            model = 'gladiator'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 18):
            make = 'chrysler'
            model = 'town-country'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 19):
            make = 'lexus'
            model = 'es'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 20):
            make = 'infiniti'
            model = 'qx60'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 21):
            make = 'mini'
            model = 'convertible'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 22):
            make = 'lincoln'
            model = 'nautilus'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 23):
            make = 'bmw'
            model = 'x5'
        elif (datetime.datetime.now().weekday() == 4) & (datetime.datetime.now().hour == 0):
            make = 'mercedes-benz'
            model = 'gle'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 1):
            make = 'honda'
            model = 'passport'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 2):
            make = 'subaru'
            model = 'legacy'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 3):
            make = 'nissan'
            model = 'armada'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 4):
            make = 'subaru'
            model = 'ascent'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 5):
            make = 'acura'
            model = 'tsx'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 6):
            make = 'mazda'
            model = 'mazda6'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 7):
            make = 'ford'
            model = 'focus'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 8):
            make = 'hyundai'
            model = 'genesis'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 9):
            make = 'kia'
            model = 'telluride'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 10):
            make = 'buick'
            model = 'encore-gx'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 11):
            make = 'audi'
            model = 'a3'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 12):
            make = 'ford'
            model = 'fiesta'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 13):
            make = 'chevrolet'
            model = 'sonic'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 14):
            make = 'toyota'
            model = 'yaris'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 15):
            make = 'honda'
            model = 'fit'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 16):
            make = 'jeep'
            model = 'patriot'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 17):
            make = 'volkswagen'
            model = 'beetle'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 18):
            make = 'dodge'
            model = 'dart'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 19):
            make = 'lexus'
            model = 'rx'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 20):
            make = 'infiniti'
            model = 'q60'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 21):
            make = 'chevrolet'
            model = 'spark'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 22):
            make = 'lincoln'
            model = 'towncar'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 23):
            make = 'bmw'
            model = 'x6'
        elif (datetime.datetime.now().weekday() == 5) & (datetime.datetime.now().hour == 0):
            make = 'mercedes-benz'
            model = 'gla'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 1):
            make = 'chevrolet'
            model = 'corvette'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 2):
            make = 'ford'
            model = 'excursion'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 3):
            make = 'tesla'
            model = 'model-3'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 4):
            make = 'subaru'
            model = 'wrx'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 5):
            make = 'tesla'
            model = 'model-y'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 6):
            make = 'mazda'
            model = 'mazda5'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 7):
            make = 'tesla'
            model = 'model-s'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 8):
            make = 'nissan'
            model = '370z'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 9):
            make = 'nissan'
            model = 'kicks'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 10):
            make = 'buick'
            model = 'verano'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 11):
            make = 'buick'
            model = 'regal'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 12):
            make = 'ford'
            model = 'ranger'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 13):
            make = 'chevrolet'
            model = 'trax'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 14):
            make = 'ford'
            model = 'maverick'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 15):
            make = 'kia'
            model = 'optima'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 16):
            make = 'nissan'
            model = 'pathfinder'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 17):
            make = 'hyundai'
            model = 'azera'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 18):
            make = 'kia'
            model = 'k5'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 19):
            make = 'chevrolet'
            model = 'trailblazer'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 20):
            make = 'chevrolet'
            model = 'blazer'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 21):
            make = 'volkswagen'
            model = 'new-beetle'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 22):
            make = 'honda'
            model = 'element'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 23):
            make = 'toyota'
            model = 'prius'
        elif (datetime.datetime.now().weekday() == 6) & (datetime.datetime.now().hour == 0):
            make = 'honda'
            model = 'crosstour'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 1):
            make = 'honda'
            model = 'cr-z'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 2):
            make = 'dodge'
            model = 'avenger'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 3):
            make = 'nissan'
            model = 'maxima'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 4):
            make = 'ford'
            model = 'ecosport'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 5):
            make = 'toyota'
            model = '4runner'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 6):
            make = 'toyota'
            model = 'sequoia'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 7):
            make = 'porsche'
            model = 'cayenne'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 8):
            make = 'kia'
            model = 'rio'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 9):
            make = 'dodge'
            model = 'magnum'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 10):
            make = 'honda'
            model = 'hr-v'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 11):
            make = 'volvo'
            model = 's90'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 12):
            make = 'volvo'
            model = 'xc90'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 13):
            make = 'volco'
            model = 'xc60'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 14):
            make = 'volvo'
            model = 's60'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 15):
            make = 'mazda'
            model = 'cx-3'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 16):
            make = 'mazda'
            model = 'cx-30'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 17):
            make = 'volkswagen'
            model = 'atlas'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 18):
            make = 'chrysler'
            model = 'aspen'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 19):
            make = 'lexus'
            model = 'nx'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 20):
            make = 'nissan'
            model = '350z'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 21):
            make = 'mitsubishi'
            model = 'lancer'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 22):
            make = 'lincoln'
            model = 'mkc'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 23):
            make = 'lincoln'
            model = 'mkt'
        elif (datetime.datetime.now().weekday() == 0) & (datetime.datetime.now().hour == 0):
            make = 'lincoln'
            model = 'mks'
        else:
            make = 'porsche'
            model = 'macan'
        # define url

load_data()
