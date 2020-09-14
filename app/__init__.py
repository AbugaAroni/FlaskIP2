from flask import Flask

# Initializing Application
app = Flask(__name__)

from app import views
