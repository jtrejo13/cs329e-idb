# artists.py --- 
# 
# Filename: artists.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Oct 21 13:11:53 2017 (-0500)
# Version: 
# Last-Updated: Sun Oct 22 16:12:13 2017 (-0500)
#           By: yulu
#     Update #: 7
# 


from app import app
import codecs, json, os
from flask import Flask
from flask import render_template

@app.route('/artists')
def artists():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/json", "Bands.json")
    with codecs.open(json_url, 'r', 'utf-8-sig') as f:
        data = json.load(f)
    tableTitles = ['NAME', 'NO_OF_TRACKS', 'START DATE', 'ORIGIN', 'NO_OF_ALBUMS']
    return render_template("artists.html",
                           tableTitles = tableTitles,
                           data = data)

