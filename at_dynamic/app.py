#!/usr/bin/python3
""" AudioTube main instance """
from flask import Flask, render_template, Response, request
from youtubesearchpython import VideosSearch
from requests import get
from os import getenv
import json
import uuid


app = Flask(__name__)


def search(query):
    """ Search youtube videos """
    yt = VideosSearch(query)
    return yt.result()['result']


@app.route('/download', methods=['POST'], strict_slashes=False)
def download_audio():
    """ Download youtube video/audio """
    url = request.form.get('url')
    filename = request.form.get('filename')
    filename = filename.replace(' ', '_')
    filename = filename.encode('utf-8').decode('unicode-escape')
    response = get(url, stream=True)
    resp = Response(response.raw)
    resp.headers["Content-Disposition"] = f"attachment; filename={filename}"
    if "mp3" in filename:
        resp.headers['Content-Type'] = 'audio/mp3'
    else:
        resp.headers['Content-Type'] = response.headers['Content-Type']
    resp.headers["Content-Length"] = response.headers["Content-Length"]
    resp.headers["Connection"] = response.headers["Connection"]
    return resp


@app.route('/', strict_slashes=False)
def audioTube():
    """ Rendering the main app page """
    video_list = search('اغنية | اغاني | music | song')
    video_list.extend(search('بودكاست | podcast'))
    video_list.extend(search('كتاب| كتب | book | books'))
    for i in range(len(video_list)):
        video_list[i]['cname'] = video_list[i]['channel']['name']
        video_list[i]['cimg'] = video_list[i]['channel']['thumbnails'][-1]['url']
        del video_list[i]['channel']
        video_list[i]['img'] = video_list[i]['thumbnails'][-1]['url']
        del video_list[i]['thumbnails']
        video_list[i]['views'] = video_list[i]['viewCount']['short']
#    video_list.sort(key=lambda k: k['views'])
    video_list = json.dumps(video_list)
    return render_template("AudioTube.html", videos=video_list)


if __name__ == '__main__':
    app.run(host=getenv('AY_HOST', '0.0.0.0'), port=getenv('AY_PORT', 5000))
