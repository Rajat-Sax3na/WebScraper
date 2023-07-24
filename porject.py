import string
from bs4 import BeautifulSoup
import pandas as pd
import requests


HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36','Accept-Language':
 'en-US, en;q=0.5'})

# choice = input("smartphones,tablets or laptops?")

# if choice == 'laptop':
# url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
# elif choice == 'smartphones':
#     pass
# elif choice == 'tablet':
#     pass

names = []
prices = []
rating = []


for x in range(10):
    k = requests.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={}".format(x)).text
    soup = BeautifulSoup(k,"htmlparser")


    for i in soup.find_all('a',{'class':'_1fQZEK'}):
        productName = i.find('div', attrs = {'class':'_4rR01T'})
        productPrice = i.find('div',attrs = {'class':'_30jeq3 _1_WHN1'})
        productRating = i.find('div',attrs = {'class':'_3LWZlK'})

        if productName and productRating and productPrice:
            names.append(productName.text)
            prices.append(productPrice.text)
            rating.append(productRating.text)

df = pd.DataFrame({'Product Name':names,'Prices':prices,'Rating':rating})
print(df)

df.to_csv('products.csv', index=False, encoding='utf-8')