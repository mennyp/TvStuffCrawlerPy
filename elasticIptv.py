from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')

from datetime import datetime

# clear index
#curl -XDELETE 'http://localhost:9200/iptv/'

def add(link, title = None, speed = None, info = None, statuscode = None, source = None,
        m3uID = None, downloadSpeed = None, type = None):

    doc = {
        'link': link,
        'lastupdate': datetime.now(),
    }
    if title:
        doc['title'] = title
    if speed != None:
        doc['speed'] = speed
    if info:
        doc['info'] = info
    if statuscode:
        doc['statuscode'] = statuscode
    if source:
        doc['source'] = source
    if m3uID:
        doc['m3uID_'] = m3uID
    if downloadSpeed:
        doc['downloadSpeed'] = downloadSpeed
    if type:
        doc['type'] = type

    try:
        exist = es.exists(index="iptv", doc_type='m3u', id=link)
        #res = es.search(index="iptv", doc_type="m3u", body=queryExact)
        if exist:
            res = es.update(index="iptv", doc_type='m3u', id=link, body={'doc': doc})
            print "elastic updated"
        else:
            doc['create'] = datetime.now()
            if link.endswith('.mp4') or link.endswith('.flv') or link.endswith('.mkv'):
                doc['type'] = 'vod'
            else:
                doc['type'] = 'tv'
            res = es.index(index="iptv", doc_type='m3u', id=link, body=doc)
            print ("elastic created", doc)

        #print(res['elastic success'])
    except Exception, e:
        print e

def isLinkExist(link):
    try:
        # queryExact = {
        #     "query": {
        #         "constant_score": {
        #             "filter": {
        #                 "term": {
        #                     "link": link
        #                 }
        #             }
        #         }
        #     }
        # }

        #res = es.search(index="iptv", doc_type="m3u", body=queryExact)
        #exist = res['hits']['total'] > 0
        #print (link, exist)
        return es.exists(index="iptv", doc_type='m3u', id=link)
    except Exception, e:
        print e

def getListWithSpeed(size):
    query = {
        "query": {
            "range" : {
                "speed" : {
                    "gte" : 0.000000001,
                    "lte" : 0.9
                }
            }
        },
        "sort" : [
        "title"
        ],
        "size": size
    }
    return returnQuery(query)

def getListWithDownloadStatus(size):
    query = {
        "query": {
            "range" : {
                "downloadSpeed" : {
                    "gte" : 0.01,
                    "lte" : 2.9
                }
            }
        },
        "sort" : [
        "downloadSpeed"
        ],
        "size": size
    }
    return returnQuery(query)

def getTVListWithDownloadStatus(from1, size, type):
    query = {
        "query": {
        "bool": {
            "must": {
                "constant_score": {
                    "filter": {
                        "term": {
                            "type": type
                        }
                    }
                }
        },
            "filter": {
                "range": {"downloadSpeed": {
                    "gte" : 0.0001,
                    "lte" : 3
                }}
            }
        }},
        "sort" : [
        "title"
        ],
        "from": from1,
        "size": size

    }
    return returnQuery(query)

def searchTitle(titleKey, size):
    query = {
        "query": {
        "bool": {
            "must": {
          "query_string": {
            "default_field": "title",
            "query": "*{0}*".format(titleKey)
          }
        },
            "filter": {
                "range": {"speed": {
                    "gte" : 0.000000001,
                    "lte" : 0.9
                }}
            }
        }},
        "sort" : [
        "title"
        ],
        "size": size
    }
    return returnQuery(query)

def searchVod( size):
    query = {
        "query": {
        "bool": {
            "must": {
          "query_string": {
            "default_field": "link",
            "query": "*flv*"
          }
        },
            "filter": {
                "constant_score": {
                    "filter": {
                        "term": {
                            "type": 'tv'
                        }
                    }
                }
            }
        }},
        "sort" : [
        "title"
        ],
        "size": size
    }
    return returnQuery(query)

def getListWithSpeedNoDownloadStatus(size):
    query = {
        "query": {
            "bool": {
                "must_not": {
                    "exists": {"field": "downloadSpeed"}
                },
                "filter": {
                    "range": {"speed": {
                        "gte": 0.000000001,
                        "lte": 0.9
                    }}
                }
            }},
        "size": size
    }
    return returnQuery(query)

def getListWithDownloadNoType(from1, size):
    query = {
        "query": {
            "bool": {
                "must_not": {
                    "exists": {"field": "type"}
                },
                "filter": {
                    "range": {"speed": {
                        "gte": 0.000000001,
                        "lte": 0.9
                    }}
              }
            }},
        "from": from1,
        "size": size
    }
    return returnQuery(query)

def returnQuery(query):
    res = es.search(index="iptv", doc_type="m3u", body=query)
    lines = []
    for hit in res['hits']['hits']:
        #print(hit['_id'], hit["_source"])
        lines.append(hit["_source"])
    return lines

list = searchVod(10000)
for l in list:
    add(link=l['link'], type='vod')