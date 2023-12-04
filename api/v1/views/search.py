#!/usr/bin/python3
""" Flask Api endpoint for searching """
from api.v1.views import app_audio
from flask import jsonify, make_response
from youtubesearchpython import VideosSearch
import json


def search(query, max_result, type_vid):
    """ Search youtube videos """
    yt = VideosSearch(query, 40)
    video_list = yt.result()['result']
    if len(video_list) < max_result:
        yt.next()
        video_list.extend(yt.result()['result'])
    if len(video_list) < max_result:
        yt.next()
        video_list.extend(yt.result()['result'])
    videos = []
    for i in video_list:
        i['cname'] = i['channel']['name']
        i['cimg'] = i['channel']['thumbnails'][-1]['url']
        del i['channel']
        i['img'] = i['thumbnails'][-1]['url']
        del i['thumbnails']
        i['views'] = i['viewCount']['short']
        if i['viewCount']['short'] and type_vid != 'search':
            videos.append(i)
        elif type_vid == 'search':
            videos.append(i)
    return videos


@app_audio.route('/catagories/<int:catagory_id>/', methods=['GET'],
                 strict_slashes=False)
def catagories(catagory_id=None):
    """ Get content from youtube """
    podcast = 'بودكاست | podcast'
    books = 'كتاب | كتب | book | books'
    songs = "أغنية | أغاني | music | song"
    if catagory_id == 10:
        vidList = search(songs, 50, 'tag')
    elif catagory_id == 27:
        vidList = search(books, 50, 'tag')
    elif catagory_id == 24:
        vidList = search(podcast, 50, 'tag')

    return jsonify(vidList)


@app_audio.route('/search/<quary>/', methods=['GET'], strict_slashes=False)
def searchVid(quary):
    """ Search videos by key words """
    search_list = search(quary, 50, 'search')
    return jsonify(search_list)
