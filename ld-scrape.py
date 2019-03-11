import requests,codecs
from bs4 import BeautifulSoup
import json
import re
import api
hdr = {'User-Agent': 'Mozilla/5.0'}
def _scrapeProduct(url):
    product = {}
    with requests.get(url,headers=hdr)  as page_response:
        soup = BeautifulSoup(page_response.content, 'lxml')
        amount = soup.findAll("span",{"class": "woocommerce-Price-amount"})
        addons = soup.findAll("div",{"class": "product-addon"})
        product_title= soup.findAll("h1",{"class": "product_title"})
        description = soup.findAll("div",{"id": "content_show"})
        images = soup.findAll("div",{"class":"images"})[0].findAll("a")
    imgs = [i["href"] for i in images]
    product["Images"] = ",".join(imgs)
    product["Name"] = product_title[0].text
    product["Price"] = amount[0].text
    product["Description"] = description[0].text.replace("Fence Workshop","Aluminum Fence Contractor")
    return product 

data = [_scrapeProduct("https://fenceworkshop.com/product/athens-double-driveway-gate/")]
print data
with open('data.json', 'w') as f:
        json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False,indent=4)
api.json_to_csv('data.json',"out.csv")
# with open('data_'+now.strftime("%Y-%m-%d %H:%M")+'.json', 'w') as f:
#         json.dump(json_o, codecs.getwriter('utf-8')(f), ensure_ascii=False,indent=4)