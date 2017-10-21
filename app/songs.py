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
# Last-Updated: Sat Oct 21 13:39:33 2017 (-0500)
#           By: yulu
#     Update #: 4
# 


from app import app
from flask import Flask
from flask import render_template

@app.route('/songs')
def songs():
    return render_template("songs.html")


