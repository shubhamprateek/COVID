from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10 
    )

def getData(url):
    r = requests.get(url)
    return r.text
 
if __name__ == "__main__":
    while True:

        #notifyMe("Shubham","Let's stop the spread of this virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')
        #print(myHtmlData)
        soup = BeautifulSoup(myHtmlData,'html.parser')
        #print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")
        states = ['Bihar','Odisha','West Bengal']
        for item in itemList[0:35]:
            dataList=item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State : {dataList[1]}\nActive Cases :  {dataList[2]}\nCured :  {dataList[3]}\nDeaths :  {dataList[4]}\nTotal Cases :  {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(2)
        time.sleep(3000)
