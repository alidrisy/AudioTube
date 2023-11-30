#!/usr/bin/python3
""" Flask Api endpoint for searching """
from api.v1.views import app_audio
from flask import jsonify, make_response
from youtubesearchpython import VideosSearch
import json


def search(query, max_result):
    """ Search youtube videos """
    yt = VideosSearch(query, 40)
    video_list = yt.result()['result']
    if len(video_list) < max_result:
        yt.next()
        video_list.extend(yt.result()['result'])
    if len(video_list) < max_result:
        yt.next()
        video_list.extend(yt.result()['result'])
    for i in range(len(video_list)):
        video_list[i]['cname'] = video_list[i]['channel']['name']
        video_list[i]['cimg'] = video_list[i]['channel']['thumbnails'][-1]['url']
        del video_list[i]['channel']
        video_list[i]['img'] = video_list[i]['thumbnails'][-1]['url']
        del video_list[i]['thumbnails']
        video_list[i]['views'] = video_list[i]['viewCount']['short']
    return video_list


@app_audio.route('/catagories/<int:catagory_id>/', methods=['GET'],
                 strict_slashes=False)
def catagories(catagory_id=None):
    """ Get content from youtube """
    podcast = 'بودكاست | podcast'
    books = 'كتاب | كتب | book | books'
    songs = "أغنية | أغاني | music | song"
    if catagory_id == 10:
        vidList = search(songs, 50)
    elif catagory_id == 27:
        vidList = search(books, 50)
    elif catagory_id == 24:
        vidList = search(podcast, 50)

    return jsonify(vidList)


@app_audio.route('/search/<quary>/', methods=['GET'], strict_slashes=False)
def searchVid(quary):
    """ Search videos by key words """
    search_list = search(quary, 50)
    return jsonify(search_list)
