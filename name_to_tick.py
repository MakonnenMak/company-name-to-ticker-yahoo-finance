'''

Version (1) -- Yahoo  finance doesn't allow for the searching of information using names, only tickers.
The purpose of this algorithm is to convert any company entered into a ticker using selenium web scraping.

- MakonnenM
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from yahoo_finance import *

def name_to_tick(self):
    #Using firefox/webdriver to search up google

    #Insert location of geckodriver. The default code I have entered pertains only to my location.
    browser=webdriver.Firefox(executable_path='C:\Program Files (x86)\Gec\geckodriver.exe')
    browser.get('http://www.google.com')
    companyname=(self)

    #Mouse 'clicks' into the google search parameters
    search = browser.find_element_by_name('q')
    #Enters this information
    search.send_keys("yahoo finance "+companyname)
    search.send_keys(Keys.ENTER)
    browser.implicitly_wait(2)

    #First link that is a yahoo finance link is clicked
    link=browser.find_element_by_xpath('//a[starts-with(@href,"https://finance.yahoo")]').get_attribute('href')
    #Gets ticker from the URL (.get_attribute('href'))
    link=link.split("/")
    if link[-1]=='':
        ticker=link[-2]
    else:
        x=link[-1].split('=')
        ticker=x[-1]

    return(ticker)

#Function uses yahoo finance to return opening ,closing, and percent change.
def company_data(self):
    company=Share(self)
    opening_price=company.get_open()
    closing_price=company.get_prev_close()
    percent_change=company.get_percent_change()

    return opening_price,closing_price, percent_change

company_name=input("Enter a company name: ")
company=name_to_tick(company_name)
print(company_data(company))


