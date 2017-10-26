from app import app
import codecs,json, os
from flask import Flask, url_for, render_template

@app.route('/database/<name>')
def database(name=None):
    return render_template(name+'.html')
