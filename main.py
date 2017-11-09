# main.py --- 
# 
# Filename: run.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Oct 21 12:50:32 2017 (-0500)
# Version: 
# Last-Updated: Fri Oct 27 01:19:34 2017 (-0500)
#           By: yulu
#     Update #: 3
#

from app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# import database models
# import create database

if __name__=='__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
