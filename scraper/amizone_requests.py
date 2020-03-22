import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Set-Cookie': 'ASPSESSIONIDSWDCBSBQ=GKACLGDCKMDFKAOHNOOOPBOM; secure; path=/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection':'keep-alive',
    'DNT': '1',
    'Host': 'amizone.net',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
}
class myclass:
    def __init
    }

with requests.Session() as s:
    url = 'https://student.amizone.net'
    #url = 'https://httpbin.org/get'
    r1 = s.get(url, headers=headers)
    print(r1.headers)
    with open('amizone.html', 'w') as f:
        f.write(r1.text)
    cookie_raw = r1.headers['Set-Cookie']
    #print(cookie_raw)
    cookie_list = cookie_raw.split("=")
    #print(cookie_list)
    rvt = cookie_list[0]
    rvt_code = cookie_list[1].split(";")[0]
    login_data = {
        '_UserName': '7071804',
        '_Password': 'kalakand',
        rvt:rvt_code
    }
    print(login_data)
    r2 = s.post(url, data=login_data, headers = headers)
    with open('amizone_requests.html', 'w') as f:
        f.write(r2.text)4

    



