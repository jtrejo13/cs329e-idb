from app import app
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Albums, engine
#from app.build_db import create_albums, session

@app.route('/albums')
def albums():
  #albums = session.query(Albums)
  tableTitles = ['NAME', 'NO_OF_TRACKS', 'BAND', 'GENRE', 'YEAR_OF_RELEASE']
  return render_template("albums.html", tableTitles = tableTitles)
  #return render_template("albums.html", tableTitles = tableTitles, albums = albums)
