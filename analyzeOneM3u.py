import requests
import m3uFileChecker
import json, tester

def checkOneM3uFile(m3uFilePath, source = None):
    playlist = m3uFileChecker.parsem3u(m3uFilePath, False, source)
    for p in playlist:
        if (p['path'].endswith('.mp4')):
            try:
                p['title'] = 'mp4 - {0}'.format(p['title'].encode('utf-8'))
                print p['title']
            except:
                continue
    # if playlist.__len__() > 0:
    #     with open(outJsonFilePath, 'w') as outfile:
    #         json.dump(playlist, outfile)
    #     print "finished analyzing m3u file"
    # else:
    #     print "no working m3u list"

checkOneM3uFile("/home/menny/Documents/m3uAnalyze/iptvzone/iptvzone.m3u", 'iptvzone')
def downloadId(id):
    try:
        r = requests.get('https://pastebin.com/raw/{0}'.format(id))
        if r.status_code == 200:
            content = r.content
            if content.startswith('#EXTM3U'):
                with open("/home/menny/Documents/m3uAnalyze/{0}.m3u".format(id), 'wb') as f:
                    f.write(content)
                return 1
            else:
                return -1
        else:
            return r.status_code
    except Exception, e:
        return 0
def checkSomePastbinIds():
    for id in [' FvFQdp8A','n2SE9DTp','ffGsL/3m0','DKJyuwHH','SMkGQDAm','2rVZ6LZ','LnZU7sgG',
               'uxEW2sr3','MuZ7ab1P','5yx8tQrL']:
        status = downloadId(id)
        print("finished id: {0} with status: {1}".format(id, status))
        if status == 1:
            playlist = m3uFileChecker.parsem3u("/home/menny/Documents/m3uAnalyze/{0}.m3u".format(id), 'pastebin', id)
            if playlist.__len__() > 0:
                with open('/home/menny/Documents/m3uAnalyze/{0}.json'.format(id), 'w') as outfile:
                    json.dump(playlist, outfile)
                print "finished analyzing m3u file"
            else:
                print "no working m3u list"

def scanUrlTs():
    list = []
    for i in range(20000):
        url = "http://217.23.1.3:6969/live/batman/batman/{0}.m3u8".format(i)
        speed = tester.downloadFile(url)
        print (speed, url)
        if speed > 0 and speed < 1:
            extLine = {'time_elapsed': speed, 'title': str(i), 'path': url}
            list.append(extLine)
    return list

# playlist = scanUrlTs()
# id = "scanIl"
# with open('/home/menny/Documents/m3uAnalyze/{0}.json'.format(id), 'w') as outfile:
#     json.dump(playlist, outfile)
# print "finished analyzing m3u file"

#checkSomePastbinIds()