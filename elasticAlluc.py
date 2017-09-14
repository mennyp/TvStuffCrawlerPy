from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')

from datetime import datetime

# clear index
#curl -XDELETE 'http://localhost:9200/alluc/'

def add(filedataid, mp4Link = None, title = None, sourceUrl = None, sourceTitle = None, hostName = None,
        query = None, isNoMp4 = None, file_info = None, movie_info = None):

    doc = {
        'lastupdate': datetime.now(),
    }
    if title:
        doc['title'] = title
    if mp4Link:
        doc['mp4Link'] = mp4Link
    if sourceUrl:
        doc['sourceUrl'] = sourceUrl
    if sourceTitle:
        doc['sourceTitle'] = sourceTitle
    if hostName:
        doc['hostName'] = hostName
    if query:
        doc['query'] = query
    if isNoMp4 != None:
        doc['isNoMp4'] = isNoMp4
    if file_info:
        doc['file_info'] = file_info
    if movie_info:
        doc['movie_info'] = movie_info

    try:
        exist = es.exists(index="alluc", doc_type='mp4', id=filedataid)
        #res = es.search(index="iptv", doc_type="m3u", body=queryExact)
        if exist:
            res = es.update(index="alluc", doc_type='mp4', id=filedataid, body={'doc': doc})
            print "elastic updated"
        else:
            doc['create'] = datetime.now()
            res = es.index(index="alluc", doc_type='mp4', id=filedataid, body=doc)
            print ("elastic created")

        #print(res['elastic success'])
    except Exception, e:
        print e

def isLinkExist(filedataid):
    try:
        return es.exists(index="alluc", doc_type='mp4', id=filedataid)
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

def getAll(size):
    query = {
        "query": {
            "match_all": {}
        },
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

def searchWorkingMp4(from1,  size):
    query = {
        "query": {
        "bool": {
            "must": {
          "query_string": {
            "default_field": "mp4Link",
            "query": "*http*"
          }
        }
        }},
        "from": from1,
        "size": size
    }
    return returnQuery(query)

def searchMovie(from1,  size):
    query = {
        "query": {
            "match" : {
                "movie_info.video" : False
            }
        },
        "from": from1,
        "size": size,
        "sort" : "movie_info.title"

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
    res = es.search(index="alluc", doc_type="mp4", body=query)
    lines = []
    for hit in res['hits']['hits']:
        #print(hit['_id'], hit["_source"])
        hit["_source"]['filedataid'] = hit["_id"]
        lines.append(hit["_source"])
    return lines

# list = searchWorkingMp4(10000)
# print len(list)
# for l in list:
#    add(link=l['link'], type='vod')