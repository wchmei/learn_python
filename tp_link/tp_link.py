# encoding=utf-8
# author:walker
# date:2015-08-05
# summary:通过断开连接时TP-LINK重新拨号，以切换IP。此代码经过python3.4测试(适用于TL-WR847N)。

import base64, requests, traceback


def ChangeIP():
    ip = '192.168.42.1'
    user = 'gsafetydata'
    pwd = 'gsafetydata'

    desturl = 'http://' + ip + '/userRpm/StatusRpm.htm?Disconnect=%B6%CF%20%CF%DF&wan=1'
    auth = 'Basic ' + base64.b64encode((user + ':' + pwd).encode(encoding='utf-8')).decode(encoding='utf-8')
    heads = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Referer': 'http://' + ip + '/userRpm/StatusRpm.htm',
        # 'Authorization' : auth
        'Cookie': 'Authorization=' + auth
    }

    try:
        r = requests.get(url=desturl, headers=heads)
        print(r)
    except:
        exMsg = '* exMsg:\n' + traceback.print_exc()
        print(exMsg)


if __name__ == "__main__":
    ChangeIP()