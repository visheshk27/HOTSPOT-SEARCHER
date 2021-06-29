from bs4 import BeautifulSoup
import requests
import json
name = raw_input("enter the place")
f_name = name.lower()
def destination(f_name):
    try:

        url = "http://tourism.rajasthan.gov.in/"

        url_final = url + f_name+'.html'
        r = requests.get(url_final)
        soup = BeautifulSoup(r.text , "lxml")
        l_destination = []
        for s in soup.find_all('div', {'class': 'articleCont'}):
            # print s.h4.text
            # print s.p.text

            l_destination.append(s.h4.text +s.p.text)
        print l_destination


    except:
            return "Enter city name"



def hotel(f_name):

    try:

        url = "https://www.holidify.com/places/"+f_name+"/hotels-where-to-stay.html"

        url_final = url
        r = requests.get(url_final)
        soup = BeautifulSoup(r.text , "lxml")
        l_hotel = []
        for s in soup.find_all('div', {'class': ' col-md-6 col-xs-7 nopadding'}):
            # print s.h4.text
            # print s.p.text
            l_hotel.append(s.h4.text)
        print l_hotel
    except:
            return "Enter city name"
destination(f_name)
hotel(f_name)
