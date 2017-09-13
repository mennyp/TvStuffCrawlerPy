import json, os
import glob


def convertJsonToM3u(jsonfilepath):
    dict = {}
    with open(jsonfilepath) as json_data:
        d = json.load(json_data, encoding=('utf-8'))
        print (d.__len__())
        lines = []
        for c in d:
            if c.__contains__('time_elapsed'):
                c['title'] = c['title'].strip()
                if dict.__contains__(c['path']):
                    continue
                elif  c['time_elapsed'] == 0:
                    continue
                elif c['time_elapsed'] > 1:
                    continue
                dict[c['path']] = c
                lines.append(c)
            else:
                print ("no time_elapsed property", jsonfilepath)
        return lines

def mergeM3uinFolder(folderName):
    lines = []
    try:
        g = "/home/menny/Documents/m3uAnalyze/{0}/*.json".format(folderName)
        jsons =  glob.glob(g)
        for jsonFile in jsons:
            lines.extend(convertJsonToM3u(jsonFile))

        lines1 = sorted(lines, key=lambda k: (k.get('title'), k.get('time_elapsed')))
            #'time_elapsed', 0), reverse=False)
        print ("finished {0}".format(lines1.__len__()))
        fileName = folderName
            #"speed"
        with open('/home/menny/Documents/m3uAnalyze/{0}/{1}.json'.format(folderName, fileName), 'w') as outfile:
            json.dump(lines1, outfile)
        with open("/home/menny/Documents/m3uAnalyze/{0}/{1}.m3u".format(folderName, fileName), 'wb') as f:
            f.write("#EXTM3U\n")
            f.write("#EXTINF:-1, {0}\n".format('count: {0}'.format(lines1.__len__())))
            f.write("{0}\n".format('http://192.99.18.85:1935/live/sport1/playlist.m3u8'))
            for c in lines1:
                f.write("#EXTINF:-1, {0}\n".format(c['title'].encode('utf-8')))
                f.write("{0}\n".format(c['path'].encode('utf8')))
        for jsonFile in jsons:
            if(jsonFile.__contains__(folderName)):
                continue
            os.remove(jsonFile)
    except Exception, e:
        print e

mergeM3uinFolder('pastbin')
    #'scanUrl')
    #'iptvzone')
    #'pastbin')

