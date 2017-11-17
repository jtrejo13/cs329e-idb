# about.py --- 
# 
# Filename: about.py
# Description: 
# 
# Author:    Yu Lu
# Email:     yulu@utexas.edu
# Github:    https://github.com/SuperYuLu 
# 
# Created: Sat Oct 21 13:31:38 2017 (-0500)
# Version: 
# Last-Updated: Sat Oct 21 13:32:07 2017 (-0500)
#           By: yulu
#     Update #: 2
# 

from app import app
from flask import render_template
import subprocess
from unittest import TextTestRunner, makeSuite
from io import StringIO
import tests as testClass



@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/tests')
def tests():
	stream = StringIO()
	runner = TextTestRunner(stream=stream, verbosity=2)
	suite = makeSuite(testClass.TestIDB)
	result = runner.run(suite)
	output = stream.getvalue()
	return render_template("tests.html", output=output)


