#!/usr/bin/python3
""" AudioTube main instance """
from flask import Flask, render_template, Response, request, make_response
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
    # covert filename to valid latin-1
    filename = filename.encode('utf-8').decode('unicode-escape')
    # fetch audio or video as stream without downloud it
    response = get(url, stream=True)
    # return a fetched data as raw or chunks
    resp = Response(response.iter_content(chunk_size=1024))
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
    # git user id cookie to insure if the user use the app for the fris time
    user_id = request.cookies.get('userId')
    # if there is no user id cookie (the user use the app for the first time)
    # set a user id cookie and render the home page 
    if not user_id:
        response = make_response(render_template('main.html'))
        response.set_cookie('userId', str(uuid.uuid4()))
        return response
    # if the user did not use it for the first time render the AudioTube page
    video_list = search('اغنية | اغاني | music')
    video_list.extend(search('بودكاست | podcast'))
    video_list.extend(search('كتاب| كتب | book | books'))
    videos = []
    # reduce the data length (take the needed  data)
    for i in video_list:
        i['cname'] = i['channel']['name']
        i['cimg'] = i['channel']['thumbnails'][-1]['url']
        del i['channel']
        i['img'] = i['thumbnails'][-1]['url']
        del i['thumbnails']
        i['views'] = i['viewCount']['short']
        if i['viewCount']['short']:
            videos.append(i)
    videos.sort(key=lambda k: k['views'])
    videos = json.dumps(videos)
    return render_template("AudioTube.html", videos=videos, cache_id=str(uuid.uuid4()))


@app.route('/home')
def home():
    """ Landing page (the home page) """
    return render_template("main.html")


if __name__ == '__main__':
    app.run(host=getenv('AY_HOST', '0.0.0.0'), port=getenv('AY_PORT', 5000), debug=True)
