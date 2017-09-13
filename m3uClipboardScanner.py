import clipboard, m3uFileChecker, json

def saveContent(content):
    content = clipboard.paste
    if content.startswith('#EXTM3U'):
        from time import gmtime, strftime
        id = strftime("%Y%m%d%H%M%S", gmtime())
        fileName = "/home/menny/Documents/m3uAnalyze/clipboard/{0}.m3u".format(id)
        with open(fileName, 'wb') as f:
            f.write(content)
        dict[id] = 0
        # playlist = m3uFileChecker.parsem3u("/home/menny/Documents/m3uAnalyze/pastbin/{0}.m3u".format(id))
        # if playlist.__len__() > 0:
        #     with open('/home/menny/Documents/m3uAnalyze/clipboard/{0}.json'.format(id), 'w') as outfile:
        #         json.dump(playlist, outfile)
        #     print "finished analyzing m3u file"
        #     dict[id] = playlist.__len__()
        # else:
        #     print "no working m3u list"

        return True
    else:
        return False

