import json
from urllib.request import urlopen
url = "https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"

#gooleapis v2 has been deprecated.  figure out how to get his working with v3

response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])

#This example no longer works - see note in page 4 of third edition of book


