from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 3
    )
def getData(url):
    r = requests.get(url)
    return r.text


if __name__=='__main__':
    while True:
        #notifyMe("Ujala","Lets stop the spread of this virus ")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print(soup.prettify())
        myDatastr = ""
        #print(soup.select('tbody[id*="site-dashboard"]'))
        for tr in soup.find_all("strong",class_="mob-hide"):
            myDatastr += tr.get_text()+'\n'
            #print(tr.get_text())
        l=myDatastr.split()
        mes="";
        mes+='Active Case:'
        mes+=l[l.index("Active")+1]
        mes+='\nDischarged Case:'+l[l.index("Discharged")+1]
        mes+='\nDeaths Case:'+l[l.index("Deaths")+1]
        mes+="\nTotal Vaccinated:"+soup.find("span",class_="coviddata").get_text()
        notifyMe('Covid Update',mes)
        #notifyMe()
                #notifyMe()
                #time.sleep(2)
        time.sleep(3600)
