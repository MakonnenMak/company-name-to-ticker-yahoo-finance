'''

Version (1) -- Yahoo  finance doesn't allow for the searching of information using names, only tickers.
The purpose of this algorithm is to convert any company entered into a ticker using selenium web scraping.

Version (2) -- Instead of using selenium to do the scraping, I used the google API. It's a lot faster than the
selenium scraping.

- MakonnenM
'''


from google import search
from yahoo_finance import *

def name_convert(self):

    searchval = 'yahoo finance '+self
    link = []
    #limits to the first link
    for url in search(searchval, tld='es', lang='es', stop=1):
        link.append(url)

    link = str(link[0])
    link=link.split("/")
    if link[-1]=='':
        ticker=link[-2]
    else:
        x=link[-1].split('=')
        ticker=x[-1]

    return(ticker)

#Function uses yahoo finance to return opening ,closing, and percent change. More get_ methods can be tested, available on the yahoo-finance python documentation.
def company_data(self):
    company=Share(self)
    opening_price=company.get_open()
    closing_price=company.get_prev_close()
    percent_change=company.get_percent_change()
    name_from_tick=company.get_name()

    listval=[opening_price,closing_price,percent_change,name_from_tick]
    return listval


#Comment out when testing

company_name=input("Enter a company name: ")
company=name_convert(company_name)
print(company_data(company))



