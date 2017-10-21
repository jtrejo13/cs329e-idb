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
# Last-Updated: Sat Oct 21 13:26:41 2017 (-0500)
#           By: yulu
#     Update #: 2
# 

from app import app
from flask import Flask
from flask import render_template

@app.route('/albums')
def albums():
    return render_template("albums.html")
