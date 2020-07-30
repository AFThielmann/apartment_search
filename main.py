import json
from pkg import WebScraper, EmailSender
import pandas as pd
import pickle


ws = WebScraper()
es = EmailSender()
with open("pkg/login.json", "r") as lg:
    LG = json.load(lg)


with open("pkg/list.txt", "rb") as fp:
    old_list = pickle.load(fp)

new_list = ws.find_links()
new_list = ws.find_links_ebay()




if new_list != old_list:
    result = set(new_list) - set(old_list)
    print('there is new content')

    es.send(str(result))
    with open("pkg/list.txt", "wb") as fp:
        pickle.dump(new_list, fp)

else:
    print("nothing new")




