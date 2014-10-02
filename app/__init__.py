
from sqlite3 import dbapi2 as sqlite3
import urllib
import mechanize
import csv
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


url = "http://finviz.com/export.ashx?v=171&f=sh_avgvol_o1000,sh_relvol_o2"
url2 = "http://finviz.com/export.ashx?v=141&f=sh_avgvol_o2000"


@app.route('/', methods=['GET'])
def get_finviz_data():
    yolo = "Finviz Charting Platform"
    stockdata = urllib.urlopen(url).readlines()
    return render_template('csv.html', collums=stockdata,yolo=yolo,tickerlist=get_series_data(stockdata),pricelist=get_series_value(stockdata),secondSeries="Finviz Chart",selectedTab="Fundamentals" )

@app.route('/technicals', methods = ['GET'])
def return_technicals_data():
    stockdata = urllib.urlopen(url2).readlines()
    yolo = "Finviz Charting Platform"
    return render_template('csv.html', collums=stockdata,yolo=yolo,tickerlist=get_series_data(stockdata),pricelist=get_series_value(stockdata),secondSeries="Finviz Chart",selectedTab="Technicals" )

def get_series_data(stockdata):
    tlist = []
    for r in stockdata[1:20]:
        tlist.append(r.split(",")[1])   
    return tlist

def get_series_value(stockdata):
    zlist = []
    for r in stockdata[1:20]:   
        try:
            zlist.append(float(r.split(",")[3].replace("%",""))) 
        except:
            print ""
    return zlist

if __name__ == '__main__':
    app.run()

# db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404

# Later on you'll import the other blueprints the same way:
#from app.comments.views import mod as commentsModule
#from app.posts.views import mod as postsModule
#app.register_blueprint(commentsModule)
#app.register_blueprint(postsModule)

