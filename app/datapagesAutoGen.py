from app import app
from flask import render_template

@app.route('/database/<name>')
def database(name=None):
    return render_template(name+'.html')
