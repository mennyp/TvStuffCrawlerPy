import io
import tester
import random
import elasticIptv


def parsem3u(infile, isCheckRandom = True, source = None, m3uID = None, isChkSpeedAll = True):
    try:
        assert(type(infile) == '_io.TextIOWrapper')
    except AssertionError:
        infile = io.open(infile,'r', encoding="utf-8")

    """
        All M3U files start with #EXTM3U.
        If the first line doesn't start with this, we're either
        not working with an M3U or the file we got is corrupted.
    """

    line = infile.readline().lower()
    if not line.startswith('#extm3u'):
       return

    # initialize playlist variables before reading file
    playlist=[]
    extLine={}
    for line in infile:
        try:
            line=line.strip().lower()
            if line.startswith('#extinf:'):
                # pull length and title from #EXTINF line
                info,title=line.split('#extinf:')[1].split(',',1)
                extLine={'info': info,'title': title}
            elif (len(line) != 0):
                # pull song path from all other, non-blank lines
                extLine['path']=line
                if line.__contains__('youtube.com') or line.__contains__('radio') or \
                        extLine['title'].__contains__('radio') or line.__contains__('youtu.be'):
                    continue


                if elasticIptv.isLinkExist(line) == False:
                    playlist.append(extLine)
                    elasticIptv.add(extLine['path'], title=extLine['title'], info=extLine['info'], source=source, m3uID=m3uID)
                elif isChkSpeedAll:
                    playlist.append(extLine)
                # reset the song variable so it doesn't use the same EXTINF more than once

        except Exception, e:
            print ("error ", e.message, line)
            break
    infile.close()
    lenP = len(playlist)
    chk = True
    if(isCheckRandom and lenP > 15):
        chk = False
        numbers = random.sample(range(0, lenP), (int)(lenP * 0.1))
        for num in numbers:
            speed = tester.downloadFile(playlist[num]['path'])
            playlist[num]['time_elapsed'] = speed
            print (num, speed, playlist[num]['path'], playlist[num]['title'])
            if speed > 0 and speed < 1:
                elasticIptv.add(playlist[num]['path'], speed=speed, statuscode=200)
                chk = True
            else:
                elasticIptv.add(playlist[num]['path'], statuscode=speed)
    newPlayList = []
    if chk:
        for p in playlist:
            if p.has_key('time_elapsed'):
                newPlayList.append(p)
                continue
            speed = tester.downloadFile(p['path'])
            p['time_elapsed'] = speed
            print (speed, p['path'], p['title'])
            if speed > 0 and speed < 1:
                newPlayList.append(p)
                elasticIptv.add(p['path'], speed=speed, statuscode=200)
            else:
                elasticIptv.add(p['path'], statuscode=speed, speed=-1)
        return newPlayList
    else:
        return []


# playlist = parsem3u("/home/menny/Documents/m3uAnalyze/269095.m3u")
# with open('/home/menny/Documents/m3uAnalyze/data.txt', 'w') as outfile:
#     json.dump(playlist, outfile)
