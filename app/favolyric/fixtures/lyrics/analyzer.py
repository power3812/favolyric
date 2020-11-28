import glob
import collections as cl
import pprint
from sentimentja import Analyzer
import datetime
import os
import pandas as pd
import numpy as np

dt_now = datetime.datetime.now()

time = dt_now.strftime('%Y_%m_%d')
#dirname  = "ranking/" + time + "/"
dirname  =  "ranking/*/"
filename = "*.txt"
#dirname_result = "result/" + time + "/"
dirname_result  =  "result/*/"
files = glob.glob(dirname + filename)
analyzer = Analyzer()

lyrics_csv       = pd.read_csv("lyrics.csv",  sep=',', encoding='utf-8')
artists_csv      = pd.read_csv("artists.csv",  sep=',', encoding='utf-8')
#emotions_csv     = pd.read_csv("emotions.csv",  sep=',', encoding='utf-8')
images_csv       = pd.read_csv("images.csv",  sep=',', encoding='utf-8')
#itunes_links_csv = pd.read_csv("itunes_links.csv",  sep=',', encoding='utf-8')

for i, file in enumerate(files):
    f = open(file)
    data = f.readlines()
    f.close()
    if len(data) < 6:
        continue
    sentences = data[5:]

    happy    = 0
    sad      = 0
    angry    = 0
    disgust  = 0
    surprise = 0
    fear     = 0
    count    = 0

    for sentence in sentences:
        sentence = sentence.replace("\u3000", " ")
        sentence = sentence.replace("\n", "")
        sentence = [sentence]

        analyzed_sentence = analyzer.analyze(sentence)

        happy    += float(analyzed_sentence[0]["emotions"]["happy"])
        sad      += float(analyzed_sentence[0]["emotions"]["sad"])
        angry    += float(analyzed_sentence[0]["emotions"]["angry"])
        disgust  += float(analyzed_sentence[0]["emotions"]["disgust"])
        surprise += float(analyzed_sentence[0]["emotions"]["surprise"])
        fear     += float(analyzed_sentence[0]["emotions"]["fear"])
        count    += 1

    happy    = happy / count
    sad      = sad / count
    angry    = angry / count
    disgust  = disgust / count
    surprise = surprise / count
    fear     = fear / count

    artist      = data[0].replace("\n","")
    title       = data[1].replace("\n","")
    image       = data[2].replace('\n', '')
    itunes_link = data[3].replace('\n', '')


    artist_exist_flag = False
    for index, row in artists_csv.iterrows():
        if artist == row['name']:
            artist_exist_flag = True
            break

    if not artist_exist_flag:
        artists_csv = artists_csv.append({"id": artists_csv.tail(1).id.iloc[-1] + 1, "name":artist}, ignore_index=True)

    image_exist_flag = False
    for index, row in images_csv.iterrows():
        if image == row['url']:
            image_exist_flag = True
            break

    if not image_exist_flag:
        images_csv = images_csv.append({"id": images_csv.tail(1).id.iloc[-1] + 1, "url":image}, ignore_index=True)

    title_exist_flag = False
    for index, row in lyrics_csv.iterrows():
        if title == row['title']:
            title_exist_flag = True
            break

    if not title_exist_flag:
        artist_id = artists_csv[artists_csv['name'] == artist].id.iloc[-1]
        image_id  = images_csv[images_csv['url'] == image].id.iloc[-1]
        #itunes_link  = itunes_links_csv[itunes_links_csv['url'] == itunes_link].id.iloc[-1]
        #emotion_id = emotions_csv[(emotions_csv['happy'] == happy) & (emotions_csv['sad'] == sad) & (emotions_csv['angry'] == angry) & (emotions_csv['disgust'] == disgust) & (emotions_csv['surprise'] == surprise) & (emotions_csv['fear'] == fear)].id.iloc[-1]
        #print(lyrics_csv.tail(1).id.iloc[-1])
        lyric_json = {
            "id": lyrics_csv.tail(1).id.iloc[-1] + 1,\
            "title":title, \
            "artist_id":artist_id, \
            "image_id":image_id, \
            "itunes_link":itunes_link, \
            "happy":happy, \
            "sad":sad, \
            "angry":angry, \
            "disgust":disgust, \
            "surprise":surprise, \
            "fear":fear, \
        }
        lyrics_csv = lyrics_csv.append(lyric_json, ignore_index=True)

print(artists_csv)
artists_csv.to_csv('artists.csv', index=False)
#emotions_csv["id"] = emotions_csv["id"].astype(int)
#emotions_csv.to_csv('emotions.csv', index=False)
images_csv.to_csv('images.csv', index=False)
#itunes_links_csv.to_csv('itunes_links.csv', index=False)
#lyrics_csv["itunes_link_id"] = lyrics_csv["itunes_link_id"].astype(int)
#lyrics_csv["emotion_id"] = lyrics_csv["emotion_id"].astype(int)
lyrics_csv.to_csv('lyrics.csv', index=False)
#os.mkdir(dirname_result)
#fw = open(dirname_result + 'lyric.json','w')
#json.dump(ys, fw, indent=4, ensure_ascii=False)
