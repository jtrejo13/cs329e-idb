from app import app
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Artists, engine
#from app.build_db import create_artists, session

@app.route('/artists')
def artists():
  #artists = session.query(Artists)
  tableTitles = ['NAME', 'NO_OF_MEMBERS', 'START DATE', 'ORIGIN', 'NO_OF_ALBUMS']
  return render_template("artists.html", tableTitles = tableTitles)
  #return render_template("artists.html", tableTitles = tableTitles, artists = artists)

