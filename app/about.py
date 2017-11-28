# about.py

from app import app
from flask import render_template
import subprocess
from unittest import TextTestRunner, makeSuite
import tests as testClass
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO


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
