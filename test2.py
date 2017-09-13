import pycurl, validators


def url_exists(url):
    """
    Check if the given URL really exists
    :param url: str
    :return: bool
    """
    if validators.url(url):
        c = pycurl.Curl()
        c.setopt(pycurl.NOBODY, True)
        c.setopt(pycurl.FOLLOWLOCATION, False)
        c.setopt(pycurl.CONNECTTIMEOUT, 2)
        c.setopt(pycurl.TIMEOUT, 2)
        c.setopt(pycurl.COOKIEFILE, '')
        c.setopt(pycurl.URL, url)
        try:
            c.perform()
            response_code = c.getinfo(pycurl.RESPONSE_CODE)
            c.close()
            return True if response_code < 400 else False
        except pycurl.error as err:
            errno, errstr = err
            # raise OSError('An error occurred: {}'.format(errstr))
            return False
    else:
        # raise ValueError('"{}" is not a valid url'.format(url))
        return False

url = "http://93.190.138.26:8080/live/zakariaadmin/JNFunfIUN/7479.ts"
if(url_exists(url)):
    print "success " + url
else:
    print "Error " + url