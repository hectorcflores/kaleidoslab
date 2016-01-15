from flask import Flask

app = Flask(__name__)

app.secret_key = "dfcurazaoestocolmo1919"

from app import routes