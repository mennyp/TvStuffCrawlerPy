import requests
import m3uFileChecker
import json

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8,he;q=0.6,uz;q=0.4',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'referer': 'https://iptv.zone/en/playlist/258233',
    'authority': 'iptv.zone',
    'cookie': 'bbtimezoneoffset=3; __cfduid=d4f5fc8a548be4bf3c1413cdb770515ef1504550895; _ym_uid=1504796031652083299; _ym_isad=1; bblastvisit=1504550895; bblastactivity=0; bbuserid=84658; bbpassword=8180841e009effe43191eaf91b48291c; IDstack=%2C84658%2C; bblanguageid=1; bbsessionhash=e8dea7ebc8e745cbb43b88d5426ef964; bbplaylist=%2C259528%2C258233',
}

params = (
    ('s', ''),
    ('securitytoken', '1504800874-ac6734de612a2a57d8dee9c15198ba280021d610'),
    ('format', ''),
)


def downloadId(id):
    try:
        r = requests.get('https://iptv.zone/en/download/{0}'.format(id), headers=headers, params=params)
        if r.status_code == 200:
            content = r.content
            if content.startswith('#EXTM3U'):
                with open("/home/menny/Documents/m3uAnalyze/iptvzone/{0}.m3u".format(id), 'wb') as f:
                    f.write(content)
                return 1
            else:
                return -1
        else:
            return r.status_code
    except Exception, e:
        return 0

startid = 268177
    #271022
for count in range(10000):
    id = startid + count
    status = downloadId(id)
    print("finished id: {0} with status: {1}".format(id, status))
    if status == 1:
        playlist = m3uFileChecker.parsem3u("/home/menny/Documents/m3uAnalyze/iptvzone/{0}.m3u".format(id), source='iptvzone',m3uID=id, isChkSpeedAll=False )
        if playlist.__len__() > 0:
            with open('/home/menny/Documents/m3uAnalyze/iptvzone/{0}.json'.format(id), 'w') as outfile:
                json.dump(playlist, outfile)
            print "finished analyzing m3u file"
        else:
            print "no working m3u list"