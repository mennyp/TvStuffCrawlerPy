#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, json
import mechanize, urllib2
import time, elasticAlluc
from selenium import webdriver

def getSeleniumOpenloadLink(url):
    r = requests.get(url)
    content = r.content
    if content.find('We’re Sorry!') > 0:
        return "NULL"
    driver = webdriver.Chrome()
    driver.get(url)
    link = driver.execute_script(
        "return 'https://openload.co/stream/'+document.getElementById('streamurl').innerHTML+'?mime=true';")
    driver.close()
    urlNew = urllib2.urlopen(link).geturl()
    return urlNew


def getgoogleDocMovieLink(url): #notWorking Yet
    r = requests.get(url)
    content = r.content
    d = content[:content.rfind('"></video>')]
    link = d[d.rfind('http'):]
    print link
    return link

def getMp4FromUptostream(url): #notWorking Yet
    r = requests.get(url)
    content = r.content
    d = content[:content.rfind('.mp4') + 4]
    link = 'http://' + d[d.rfind('www'):]
    print link
    return link
#getgoogleDocMovieLink('Https://docs.google.com/file/d/0B1g-qdF_18LKRmNOOWlkTVZzdjA/preview')


#print set(getAllucJsonData(200, 100, 'מדובב'))

def getMp4FromVidtoMe(url):
    try:
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        res = br.open(url)
        content = res.read()
        if (content.find("File Not Found") > -1):
            return "NULL"
        br.select_form(nr=1)
        time.sleep(5)
        response = br.submit(name='imhuman', label='Proceed to video')
        #newUrl =response.geturl()
        content = response.read()
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        print link
        return link
    except:
        print 'error'

def getMp4FromGorillavidIn(url):
    try:
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        res = br.open(url)
        content = res.read()
        if (content.find("File Not Found") > -1):
            return "NULL"
        br.select_form(nr=1)
        time.sleep(1)
        response = br.submit()
        #newUrl =response.geturl()
        content = response.read()
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        print link
        return link
    except:
        print 'error'

def getMp4FromNowvideoSx(url):
        try:
            br = mechanize.Browser()
            br.set_handle_equiv(True)
            br.set_handle_redirect(True)
            br.set_handle_referer(True)
            br.set_handle_robots(False)
            br.open(url)
            br.select_form(nr=0)
            #time.sleep(5)
            response = br.submit(name='submit', label='submit')
            # newUrl =response.geturl()
            content = response.read()
            if (content.find("This video is not yet ready! Please try again later!") < 0):
                return "NULL"
            d = content[:content.find('.mp4') + 4]
            link = d[d.rfind('http'):]
            print link
            return link
        except:
            print 'error'

#getMp4FromNowvideoSx('http://www.nowvideo.sx/video/28c30f08f118c')


def getMp4FromThevideoMe(url):

    headers = {
        'origin': 'https://9xbuddy.com',
        'accept-encoding': 'gzip, deflate, br',
        'x-requested-with': 'XMLHttpRequest',
        'accept-language': 'en-US,en;q=0.8,he;q=0.6,uz;q=0.4',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
        'x-csrftoken': 'ae360b0c4bea334a8fb7d63a213d6c45e3a11cff54f9adf61511464c99caf726',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://9xbuddy.com/process?url={0}'.format(url),
        'authority': '9xbuddy.com',
        'cookie': '__cfduid=d2efa40efc8406025a3501759004eb6111505170933; PHPSESSID=heepc2qtc9at64dfp4jsrcmck5; notice=shown; _ga=GA1.2.1220725771.1505170935; _gid=GA1.2.1348551336.1505170935',
    }

    # headers = {
    #     'origin': 'https://9xbuddy.com',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'x-requested-with': 'XMLHttpRequest',
    #     'accept-language': 'en-US,en;q=0.8,he;q=0.6,uz;q=0.4',
    #     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    #     'x-csrftoken': 'ae360b0c4bea334a8fb7d63a213d6c45e3a11cff54f9adf61511464c99caf726',
    #     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     'accept': 'application/json, text/javascript, */*; q=0.01',
    #     'referer': 'https://9xbuddy.com/process?url=https://thevideo.me/v44l0b03dl0a',
    #     'authority': '9xbuddy.com',
    #     'cookie': '__cfduid=d2efa40efc8406025a3501759004eb6111505170933; PHPSESSID=heepc2qtc9at64dfp4jsrcmck5; notice=shown; _ga=GA1.2.1220725771.1505170935; _gid=GA1.2.1348551336.1505170935',
    # }

    data = [
        ('url', url),
    ]


    try:
        r = requests.post('https://9xbuddy.com/action/extract', headers=headers, data=data)
        data = json.loads(r.content)['response']
        link = data['formats'][len(data['formats']) - 1]['children'][0]['children'][3]['children'][0]['href']
    except:
        return None
    return link


