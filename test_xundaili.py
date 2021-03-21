from util.webRequest import WebRequest
import json

url = '''
    http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=3f349be46a674a9c9e5c9691a3625947&returnType=2&count=1
    '''
r = WebRequest().get(url, timeout=10)
print(r.text)
result = json.loads(r.text)
ips = result["RESULT"]
for ip in ips:
    proxy = "{}:{}".format(ip["ip"], ip["port"])