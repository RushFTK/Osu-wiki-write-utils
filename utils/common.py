from ossapi import Ossapi

# don't fotgot add '' to contain client_id and secret, e.g:None
client_id = None
client_secret = None

def generate_osu_api():
    try:
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
        '*' : '\*'
    }
    for target_char in convert_list.keys():
        target = target.replace(target_char,convert_list[target_char])
    return target