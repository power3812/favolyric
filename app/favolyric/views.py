from django.shortcuts import render
from . rating import pearson_score, find_similar_users
import json
from pymongo import MongoClient
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
import urllib.request
import urllib.parse


def index(request):
    return render(request, 'favolyric/index2.html')

def result(request):
    DATABASE_NAME = 'music'
    COLLECTION_NAME = 'lyrics'
    client = MongoClient('mongodb://root:MongoDB2019!@mongo:27017/music')
    #client = MongoClient('mongodb://root:MongoDB2019!@localhost:27017/music')
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    music = db[COLLECTION_NAME]
    ratings = list(music.find())
    client.close()

    #ratings_file = 'analyze_image_ituens.json'
    #ratings = json.load(open(ratings_file, "r", encoding="utf-8"))

    #データ変換
    dic = {}
    for i in range(len(ratings)):
        dic[ratings[i]['title']] = ratings[i]["emotions"]

    dic['User'] = {'happy': float(request.POST.get('happy')), 'sad': float(request.POST.get('sad')),
        'disgust': float(request.POST.get('disgust')), 'anger': float(request.POST.get('anger')),
        'fear': float(request.POST.get('fear')), 'surprise': float(request.POST.get('surprise'))}
    user = "User"
    similar_users = find_similar_users(dic, user, 3)
    res = []
    for item in similar_users:
        d = {}
        d["title"] = item[0]
        for i in range(len(ratings)):
            if ratings[i]['title'] == item[0]:
                d["artist"] = ratings[i]["artist"]
                d["music_img"] = ratings[i]["music_img"]
                d["ituens_img"] = ratings[i]["ituens_img"]
                break
        res.append(d)
    data = {
        'res':res,
    }
    return render(request, 'favolyric/result.html', data)
