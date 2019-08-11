import requests
from bs4 import BeautifulSoup
from pprint import pprint

url="https://www.giveindia.org/certified-indian-ngos"

response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

main_table=soup.find("table",class_="jsx-697282504 certified-ngo-table")
trs=main_table.findAll("tr")

total_data_list=[]
for tr in trs:
    try:
        dictionary={}
        name=tr.findAll("td")
        new_list=[]
        for index in name:
            j=index.get_text()
            new_list.append(j)
        dictionary["name"]=new_list[0]
        dictionary["cause"]=new_list[1]
        dictionary["state"]=new_list[2]
        # pprint (dictionary)
        total_data_list.append(dictionary)
    

    except AttributeError:
        continue
    except IndexError:
        continue
pprint (total_data_list)
