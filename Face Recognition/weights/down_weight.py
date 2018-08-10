import requests
from bs4 import BeautifulSoup

r = requests.get(url ='https://hub.coursera-notebooks.org/user/gvtfmfmsldngrwwhfcimio/tree/week4/Face%20Recognition/weights')
bs = BeautifulSoup(r.text, "html.parser")
print(bs)