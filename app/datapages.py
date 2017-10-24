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
from flask import render_template

@app.route('/nineinchnails')
def nineinchnails():
    return render_template("nineinchnails.html")

@app.route('/arushofbloodtothehead')
def arushofbloodtothehead():
    return render_template("arushofbloodtothehead.html")

@app.route('/bananaphone-album')
def bananaphonealbum():
    return render_template("bananaphone-album.html")

@app.route('/bananaphone')
def bananaphone():
    return render_template("bananaphone.html")

@app.route('/coldplay')
def coldplay():
    return render_template("coldplay.html")

@app.route('/countingstars')
def countingstars():
    return render_template("countingstars.html")

@app.route('/godputasmileuponyourface')
def godputasmileuponyourface():
    return render_template("godputasmileuponyourface.html")

@app.route('/headlikeahole')
def headlikeahole():
    return render_template("headlikeahole.html")

@app.route('/native')
def native():
    return render_template("native.html")

@app.route('/onerepublic')
def onerepublic():
    return render_template("onerepublic.html")

@app.route('/prettyhatemachine')
def prettyhatemachine():
    return render_template("prettyhatemachine.html")

@app.route('/raffi')
def raffi():
    return render_template("raffi.html")

