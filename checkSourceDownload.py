import tester,elasticIptv

def testElasticSourceDownload():
    lines = elasticIptv.getWorkingList(10000)
    print 'got from elastic {0} rows'.format(len(lines))
    for l in lines:
        fileName = generateFileName(l['title'])
        status = tester.downloadFile(l['link'], 1000, fileName, 10000000)
        if status == 0 or status == None:
            elasticIptv.add(link=l['link'], speed=0)
        elif status > 300:
            elasticIptv.add(link=l['link'], speed=0, statuscode=status)
        else:
            elasticIptv.add(link=l['link'], statuscode=200, downloadSpeed=status)
        print status, fileName
    return True

def generateFileName(title):
    from time import gmtime, strftime
    id = strftime("%Y%m%d%H%M%S", gmtime())
    fileName = "{0} - {1}".format(id, title.encode('utf-8'))
    return fileName

testElasticSourceDownload()
