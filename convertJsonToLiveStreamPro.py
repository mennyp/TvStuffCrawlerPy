import clipboard, json

def xml_out(parsed_file, id):
    with open("/home/menny/Documents/m3uAnalyze/clipboard/{0}.xml".format(id), 'w') as f:
        f.write('<streamingInfos>\n')
        for i in parsed_file:
            f.write('<item>\n')
            f.write('<title>{0}</title>\n'.format(i["title"]))
            f.write('<link>plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;url={0}</link>\n'.format(i["path"]))
            f.write('<thumbnail>{0}</thumbnail>\n'.format(""))
            f.write('</item>\n')
        f.write('</streamingInfos>\n')

s = clipboard.paste().lower()
d = s.split('\n')
playlist = []
for line in d:
    try:
        if line.startswith('#extm3u'):
            continue
        elif line.startswith('#extinf:'):
            # pull length and title from #EXTINF line
            info, title = line.split('#extinf:')[1].split(',', 1)
            extLine = {'info': info, 'title': title}
        elif (len(line) != 0):
            # pull song path from all other, non-blank lines
            extLine['path'] = line
            if line.__contains__('youtube.com') or line.__contains__('radio') or \
                    extLine['title'].__contains__('radio') or line.__contains__('youtu.be'):
                continue
            extLine['time_elapsed'] = 0.5
            playlist.append(extLine)
            # reset the song variable so it doesn't use the same EXTINF more than once

    except:
        print ("error", line)
        continue
xml_out(playlist, 'israel')
print "finished"