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
# Last-Updated: Sun Oct 22 14:14:03 2017 (-0500)
#           By: yulu
#     Update #: 26
# 


#from app import app
import codecs,json
import os
from flask import Flask, url_for
from flask import render_template

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
print(SITE_ROOT)
jsonFile = "Songs.json"
with codecs.open(url_for('static', filename = jsonFile), 'r', 'utf-8-sig') as f:
    data = json.load(f)
    print(data)
    tableTitles = data.keys()
    



