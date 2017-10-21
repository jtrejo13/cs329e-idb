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
# Last-Updated: Sat Oct 21 13:39:33 2017 (-0500)
#           By: yulu
#     Update #: 3
# 


from app import app
from flask import Flask
from flask import render_template

@app.route('/artists')
def artists():
    return render_template("artists.html")

