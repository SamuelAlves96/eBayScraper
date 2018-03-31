import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
product_name=input("What do you want to search? ")
product_name=product_name.replace(" ","+")
my_url= 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.X'+product_name+'.TRS0&_nkw='+product_name+'&_sacat=0'

#opens the conection and grabs the page
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers=page_soup.findAll("li", {"class":"sresult lvresult clearfix li shic"})

file=input("Name of the file you want to create: ")
filename= file+".csv"
f= open(filename, "w", encoding="utf8")
headers = "name; price_bef; price_now; perc; shipping fee; shipping; state; quantity; link\n"

f.write(headers)
for container in containers:
        name = container.find("h3" , {"class": "lvtitle"}).text.strip()
     
        try:
            free_shipping = container.find("span", {"class": "bfsp"}).text.strip()
            fee="noone"
        except:
            free_shipping="no free shipping"
            fee=container.find("span", {"class":"fee"}).text.strip()


        try:
            price_bef = container.find("span", {"class":"stk-thr"}).text.strip()
            price_now=container.find("span", {"class":"bold"}).text.strip()

        except:
            price_now=container.find("span", {"class":"bold"}).text.strip()
            price_bef="no discount"

        try:
            perc=container.find("div", {"class": "hotness-signal black"}).text.strip()
        except:
            perc="0%"
            
        link = container.h3.a["href"].strip()
        try:
                state=container.find("div", {"class": "lvsubtitle"}).text.strip()
        except:
                state="no information"
        try:
            quantity=container.find("div", {"class": "hotness-signal red"}).text.strip()
        except:
            quantity="no quantity limit"

        print("name: " + name)
        print("price_now: " + price_now)
        print("price_bef: " + price_bef)

        print("free shipping: " + free_shipping)
        print("fee: " + fee)
        print("perc: " + perc)

        print("state: " + state)
        print("quantity:" + quantity)
        print("link :" + link)
        print()
        print("-"*10)
        print()
      
        f.write(name.replace(";" , " ")+ " ; "  + price_bef +  " ; " + price_now + " ; "  + perc.strip()+ " ´; "  + fee+ " ; " +free_shipping + " ; " + state+ " ; "  + quantity+ " ; "  + link+"\n")

f.close()

