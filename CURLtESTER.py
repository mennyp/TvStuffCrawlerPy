import requests

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8,he;q=0.6,uz;q=0.4',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'referer': 'https://iptv.zone/en/playlist/269548',
    'authority': 'iptv.zone',
    'cookie': '__cfduid=d67401a47d00068f9f03994c1ab2d27551503822951; bblastvisit=1503822951; _ym_uid=1503822980523290443; _ym_isad=1; bbtimezoneoffset=3; bblastactivity=0; bbuserid=84658; bbpassword=8180841e009effe43191eaf91b48291c; IDstack=%2C84658%2C; bblanguageid=1; bbsessionhash=bfd5e465ea9b1f8f584d405147609e18; bbplaylist=%2C269548',
}

params = (
    ('s', ''),
    ('securitytoken', '1503842455-f5ec3471546f665e88784a069127761795d3b52e'),
    ('format', ''),
)

requests.get('https://iptv.zone/en/download/269550', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# requests.get('https://iptv.zone/en/download/269550?s=&securitytoken=1503842455-f5ec3471546f665e88784a069127761795d3b52e&format=', headers=headers)
