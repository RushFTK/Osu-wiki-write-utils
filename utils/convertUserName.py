from utils.common import generate_osu_api
from utils.common import convert_char
osu_api = generate_osu_api()

class osuWikiUser:
    uid = 0
    uname = ''
    flagcode = ''
    # using username to find player
    def __init__(self,uid:int,uname:str,flagcode:str):
        self.uid = uid
        self.uname = uname
        self.flagcode = flagcode

    def __init__(self,user,is_uid=False):
        if (is_uid):
            self.uid = user
            self.update_info_by_uid(user)
        else:
            self.uname = user
            self.update_info_by_name(user)

    def __repr__(self):
        user_part = self.uname if self.uname != '' else '-'
        link_part = '('+str(self.uid)+')' if self.uid != 0 else '-'
        return user_part + link_part

    def __str__(self):
        flag_part = '::{ flag='+self.flagcode+' }:: ' if self.flagcode != '' else ''
        user_part = '['+self.uname+']' if self.uname != '' else ''
        link_part = '(https://osu.ppy.sh/users/'+str(self.uid)+')' if self.uid != 0 else ''
        return flag_part + user_part + link_part

    def update_info_by_uid(self,uid:int):
        if uid is None and self.uid > 0:
            uid = self.uid
        else:
            self.uid = uid
        if osu_api is None:
            print('Vaild api required for get user info')
            pass
        user = osu_api.user(uid,key='id')
        self.flagcode = user.country_code
        self.uname = convert_char(user.username)

    def update_info_by_name(self,uname:str):
        if uname is None and self.uname != '':
            uname = self.uname
        else:
            self.uname = uname
        user = osu_api.user(uname,key='username')
        self.flagcode = user.country_code
        self.uid = user.id
        self.uname = convert_char(self.uname)