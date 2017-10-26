# datapagesAutoGen.py ---
#
# Filename: datapagesAutoGen.py
# Description:
#
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu
#
# Created: Wed Oct 25 23:11:53 2017 (-0500)
# Version:
# Last-Updated: Wed Oct 25 23:15:15 2017 (-0500)
#           By: yulu
#     Update #: 9
#

from app import app
from flask import render_template

@app.route('/database/<name>')
def database(name=None):
    return render_template(name+'.html')
