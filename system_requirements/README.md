# 概要
感情で楽曲推薦WEBアプリケーション <br>
sentimentjaという日本語テキストの感情を6種類(happy, sad, angry, disgust, surprise, fear)に分類するためのモデルが存在する。<br>
これを使って楽曲の歌詞を解析して、ユーザーに感情を入力してもらってピアソンの積率相関係数を求めれば新しい楽曲推薦システムができるのではという発想
<br>
バズるかどうかわからないので、技術力向上が多分メインテーマ <br>
もし、音楽配信サービスに売りこめたら最高 <br>

# 使用技術(暫定)
- バックエンド
    - Python
    - Django
    - MySQL
    - Redis
- フロントエンド
    - React or Vue
- インフラ
    - Docker
    - Nginx

# テーブル定義
[テーブル定義(暫定)](./db_schema) <br>

# システム構成図
todo

# 機能要件
- 楽曲推薦ロジック(完成)
    - ユーザーの感情の入力値にと楽曲の感情の値のピアソンの相関係数を求めることで上位3つを推薦
- 歌詞スクレイピング(完成)
    - [歌ネット](https://www.uta-net.com)からデイリーランキングを毎日スクレイピングしている
- 歌詞を感情分析(完成)
    - sentimentjモデルを使用して、感情解析をしてcsvで出力
- 検索ヒット数ランキング
    - 毎日10時に前日に検索でヒットした数で楽曲のランキングを表示
- ソーシャルログイン
- ユーザーごとの検索履歴
- ユーザーの検索傾向から違う楽曲を推薦
    - 音楽推薦ロジックを改変すればいけそう?
- SPAでUXを上げたい
- and more...
