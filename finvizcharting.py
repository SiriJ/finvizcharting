# -*- coding: utf-8 -*-

from sqlite3 import dbapi2 as sqlite3
import urllib
import mechanize
import csv
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


url = "http://finviz.com/export.ashx?v=111&f=earningsdate_nextdays5"
stockdata = urllib.urlopen(url).readlines()

@app.route('/finviz', methods=['GET'])
def get_finviz_data():
    yolo = "Finviz Charting Platform"
    return render_template('csv.html', collums=stockdata,yolo=yolo,tickerlist=get_series_data(),pricelist=get_series_value(),secondSeries="Finviz Chart" )

def get_series_data():
    tlist = []
    for r in stockdata[1:]:
        tlist.append(r.split(",")[1])   
    return tlist

def get_series_value():
    zlist = []
    for r in stockdata[1:]:   
        try:
            zlist.append(float(r.split(",")[8])) 
        except:
            print ""
    return zlist

if __name__ == '__main__':
    app.run()
