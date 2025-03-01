import requests

payload = []
f = open('payload.txt', 'r')
for line in f:
    payload.append(line.strip())

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
    "Cookie": "security=high; PHPSESSID=b171pc6qicumo686s83fqfe6t5"
}


class spider():
    def __init__(self):
        self._url = ""

    def run(self, url):
        urls = urlsplit(url)
        if urls is None:
            return False
        print("\r[+] XSS Scaning......")
        for _urlp in urls:
            for _payload in payload:
                _url = _urlp.replace("payload", _payload)
                # urlt = url
                # self._url = _url
                r = requests.get(_url, headers=headers, timeout=5)
                # 如果无法正常访问返回空
                if r.status_code != 200:
                    break
                res = r.text
                if res is None:
                    return False
                # 如果页面返回内容中有payload则发现XSS
                if (res.find(_payload) != -1):
                    print("[*] XSS Found: ", _url)

        return False


# 将url拆分，并将后面参数与payload单独替换，之后查看页面反应
def urlsplit(url):
    domain = url.split("?")[0]
    # print(domain)
    _url = url.split("?")[-1]
    # print(_url)
    param = {}
    for val in _url.split("&"):
        param[val.split('=')[0]] = val.split('=')[-1]
    urls = []
    for val in param.values():
        new_url = domain + '?' + _url.replace(val, 'payload')
        urls.append(new_url)
    return urls


def main():
    url = 'http://127.0.0.1/i/DVWA-master/vulnerabilities/xss_r/?name=123&pwd=456'
    #url = input("请输入url: ")
    spi = spider()
    spi.run(url)


if __name__ == '__main__':
    main()

