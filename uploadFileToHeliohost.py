import requests

cookies = {
    '_ga': 'GA1.2.1668426238.1503847072',
    '_gid': 'GA1.2.1183588913.1503847072',
    'timezone': 'Asia/Damascus',
    'cpsession': 'mpinhaso%3awWS1WGSpQYZu6qlV%2c4a1700ff7b90c8f258ea469eeddde9ba',
}

headers = {
    'Origin': 'https://johnny.heliohost.org:2083',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,he;q=0.6,uz;q=0.4',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarywGLANc63p09heEvf',
    'Accept': '*/*',
    'Referer': 'https://johnny.heliohost.org:2083/cpsess3716617132/frontend/paper_lantern/filemanager/upload-ajax.html?file=sitemap.xml&fileop=&dir=%2Fhome%2Fmpinhaso%2Fpublic_html&dirop=&charset=&file_charset=&baseurl=&basedir=',
    'Connection': 'keep-alive',
}

data = '$------WebKitFormBoundarywGLANc63p09heEvf\\r\\nContent-Disposition: form-data; name="get_disk_info"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundarywGLANc63p09heEvf\\r\\nContent-Disposition: form-data; name="dir"\\r\\n\\r\\n/home/mpinhaso/public_html\\r\\n------WebKitFormBoundarywGLANc63p09heEvf\\r\\nContent-Disposition: form-data; name="file-0"; filename="269489.m3u"\\r\\nContent-Type: audio/x-mpegurl\\r\\n\\r\\n\\r\\n------WebKitFormBoundarywGLANc63p09heEvf\\r\\nContent-Disposition: form-data; name="overwrite"\\r\\n\\r\\n1\\r\\n------WebKitFormBoundarywGLANc63p09heEvf--\\r\\n'
try:
    requests.post('https://johnny.heliohost.org:2083/cpsess3716617132/execute/Fileman/upload_files', headers=headers, cookies=cookies, data=data)
    print "ok"
except Exception, e:
    print e