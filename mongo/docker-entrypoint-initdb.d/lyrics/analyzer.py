import glob
import json
import collections as cl
import pprint
from sentimentja import Analyzer
import datetime
import os

dt_now = datetime.datetime.now()

time = dt_now.strftime('%Y_%m_%d')

dirname  = "ranking/" + time + "/"
filename = "*.txt"
dirname_result = "result/" + time + "/"
files = glob.glob(dirname + filename)
analyzer = Analyzer()
ys=[]

for i, file in enumerate(files):
    f = open(file)
    data = f.readlines()
    f.close()
    if len(data) < 6:
        continue
    sentences = data[5].split("\u3000")
    #sentences = sentences.split("\u3000")
    analyzed_sentences = analyzer.analyze(sentences)
    happy    = 0
    sad      = 0
    angry    = 0
    disgust  = 0
    surprise = 0
    fear     = 0
    count    = 0
    for analyzed_sentence in analyzed_sentences:
        happy    += float(analyzed_sentence["emotions"]["happy"])
        sad      += float(analyzed_sentence["emotions"]["sad"])
        angry    += float(analyzed_sentence["emotions"]["angry"])
        disgust  += float(analyzed_sentence["emotions"]["disgust"])
        surprise += float(analyzed_sentence["emotions"]["surprise"])
        fear     += float(analyzed_sentence["emotions"]["fear"])
        count    += 1
    happy    = happy / count
    sad      = sad / count
    angry    = angry / count
    disgust  = disgust / count
    surprise = surprise / count
    fear     = fear / count

    artist = data[0].replace("\n","")
    title  = data[1].replace("\n","")
    print(title)

    json_data               = {}
    json_data["title"]      = title
    json_data["artist"]     = artist
    json_data["img"]        = data[2].replace('\n', '')
    json_data["music_img"]  = data[2].replace('\n', '')
    json_data["ituens_img"] = data[3].replace('\n', '')
    json_data["emotions"] = {"happy" : happy, "sad" : sad, "angry" : angry, "disgust" : disgust, "surprise" : surprise, "fear" : fear}
    ys.append(json_data)

    print(happy)
os.mkdir(dirname_result)
fw = open(dirname_result + 'lyric.json','w')
json.dump(ys, fw, indent=4, ensure_ascii=False)
