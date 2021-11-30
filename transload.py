from config import Config
from requests import post
import os
#from requests_html import HTMLSession


from bs4 import BeautifulSoup as bs

host_url = Config.host_url

def trans(link):

    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9" }
                
                

    data = dict(
        link = link,
        referer = "",
        iuser = "",
        ipass = "",
        comment = "",
        cookie= "",
        method = "tc",
        partSize = 10,
        proxy = "",
        proxyuser = "",
        proxypass  = "", 
        premium_user = "",
        premium_pass = "" ,  
        path = "/var/www/html/files"
        )

    base = f"{host_url}/index.php"


    r = post(base,data=data,headers=headers,verify=False)
    #session = HTMLSession()
    #r = session.post(base,data=data,headers=headers)
    soup = bs(r.text,"lxml")
    
    all_ = soup.find_all("input",type="hidden",attrs = {"name":True}, value=True)
    """method = soup.find()
    dis_plug = soup.find()
    filename = soup.find()
    host = soup.find()
    port = soup.find()
    path = soup.find()
    referer = soup.find()
    link = soup.find()"""

    data = {}

    for a in all_:
        data.update({a["name"]:a["value"]})
    #session = HTMLSession()
    #r = session.post(base,data=data,headers=h)
    j = post(base,data=data,headers=headers,verify=False)

    final = bs(j.text,"lxml")

    d = final.find_all("a",href=True)



    #rn = r.html.render()

   #print(r.text)

    final_link = f"{host_url}"+d[-2]["href"]

    return final_link
