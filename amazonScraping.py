import collections
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
data_scraped = []

amazon_asin_country = pd.read_csv('Sheet1.csv', index_col='S.No.')
headerAgent = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
for i in range(0,200,2):
    asin = amazon_asin_country.at[i,"Asin"]
    country = amazon_asin_country.at[i,"country"]
    product_data = collections.defaultdict(dict)
    response = requests.get("https://www.amazon.{}/dp/{}".format(country, asin), headers=headerAgent, allow_redirects=False)
    print(response.status_code)
    if response.status_code == 200:
        try:
            driver.get("https://www.amazon.{}/dp/{}".format(country, asin))
            driver.implicitly_wait(10)
            # title
            try:
                product_data["Title"] = driver.find_element(By.XPATH, "//span[@id='productTitle']").text
            except Exception:
                product_data["Title"] = "Not found"
                pass
            # Image URL
            try:
                product_data["Image URL"] = driver.find_element(By.XPATH, "//img[@id='imgBlkFront']").get_attribute("src")
            except Exception:
                product_data["Image URL"] = 'Not Found'
                pass

           # price
            try:
                product_data["Price"] = driver.find_element(By.XPATH, "(//span[contains(@class,'a-color-price')])[1]").text
            except Exception:
                product_data["Price"] = "not found"
                pass
            # details
            try:
                product_details = driver.find_element(By.XPATH, "//div[@id='detailBulletsWrapper_feature_div']//div[@id='detailBullets_feature_div']").text
                product_data["Details"] = product_details[16:]
            except Exception:
                product_data["Details"]="not found"
                pass
            # print(product_data.values())
            data_scraped.append(product_data)
        except Exception:
            print("An exception occured")
            pass
    else:
        print("Error " + str(response.status_code) + " : URL not available")


print(data_scraped)
with open('data.json', 'a') as f:
    f.write(final_Data = json.dumps(data_scraped, indent=2))

