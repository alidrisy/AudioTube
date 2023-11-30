#!/usr/bin/python3
""" SET the api blueprint """
from flask import Blueprint

app_audio = Blueprint("app_audio", __name__, url_prefix="/api/v1/")

from api.v1.views.stream import *
from api.v1.views.search import *
from api.v1.views.download import *
