# albums.py --- 
# 
# Filename: albums.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Oct 21 13:24:15 2017 (-0500)
# Version: 
# Last-Updated: Sun Oct 22 16:21:19 2017 (-0500)
#           By: yulu
#     Update #: 6
# 


from app import app
import codecs, json, os
from flask import Flask
from flask import render_template

@app.route('/albums')
def albums():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/json", "Albums.json")
    with codecs.open(json_url, 'r', 'utf-8-sig') as f:
        data = json.load(f)
    tableTitles = ['NAME', 'NO_OF_TRACKS', 'BAND', 'GENRE', 'YEAR_OF_RELEASE']
    return render_template("albums.html",
                           tableTitles = tableTitles,
                           data = data)

    
    return render_template("albums.html")
