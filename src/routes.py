#import sys
#sys.path.insert(0,'~/Desktop/oop/src')
from src import app
from flask import render_template, url_for, flash, redirect
from src.forms import *
from src.amazon_scraper import *
from src.tapaz_scraper import *


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    item = form.item.data
    if item:
        amazon_products =scrape_amazon(item)
        tapaz_products =scrape_tapaz(item)
        
    else:
        amazon_products = {}
        tapaz_products = {}
        
    return render_template('home.html', title='Search', form=form,amazon_products=amazon_products,tapaz_products=tapaz_products)
