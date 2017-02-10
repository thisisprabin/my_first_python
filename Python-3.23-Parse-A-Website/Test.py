import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
value = {'s':'basics', 'submit':'search'}

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebkit/537.17 (KHTML, like, Gecko) Chome/24.0.1312.27 Safari/537.17"

data = urllib.parse.urlencode(value)
data = data.encode('utf-8')

req = urllib.request.Request(url, data, headers=headers)
resp = urllib.request.urlopen(req)

respData = resp.read()

paragraph = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraph:
    print(eachP)