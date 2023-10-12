import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import random
import warnings
warnings.filterwarnings('ignore')

class get_listings():
    def scrape_listings():
        page_num = 1
        while page_num <= 50:
            # define cities to locate
            # define url to scrape

            url= f'https://www.truecar.com/used-cars-for-sale/listings/?page={page_num}'

            # confirm HTTP response
            
            response = requests.get(url, timeout=10)
                    
            # define parser variable
            
            soup = BeautifulSoup(response.content, 'html.parser')

            results = soup.find_all('div', {'class' : 'linkable card card-shadow vehicle-card'})
                
                # get individual attributes and append to List
                
            vin = []
            header = []
            trim = []
            price = []
            mileage = []
            location = []
            colors = []
            other_info = []

            for result in results:
            
                    # vin
                    try:
                        vin.append(result.find('div', {'class':'vehicle-card-vin-carousel mt-1 text-xs'}).get_text())
                    except:
                        break
                    
                    try:
                        header.append(result.find('div', {'class': 'vehicle-card-header w-full'}).get_text())
                    except:
                        break
                    
                    try:
                        trim.append(result.find('div', {'class': 'truncate text-xs'}).get_text())
                    except:
                        break
                    
                    try:
                        price.append(result.find('div', {'data-test':'vehicleCardPricingBlockPrice'}).get_text())
                    except:
                        break
                    try:
                        mileage.append(result.find('div', {'data-test':'vehicleMileage'}).get_text())
                    except:
                        break
                    try:
                        location.append(result.find('div', {'data-test':'vehicleCardLocation'}).get_text())
                    except:
                        break
                    try:
                        colors.append(result.find('div', {'data-test':'vehicleCardColors'}).get_text())
                    except:
                        break
                    try:
                        other_info.append(result.find('div', {'data-test':'vehicleCardCondition'}).get_text())
                    except:
                        break
            try:
                car_listings = pd.DataFrame({'page_num':page_num, 'vin': vin, 'header':header, 'trim':trim, 'price':price, 'mileage':mileage, 'location':location, 'colors':colors, 'condition':other_info})
            except ValueError:
                print('Invalid Schema. Try again.')
                break
                
            car_listings.to_csv('raw_listings.csv', mode='a', index=False, header=False)
            print(f'Page {page_num} scraped and loaded')
            page_num += 1

get_listings.scrape_listings()