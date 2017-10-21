# index.py --- 
# 
# Filename: index.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Oct 21 12:52:27 2017 (-0500)
# Version: 
# Last-Updated: Sat Oct 21 12:55:16 2017 (-0500)
#           By: yulu
#     Update #: 1
# 

from app import app
from flask import Flask
from flask import render_template

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

