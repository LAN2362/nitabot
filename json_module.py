import json
import os

#JSON文字列を辞書に変換
def load_json(file_name):
    path = os.path.dirname(__file__) + "/json/" + file_name + ".json"
    if os.path.isfile(path) != True:
        return [False,""]
    with open(path,"r") as file:
        dict = json.load(file)
    return dict

#JSONファイルに保存
def save_json(file_name,dict):
    path = os.path.dirname(__file__) + "/json/" + file_name + ".json"
    if os.path.isfile(path) != True:
        return
    with open(path,"w") as file:
        json.dump(dict, file, indent=4, ensure_ascii=False)