#getMp4FromThevideoMe('https://thevideo.me/qigenn37gbxy')

def getMp4FromBitvidSx(url):
    try:
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.open(url)
        br.select_form(nr=1)
        response = br.submit(name='submit', label='submit')
        content = response.read()
        if(content.find("No compatible source was found for this video.") > -1):
            return "NULL"
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        print link
        return link
    except:
        print 'error'

def getMp4FromMovpodIn(url):
    try:
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        res = br.open(url)
        content = res.read()
        if (content.find("File Not Found") > -1):
            return "NULL"
        br.select_form(nr=1)
        response = br.submit()
        content = response.read()
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        print link
        return link
    except:
        print 'error'

def getMp4FromCloudtimeTo(url):
    try:
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.open(url)
        br.select_form(nr=0)
        response = br.submit(name='submit', label='submit')
        content = response.read()
        if (content.find("No compatible source was found for this video.") > -1):
            return "NULL"
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        if link == 'D':
            return "NULL"
        return link
    except:
        print 'error'

#getMp4FromBitvidSx('http://www.bitvid.sx/file/9701fc8d2b0d9')

def getMp4FromStreamcloudEu(url):
    try:
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        res = br.open(url)
        content = res.read()
        if (content.find("No such file with this filename") > -1):
            return "NULL"
        br.select_form(nr=0)
        time.sleep(10)
        response = br.submit(name='imhuman', label='Watch video now')
        # newUrl =response.geturl()
        content = response.read()
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        print link
        return link
    except:
        print 'error'

#getMp4FromStreamcloudEu('http://streamcloud.eu/nnqi61sjsbcg/Tom.and.Jerry.Blast.Off.to.Mars.DVDRip._XviD._HebDub.WWW.SERETIL.ME.avi.html')


# def getMp4FromOpenloadCo(url):
#     try:
#         br = mechanize.Browser()
#         br.set_handle_equiv(False)
#         # br.set_handle_redirect(True)
#         # br.set_handle_referer(True)
#         br.set_handle_robots(False)
#         br.addheaders = [('User-agent',
#                           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')]
#         resp = br.open(url)
#         headers = resp.info()
#         content = resp.read()
#         d = content[content.find('streamurl') + 11:]
#         link = d[d.rfind('http'):]
#         print link
#         return link
#     except Exception, e:
#         print 'error', e.message
#
getSeleniumOpenloadLink('https://openload.co/embed/ziH6tSE5Io/')
# print d

def getMp4FromVidziTv(url):
    try:
        response = requests.get(url)
        # newUrl =response.geturl()
        content = response.content
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        return link
    except:
        print 'error'

#getMp4FromVidziTv('http://vidzi.tv/9fmygeye6gy1.html')


def getMp4FromAuroravidTo(url):
    try:
        br = mechanize.Browser()
        br.set_handle_equiv(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)
        br.open(url)
        br.select_form(nr=0)
        response = br.submit(name='submit', label='submit')
        # newUrl =response.geturl()
        content = response.read()
        if(content.find("No compatible source was found for this video.") > -1):
            return "NULL"
        d = content[:content.find('.mp4') + 4]
        link = d[d.rfind('http'):]
        if link == 'D':
            return "NULL"
        return link
    except:
        print 'error'
#getMp4FromStreamcloudEu('http://streamcloud.eu/9j0ingd4c7i3/Harry.Potter.And.The.Prisoner.Of.Azkaban.DVDRiP.XviD.CD2-HEBDUB-MORIDIM.ME.avi.html')



