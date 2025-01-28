import os
from ossapi import Ossapi
from dotenv import load_dotenv, dotenv_values

def generate_osu_api():
    try:
        load_dotenv()
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        api_obj = Ossapi(client_id, client_secret)
    except AttributeError:
        print('please fill client_id / secret in utils/common.py before using\n'
            + 'You can find on osu!web settings (https://osu.ppy.sh/home/account/edit)')
        api_obj = None
    return api_obj

def convert_char(target:str):
    convert_list = {
        '[' : '\[',
        ']' : '\]',
        '*' : '\*',
        '_' : '\_',
        '~' : '\~'
    }
    for target_char in convert_list.keys():
        target = target.replace(target_char,convert_list[target_char])
    return target