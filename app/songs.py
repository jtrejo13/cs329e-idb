# songs.py --- 
# 
# Filename: songs.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Oct 21 13:24:45 2017 (-0500)
# Version: 
# Last-Updated: Wed Oct 25 22:13:43 2017 (-0500)
#           By: yulu
#     Update #: 29
# 


from app import app
import codecs,json, os
from flask import Flask, url_for, render_template

@app.route('/songs')
def songs():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/json", "Songs.json")
    with codecs.open(json_url, 'r', 'utf-8-sig') as f:
        data = json.load(f)
    tableTitles = ['NAME', 'DURATION', 'BAND', 'ALBUM', 'GENRE', 'YEAR_OF_RELEASE', 'LYRICS_LINK', 'VIDEO_LINK']
    return render_template("songs.html",
                           tableTitles = tableTitles,
                           data = data)