def getAllucJsonData(from1, count, query):
    r = requests.get("https://www.alluc.ee/api/search/stream/?apikey=ab1f790c52ad9d0bbdf099127dddca40&callback=?&count={0}&from={1}&query={2}&getmeta=1".format(count, from1, query))
    data = json.loads(r.content)['result']
    list = []
    for d in data:
        dict = {}
        dict['filedataid'] = d['hosterurls'][0]['filedataid']
        dict['sourceUrl'] = d['hosterurls'][0]['url']
        dict['title'] = d['title']
        dict['sourceTitle'] = d['sourcetitle']
        dict['hostName'] = d['hostername']
        list.append(dict)
    return list

#vidgg.to,
def startCrawling(query):
    print ('starting crawling', query)
    count = 0
    for i in range(10, 1000):
        list = getAllucJsonData(i * 100, 100, query)
        for l in list:
            count += 1
            if elasticAlluc.isLinkExist(l['filedataid']):
               continue
            host = l['hostName']
            url = l['sourceUrl']
            link = None
            if host == 'thevideo.me':
                getMp4FromThevideoMe(url)
            elif host == 'nowvideo.sx':
                link = getMp4FromNowvideoSx(url)
            elif host == 'auroravid.to':
                link = getMp4FromAuroravidTo(url)
            elif host == 'bitvid.sx':
                link = getMp4FromBitvidSx(url)
            elif host == 'vidzi.tv':
                link = getMp4FromVidziTv(url)
            elif host == 'docs.google.com':
                continue
            elif host == 'streamcloud.eu':
                link = getMp4FromStreamcloudEu(url)
            elif host == 'vidto.me':
                link = getMp4FromVidtoMe(url)
            elif host == 'openload.co':
                link = getSeleniumOpenloadLink(url)
            elif host == 'uptostream.com':
                link = getMp4FromUptostream(url)
            elif host == 'gorillavid.in':
                link = getMp4FromGorillavidIn(url)
            elif host == 'cloudtime.to':
                link = getMp4FromCloudtimeTo(url)
            elif host == 'movpod.in':
                link = getMp4FromMovpodIn(url)
            elif host == 'estream.to': #'https://estream.to/c10zk71gam4z.html'
                continue
            else:
                continue

            isNoMp4 = None
            if link:
                if link == "NULL":
                    isNoMp4 = True
            print (count, link, l['title'], l['sourceUrl'], host)
            elasticAlluc.add(l['filedataid'], link, l['title'], l['sourceUrl'], l['sourceTitle'], host, query, isNoMp4)
        if len(list) < 100:
            print ('finished', query, count)
            return
#getMp4FromUptostream('http://uptostream.com/2fnr56j4i7x2')
startCrawling('מדובב')
#getMp4FromGorillavidIn('http://gorillavid.in/d314xvqt6sx8')
#getMp4FromCloudtimeTo('http://www.cloudtime.to/video/acb8bbd33c602')
#getMp4FromThevideoMe('https://thevideo.me/qigenn37gbxy')
#getMp4FromMovpodIn('http://movpod.in/decvs2bk3d0q')

#'The.Lion.King.1994.WS.DVDRip.XviD.HebDubbed-Gozlan.Horadot.Net_2.avi', 'Spiderman_1994_S01E02_HebDub_XviD.avi' 'Hamofa_Shel_LuLu_S01E01_HebDub_XviD' 'Planes.2013.BDRip.X264-HebDub-Eliran+Gozlan-_2'
#'Smurfs E131 PDTV HebDub XviD-Yonidan', 'Movie', u'Smurfs E131')
# blackList = ['hebdub', 'eliran', 'gozlan', 'hebdubd', 'hebdubbed']
# import PTN
# lines = elasticAlluc.getAll(1000)
# for l in lines:
#     info = PTN.parse(l['title'])
#     if info.__contains__('season') and info.__contains__('episode'):
#         info['type'] = 'TV'
#     else:
#         info['type'] = 'Movie'
#     print(l['title'], info['type'], info['title'])