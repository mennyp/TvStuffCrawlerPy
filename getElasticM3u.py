
import elasticIptv, elasticAlluc

def createWorkingM3u():
    type = 'vod'
    fileName = generateFileName(type)
    lines = elasticIptv.getTVListWithDownloadStatus(1300, 200, type)
    print len(lines)
    with open(fileName, 'wb') as f:
        f.write("#EXTM3U\n")
        for c in lines:
            f.write("#EXTINF:-1, {0}\n".format(c['title'].encode('utf-8')))
            f.write("{0}\n".format(c['link'].encode('utf8')))
    print ('finished', fileName)

def createAllucWorkingM3u():
    type = 'vod'
    fileName = generateFileName(type)
    lines = elasticAlluc.searchWorkingMp4(3000, 1000)
    print len(lines)
    with open(fileName, 'wb') as f:
        f.write("#EXTM3U\n")
        for c in lines:
            f.write("#EXTINF:-1, {0}\n".format(c['title'].encode('utf-8')))
            f.write("{0}\n".format(c['mp4Link'].encode('utf8')))
    print ('finished', fileName)

def generateFileName(type):
    from time import gmtime, strftime
    id = strftime("%Y%m%d%H%M%S", gmtime())
    fileName = "/home/menny/Documents/m3uAnalyze/elastic/{0}_{1}.m3u".format(id, type)
    return fileName

createAllucWorkingM3u()
