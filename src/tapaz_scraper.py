from pathlib import Path
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

#DRIVER_PATH=str(Path('geck').resolve())
browser=webdriver.Chrome(executable_path='/home/nazrin/Downloads/chromedriver_linux64/chromedriver')
'''
input_field=browser.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')

tap_button=browser.find_element_by_xpath('//*[@id="nav-search-submit-button"]')

input_field.send_keys(item)

submit_btn.send_keys(ENTER)
'''

def get_url(search_item):
    search_item = search_item.replace(' ', '+')
    template = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={search_item}&q%5Bregion_id%5D='
    
    return template


   # browser=webdriver.Firefox(executable_path=DRIVER_PATH)


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
            'rating':rating,
            'url':url,
            'price':price,
            'source':'tap.az'
            }
    return data


def scrape_tap_az(search_item):
    ads_data=[]
    url = get_url(search_item)

    #for i in range(1,4):
    browser.get(url)
    
    #url=f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords=msi gf 65&q%5Bregion_id%5D='

    #html=get_html(url)

    soup=BeautifulSoup(browser.page_source,'lxml')

    #cards=soup.find_all('div',{'data-asin':True,'data-component-type':'s-search-result'})
    cards=soup.find_all('div[class^=categories-products-title]')

    #print(len(cards))

    for card in cards:
        data=scrape_data(card)
        ads_data.append(data)

    browser.quit()
    return ads_data

if __name__=='__main__':
    scrape_tap_az('msi 65')




