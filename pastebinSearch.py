import requests, urllib2
import m3uFileChecker
import json

def downloadFromPastebin(id):
    try:
        r = requests.get('https://pastebin.com/raw/{0}'.format(id))
        if r.status_code == 200:
            if(len(r.content) > 100):
                startIndex = r.content[0:100].lower().find('#extm3u')
            else:
                startIndex = r.content.lower().find('#extm3u')
            if startIndex > -1:
                with open("/home/menny/Documents/m3uAnalyze/pastbin/{0}.m3u".format(id), 'wb') as f:
                    f.write(r.content[startIndex:])
                return 1
            else:
                return -1
        else:
            return r.status_code
    except Exception, e:
        return 0

def getlinks(start, num = 20):
    headers = {
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8,he;q=0.6,uz;q=0.4',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'x-chrome-uma-enabled': '1',
        'accept': '*/*',
        'referer': 'https://cse.google.com/cse/publicurl?cx=012799103566678627508:nho1thiqwow',
        'authority': 'www.googleapis.com',
        'x-client-data': 'CIW2yQEIpbbJAQiLmMoBCPqcygEIqZ3KAQjSncoB',
    }

    params = (
        ('key', 'AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY'),
        ('rsz', 'filtered_cse'),
        ('hl', 'en'),
        ('prettyPrint', 'false'),
        ('source', 'gcsc'),
        ('gss', '.com'),
        ('sig', '01d3e4019d02927b30f1da06094837dc'),
        ('start', str(start)),
        ('num', str(num)),
        ('cx', '012799103566678627508:nho1thiqwow'),
        ('q', '#EXTM3U'),
        ('cse_tok', 'AHL74MxZ2ZNxbvZBlxdaZAYdBlUa:1505232331339'),
        ('sort', 'date'),
        ('googlehost', 'www.google.com'),
        ('callback', 'google.search.Search.apiary11280'),
        ('nocache', '1503928818073'),
    )

    # params = (
    #     ('cse_tok', 'AHL74MwOaAM3PVz1_unqQVsoH9DS:1504995612148'),

    d = requests.get('https://www.googleapis.com/customsearch/v1element', headers=headers, params=params)
    data = d.content
    startfindkey = '"url":"https://pastebin.com/'
    links =[]
    start = 0
    end = 0
    while start>-1 and end>-1:
        start = data.find(startfindkey)
        data = data[start+len(startfindkey):]
        end = data.find('","visibleUrl":"')
        if start>-1 and end>-1:
            link =  urllib2.unquote(data[0:end])
            data = data[end:len(data)]
            links.append(link)
    return links

links = []
for i in range(5):
    links.extend(getlinks(i * 20))
jsonfilepath = "/home/menny/Documents/m3uAnalyze/pastbin/sum.pjson"
with open(jsonfilepath) as json_data:
    dict = json.load(json_data)
    print(dict)

for id in links:
    if (dict.__contains__(id)):
        if dict[id] > -1:
            print (id, "exist")
            continue
    dict[id] = -1
    status = downloadFromPastebin(id)
    print("finished id: {0} with status: {1}".format(id, status))
    if status == 1:
        dict[id] = 0
        playlist = m3uFileChecker.parsem3u("/home/menny/Documents/m3uAnalyze/pastbin/{0}.m3u".format(id), source='pastebin', m3uID=id, isChkSpeedAll=False)
        if playlist.__len__() > 0:
            with open('/home/menny/Documents/m3uAnalyze/pastbin/{0}.json'.format(id), 'w') as outfile:
                json.dump(playlist, outfile)
            print "finished analyzing m3u file"
            dict[id] = playlist.__len__()
        else:
            print "no working m3u list"
    with open(jsonfilepath, 'w') as outfile:
        d = json.dump(dict, outfile)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# requests.get('https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=10&hl=en&prettyPrint=false&source=gcsc&gss=.com&sig=01d3e4019d02927b30f1da06094837dc&start=10&cx=012799103566678627508:nho1thiqwow&q=%23EXTM3U&cse_tok=AHL74Mx4iFP5dkMPOhoIGAPSNv5i:1503928817899&sort=date&googlehost=www.google.com&callback=google.search.Search.apiary11280&nocache=1503928818073', headers=headers)
