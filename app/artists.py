from app import app
from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Artists, engine
from app.build_db import create_artists, session

@app.route('/artists')
def artists():
  artists = session.query(Artists)
  tableTitles = ['name', 'origin', 'genre', 'start_date', 'latest_release']
  return render_template("artists.html", tableTitles = tableTitles, artists = artists)
