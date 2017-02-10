'''
import urllib.request

x = urllib.request.urlopen('https://www.google.com/')
print(x.read())
'''
'''
import urllib.parse
import urllib.request

url = 'http://pythonprogramming.net'
value = {'s':'basics', 'submit':'search'}

data = urllib.parse.urlencode(value)
data = data.encode("utf-8")

req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)

saveFile = open('page.html','w')
saveFile.write(str(resp.read()))
saveFile.close()
'''
#from wsgiref import headers
#import urllib.parse
import urllib.request

url = 'https://www.google.com/search?q=python'

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebkit/537.17 (KHTML, like, Gecko) Chome/24.0.1312.27 Safari/537.17"

req = urllib.request.Request(url, headers=headers)
data = urllib.request.urlopen(req)

print(data.read())
