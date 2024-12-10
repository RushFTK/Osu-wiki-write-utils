from ossapi import Ossapi

# don't fotgot add '' to contain client_id and secret, e.g:None
client_id = None
client_secret = None

def generate_osu_api():
    try:
        Ossapi(client_id, client_secret)
    except AttributeError:
        print('please fill client_id / secret in utils/common.py before using\n'
            + 'You can find on osu!web settings (https://osu.ppy.sh/home/account/edit)')
    return None