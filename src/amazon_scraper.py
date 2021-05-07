from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
#import csv

#DRIVER_PATH=str(Path('geck').resolve())
browser=webdriver.Chrome(executable_path='/home/nazrin/Downloads/chromedriver_linux64/chromedriver')
'''
input_field=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')

tap_button=driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')

input_field.send_keys(item)

submit_btn.send_keys(ENTER)
'''
def get_url(search_item):
    search_item = search_item.replace(' ', '+')
    template = f'https://www.amazon.com/s?k={search_item}&crid=2LVUHRLNH01PN&sprefix=ultrawide%2Caps%2C354&ref=nb_sb_ss_ts-doa-p_1_9'
    template += '&page={}'
    return template
   # browser=webdriver.Firefox(executable_path=DRIVER_PATH)
    
    #browser.get(url)
    #return browser.page_source


def scrape_data(card):
    try:
        h2=card.h2

    except:
        title=''
        url=''

    else:

        title=h2.text.strip()

        url=h2.a.get('href')
    try:
        price=card.find('span',class_='a-price-whole').text.strip('.').strip()

    except:
        price=''

    else:
        price=''.join(price.split(','))

    data={
            'title':title,
            'url':url,
            'price':price,
            'source':'amazon.com'
            }
    return data


def scrape_amazon(search_item):
    ads_data=[]
    url = get_url(search_item)
    for i in range(1,4):
        browser.get(url.format(i))
        #url=f'https://www.amazon.com'
        #html=get_url(url)
        soup=BeautifulSoup(browser.page_source, 'lxml')
        
        cards=soup.find_all('div',{'data-asin':True,'data-component-type':'s-search-result'})
#print(len(cards))

        for card in cards:
            data=scrape_data(card)
            ads_data.append(data)  


    browser.quit()

    return ads_data

if __name__=='__main__':
    scrape_amazon('msi 65')



