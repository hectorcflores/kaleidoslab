from app import app
from flask import Flask, render_template

from kaleidos import *

@app.route('/')
def home():
	films_data= films
	return render_template('index.html', films_table=films_data)

