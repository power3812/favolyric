import sys
import os
import glob
import pprint
import datetime
import pandas as pd
import numpy as np
import json

def main():
    args = sys.argv
    if len(args) != 3:
        print("引数は2です。(csvファイル名とjson名)")
        exit(1)

    csv_file = pd.read_csv(args[1],  sep=',', encoding='utf-8')
    table_name = args[1].split("/")[1].split(".")[0]
    column_names = []
    csv_jsons    = []

    for name in csv_file.columns:
        column_names.append(name)

    fields={}
    for item in csv_file.itertuples(name=None):
        fields = {}
        for i, column_name in enumerate(column_names):
            fields[column_name] = item[i+1]
        if fields["id"] == 0:
            continue
        csv_json = {
            "model":"favolyric." + table_name,
            "pk":fields["id"],
            "fields":fields
        }
        csv_jsons.append(csv_json)

    print(csv_jsons)

    json_file = open(args[2], 'w')
    json.dump(csv_jsons, json_file, indent=4, ensure_ascii=False)


    """
    json_file = open(args[2], 'w')
    dt_now = datetime.datetime.now()
    time = dt_now.strftime('%Y_%m_%d')
    #dirname  = "ranking/" + time + "/"
    dirname  =  "ranking/2020_11_01/"
    filename = "*.txt"
    #dirname_result = "result/" + time + "/"
    dirname_result  =  "result/2020_11_01/"
    files = glob.glob(dirname + filename)
    #os.mkdir(dirname_result)
    #fw = open(dirname_result + 'lyric.json','w')
    #json.dump(ys, fw, indent=4, ensure_ascii=False)
    """


if __name__ == '__main__':
    main()
