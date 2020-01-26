from django.shortcuts import render
from . rating import pearson_score, find_similar_users
import json
from pymongo import Connection

def input(request):
    return render(request, 'input.html')

def response(request):
    databaseName = "mydb"
    connection = Connection()
    db = connection[databaseName]
    music = db['music']
    data=list(music.find())
    #ratings_file = 'analyze_image_ituens.json'
    #data = json.load(open(ratings_file, "r", encoding="utf-8"))

    #データ変換
    dic = {}
    for i in range(len(data)):
        dic[data[i]['title']] = data[i]["emotions"]

    dic['User'] = {'happy': float(request.GET.get('happy')), 'sad': float(request.GET.get('sad')),
     'disgust': float(request.GET.get('disgust')), 'anger': float(request.GET.get('anger')),
     'fear': float(request.GET.get('fear')), 'surprise': float(request.GET.get('surprise'))}
    user = "User"
    similar_users = find_similar_users(dic, user, 3)
    res = []
    for item in similar_users:
        d = {}
        d["title"] = item[0]
        for i in range(len(data)):
            if data[i]['title'] == item[0]:
                d["artist"] = data[i]["artist"]
                d["music_img"] = data[i]["music_img"]
                d["ituens_img"] = data[i]["ituens_img"]
                break
        res.append(d)
    params = {
        'res':res,
    }
    return render(request, 'response.html', params)
