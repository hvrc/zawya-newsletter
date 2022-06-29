from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["CACHE_TYPE"] = "null"

from . import home
