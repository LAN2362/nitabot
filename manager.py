from json_module import load_json, save_json


def manage_token():
    dict = load_json("token&server_id")
    token = dict["token"]
    if len(token) == 0:
        token = input("Discord Botのトークンを入力してください: ")
        print("トークンを再設定したい場合は「token&server_id.json」のtokenの値を「""」にしてから再びこのプログラムを実行してください")
        dict["token"] = token
        save_json("token&server_id", dict)
    return token

def manage_serverid():
    dict = load_json("token&server_id")
    server_id = dict["server_id"]
    if len(server_id) == 0:
        server_id = input("サーバーIDを入力してください: ")
        print("サーバーIDを再設定したい場合は「token&server_id.json」のserver_idの値を「""」にしてから再びこのプログラムを実行してください")
        dict["server_id"] = server_id
        save_json("token&server_id", dict)
    return server_id

def manage_adminid():
    dict = load_json("token&server_id")
    admin_id = dict["admin_id"]
    if len(admin_id) == 0:
        admin_id = input("管理者のユーザーIDを入力してください: ")
        print("ユーザーIDを再設定したい場合は「token&server_id.json」のadmin_idの値を「""」にしてから再びこのプログラムを実行してください")
        dict["admin_id"] = admin_id
        save_json("token&server_id", dict)
    return admin_id

def manage_key():
    dict = load_json("token&server_id")
    key = dict["key"]
    if len(key) == 0:
        key = input("json秘密鍵のファイル名を入力してください: ")
        print("json秘密鍵のファイル名を再設定したい場合は「token&server_id.json」のkeyの値を「""」にしてから再びこのプログラムを実行してください")
        dict["key"] = key
        save_json("token&server_id", dict)
    return key

def manage_sheetid():
    dict = load_json("token&server_id")
    sheetid = dict["sheetid"]
    if len(sheetid) == 0:
        sheetid = input("sheetid: ")
        print("sheetidを再設定したい場合は「token&server_id.json」のkeyの値を「""」にしてから再びこのプログラムを実行してください")
        dict["sheetid"] = sheetid
        save_json("token&server_id", dict)
    return sheetid
