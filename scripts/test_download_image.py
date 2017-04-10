url= "http://45.56.104.240"
req = urllib2.Request(url)
req.add_header('Authorization', 'OAuth2 a0028f740988d80cbe670f24a9456d655b8dd419')
resp = urllib2.urlopen(req)
content = resp.read()
data = json.loads(content)
result = data