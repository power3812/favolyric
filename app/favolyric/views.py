import json
import urllib.request
import urllib.parse
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.db import connection, transaction
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from rest_framework import permissions
from rest_framework.response import Response
from pymongo import MongoClient
from .models import Views
from . rating import pearson_score, find_similar_users
from redis import Redis

def is_num(s):
    return s.replace(',', '').replace('.', '').replace('-', '').isnumeric()

"""
class Index(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return Response(data={'status': 'aaaa'}, status=status.HTTP_200_OK)

class Result(APIView):
    permission_classes = (permissions.AllowAny)

    def get(self, request, format=None):
        DATABASE_NAME = 'music'
        COLLECTION_NAME = 'lyrics'
        client = MongoClient('mongodb://root:MongoDB2019!@mongo:27017/music')
        #client = MongoClient('mongodb://root:MongoDB2019!@localhost:27017/music')
        db = client[DATABASE_NAME]
        collection = db[COLLECTION_NAME]
        lyric = db[COLLECTION_NAME]
        ratings = list(lyric.find())
        client.close()

        #ratings_file = 'analyze_image_ituens.json'
        #ratings = json.load(open(ratings_file, "r", encoding="utf-8"))

        #データ変換
        dic = {}
        for i in range(len(ratings)):
            dic[ratings[i]['title']] = ratings[i]["emotions"]

        dic['User'] = {'happy': float(request.GET.get('happy')), 'sad': float(request.GET.get('sad')),
            'disgust': float(request.GET.get('disgust')), 'anger': float(request.GET.get('anger')),
            'fear': float(request.GET.get('fear')), 'surprise': float(request.GET.get('surprise'))}
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
                    Views.objects.create(lyric_id = ratings[i]["_id"])
                    break
            res.append(d)
        data = {
            'res':res,
        }
"""
def index(request):
    """
    #ranking = Ranking(Redis(), 'viewranking')
    DATABASE_NAME = 'music'
    COLLECTION_NAME = 'lyrics'
    client = MongoClient('mongodb://root:MongoDB2019!@mongo:27017/music')
    #client = MongoClient('mongodb://root:MongoDB2019!@localhost:27017/music')
    db = client[DATABASE_NAME]
    lyric = db[COLLECTION_NAME]
    ranking = Ranking(Redis(), 'viewranking')
    ranking_ids = ranking.gen_list()
    res = [];
    for id in ranking_ids:
        col = lyric.find({'_id':id})
        res.append(col)
    client.close()
    data = {
        'res':res,
    }
    """

    return render(request, 'favolyric/index2.html' )

def result(request):
    cursor = connection.cursor()
    sql    = 'SELECT * FROM favolyric_lyrics INNER JOIN favolyric_images ON \
    favolyric_lyrics.image_id = favolyric_images.id INNER JOIN \
    favolyric_artists ON favolyric_lyrics.artist_id = favolyric_artists.id;'
    cursor.execute(sql)
    rows = cursor.fetchall()

    dic = {}
    for row in rows:
        dic[row[1]] = {
            "happy":row[5],
            "sad":row[6],
            "disgust":row[7],
            "anger":row[8],
            "fear":row[9],
            "surprise":row[10]
        }

    dic["user"] = {
        "happy": request.GET.get("happy"),
        "sad": request.GET.get("sad"),
        "disgust": request.GET.get("disgust"),
        "anger": request.GET.get("anger"),
        "fear": request.GET.get("fear"),
        "surprise": request.GET.get("surprise"),
    }

    for emotion, user_param in dic["user"].items():
        if user_param is None or not is_num(user_param):
            dic["user"][emotion] = 0.0
        else:
            dic["user"][emotion] = float(user_param)

    user          = "user"
    similar_users = find_similar_users(dic, user, 3)
    res           = []

    for item in similar_users:
        lyric          = {}
        lyric["title"] = item[0]

        for row in rows:
            if  row[1] == item[0]:
                lyric["artist"]     = row[18]
                lyric["music_img"]  = row[14]
                lyric["ituens_img"] = row[4]
                break

        res.append(lyric)

    data = {
        'res':res,
    }

    return render(request, 'favolyric/result.html', data)
