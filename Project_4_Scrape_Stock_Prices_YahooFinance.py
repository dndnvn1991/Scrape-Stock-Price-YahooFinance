import requests
from bs4 import BeautifulSoup
import json
from lxml import etree


#https://uk.finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch
#https://uk.finance.yahoo.com/quote/GOOGL    the same url


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
url = 'https://uk.finance.yahoo.com/quote/ASPL.L'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

dom = etree.HTML(str(soup))
#print(r.status_code)   #You can see the status code that the server returned: Nếu trả về 404 là FAIL, trả về 200 là ok 
#print(r.text)          # Kiem tra xem co lay duoc text cua HTML khong
#print(soup.title.text)

#Fw(b) Fz(36px) Mb(-4px) D(ib) - fin-streamer
#rice = soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'})

fin_streamer = dom.xpath('//div[@class="D(ib) Mend(20px)"]/fin-streamer[@data-test="qsp-price"]')

print(fin_streamer)

'''Project chua hoan thanh vi Finance Yahoo da doi cau truc website tab: Fin_streamer'''