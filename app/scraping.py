import os
import re
import bs4
import time
import requests
import pprint
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from time import sleep
import sys

import numpy as np

def load(url):
    res = requests.get(url)
    res.raise_for_status()

    return res.text

def pickup_tag(html, find_tag):
    soup = bs4.BeautifulSoup(str(html), 'html.parser')
    paragraphs = soup.find_all(find_tag)

    return paragraphs

def parse(html):
    soup = bs4.BeautifulSoup(str(html), 'html.parser')

    kashi_row = soup.getText()
    kashi_row = kashi_row.replace('\n', '')
    #kashi_row = kashi_row.replace('　', '')

    # 英数字の排除
    kashi_row = re.sub(r'[a-zA-Z0-9]', '', kashi_row)
    # 記号の排除
    kashi_row = re.sub(r'[ ＜＞♪`‘’“”・…_！？!-/:-@[-`{-~]', '', kashi_row)
    # 注意書きの排除
    kashi = re.sub(r'注意：.+', '', kashi_row)

    return kashi

def scraping_web_page(url):
    sleep(5)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    return soup



def main():
    url = 'https://www.uta-net.com/artist/11591/'

    # 曲ページの先頭アドレス
    base_url = 'https://www.uta-net.com'

    # ページの取得
    html = load(url)

    # 曲ごとのurlを格納
    musics_url = []
    # 歌詞を格納
    kashis = ''

    """ 曲のurlを取得 """
    # td要素の取り出し
    for td in pickup_tag(html, 'td'):
        # a要素の取り出し
        for a in pickup_tag(td, 'a'):
            # href属性にsongを含むか
            if 'song' in a.get('href'):
                # urlを配列に追加
                musics_url.append(base_url + a.get('href'))
    soup = scraping_web_page(url)
    contents = []
    contents.append(soup.find_all(href=re.compile('/song/\d+/$')))
    contents.append(soup.find_all(href=re.compile('/song/\d+/$')))
    contents.append(soup.find_all(class_=re.compile('td2')))
    contents.append(soup.find_all(class_=re.compile('td3')))
    contents.append(soup.find_all(class_=re.compile('td4')))
    infomations = []
    for i, content in enumerate(contents):
        tmp_list = []
        for element in content:
            if i == 0:
                tmp_list.append(element.get('href'))
            else:
                tmp_list.append(element.string)
        infomations.append(tmp_list)
    #DataFrameにする
    artist_df = pd.DataFrame({
        'URL' : infomations[0],
        'SongName' : infomations[1],
        'Artist' : infomations[2],
        'Lyricist' : infomations[3],
        'Composer' : infomations[4]})
    #URLにホストネームを付加
    artist_df.URL = artist_df.URL.apply(lambda x : 'https://www.uta-net.com' + x)

    #print(infomations)



    """ 歌詞の取得 """
    for i, page in enumerate(musics_url):
        print('{}曲目:{}'.format(i + 1, page))
        html = load(page)
        infomations[1][i]=infomations[1][i].replace('/','_')
        f=open(infomations[2][i]+"*"+infomations[1][i]+'.txt', 'a')
        soup = BeautifulSoup(html,'lxml')
        #amazonの画像リンクを取得
        imgs = soup.find_all('img',src=re.compile('^https://images-fe.ssl-images-amazon.com/'))

        #print(soup)
        print(len(imgs))
        if len(imgs) == 0:
            imgs = soup.find_all('img',src=re.compile('^libs/cacheimg.'))
            #print(soup)
            kashis+='*\n'
        else:
            for img in imgs:
                print(img['src'])
                kashis+=img['src']+'\n'
        #itunesリンクを取得
        itunes = None
        for link in soup.findAll("a"):
            if "https://itunes.apple.com/" in link.get("href"): 
                itunes = link.get("href")


        if itunes == None:
            kashis += '*' + '\n'
        else:
            kashis += itunes + '\n'

        for div in pickup_tag(html, 'div'):
            # id検索がうまく行えなかった為、一度strにキャスト
            div = str(div)
            # 歌詞が格納されているdiv要素か
            if r'itemprop="text"' in div:
                # 不要なデータを取り除く
                #print(html)
                kashi = parse(div)
                #print(kashi, end = '\n\n')
                # 歌詞を１つにまとめる
                #print(kashi)
                k=str(i+1)
                #kashis += k+ '曲目:' + str(page)
                kashis += kashi

                # １秒待機
                time.sleep(1)
                f.write(kashis)
                kashis = ''
                break
    # 歌詞の書き込み
        f.write(kashis)
        f.close()

if __name__ == '__main__':
    main()
