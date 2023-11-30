#!/usr/bin/python3
""" API to download Video/audio """
from api.v1.views import app_audio
from requests import get
from flask import Response, jsonify, abort, request


@app_audio.route('/download/', methods=['POST'], strict_slashes=False)
def download_audio():
    """ function to download audio """
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    url = data['url']
    response = get(url, stream=True)
    resp = Response(response.raw)
    resp.headers["Content-Disposition"] = "attachment; filename={}.mp3"\
        .format(data['title'].replace(' ', '_'))
    resp.headers['Content-Type'] = response.headers['Content-Type']
    resp.headers["Content-Length"] = response.headers["Content-Length"]
    resp.headers["Connection"] = response.headers["Connection"]
    return resp
