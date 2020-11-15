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


    """
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
                Views.objects.create(lyric_id = ratings[i]["_id"])
                break
        res.append(d)
    data = {
        'res':res,
    }
    """

    cursor = connection.cursor()
    sql = 'select * from favolyric_lyrics inner join favolyric_images on favolyric_lyrics.image_id = favolyric_images.id \
    inner join favolyric_artists on favolyric_lyrics.artist_id = favolyric_artists.id;'
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows)

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

    dic["User"] = {'happy': float(request.POST.get('happy')), 'sad': float(request.POST.get('sad')),
        'disgust': float(request.POST.get('disgust')), 'anger': float(request.POST.get('anger')),
        'fear': float(request.POST.get('fear')), 'surprise': float(request.POST.get('surprise'))}
    user = "User"
    similar_users = find_similar_users(dic, user, 3)
    res = []
    for item in similar_users:
        d = {}
        d["title"] = item[0]
        for i in range(len(rows)):
            if  rows[i][1] == item[0]:
                d["artist"] = rows[i][1]
                d["music_img"] = rows[i][14]
                d["ituens_img"] = rows[i][18]
                break
        res.append(d)
    data = {
        'res':res,
    }


    return render(request, 'favolyric/result.html', data)
