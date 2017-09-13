import os, base64, re, logging
from elasticsearch import Elasticsearch, RequestsHttpConnection
import certifi

# # Log transport details (optional):
# logging.basicConfig(level=logging.INFO)
#
# # Parse the auth and host from env:
# bonsai = 'https://7tq809ui9t:81zcbfj9rc@first-cluster-899029525.us-east-1.bonsaisearch.net'
# auth = re.search('https\:\/\/(.*)\@', bonsai).group(1).split(':')
# host = bonsai.replace('https://%s:%s@' % (auth[0], auth[1]), '')
#
# # Connect to cluster over SSL using auth for best security:
# es_header = [{
#   'host': host,
#   'port': 443,
#   'use_ssl': True,
#
#   'http_auth': (auth[0],auth[1])
# }]
#
# # Instantiate the new Elasticsearch connection:
# es = Elasticsearch(
#     host= host,
#     http_auth=(auth[0],auth[1]),
#     port=443,
#     use_ssl=True,
#     verify_certs=True,
#     ca_certs=certifi.where(),
# )
es = Elasticsearch('localhost:9200')
# Verify that Python can talk to Bonsai (optional):
es.ping()

from elasticsearch import Elasticsearch
from datetime import datetime
doc = {
    'link': 'runfirstIndex',
    'title': 'Elasticsearch: cool',
    'speed': 0.005,
    'create': datetime.now(),
    'lastupdate': datetime.now(),
    'info': 'inf',
    'statuscode': 401,
    'source': 'pastebin'
}
try:

    res = es.index(index="iptv", doc_type='m3u', body=doc)
    # print(res['created'])
    #res = es.create("iptv", 'm3u', body=doc)
    #print(res)
    # res = es.update("iptv", 'm3u', 'AV48G6veDFC85K7o6SsB', {'doc': doc})
    # print(res['updated'])
except Exception, e:
    print e

#res = es.get(index="iptv", doc_type='m3u', id='AV48G6veDFC85K7o6SsB')
#print(res['_source'])

es.indices.refresh(index="iptv")

res = es.search(index="iptv", body={"query": {"match_all": {}}})
query2field = {
  "query": {
    "bool": {
      "must": [{"match": {"link": "http://66.70.178.201:25461/live/demo/70w/25.ts"}}],
      #"must": [{"match": {"test": 9}}]
    }
  }
}
ry = {"query": {"match": {"link": 'http://66.70.178.201:25461/live/demo/70w/25.ts'}}}
queryExact = {
    "query" : {
        "constant_score" : {
            "filter" : {
                "term" : {
                    "link" : "http://51.255.77.23:7777/live/simohammed00/simohammed123456/5982.ts"
                }
            }
        }
    }
}
#res = es.search(index="iptv", doc_type="m3u", body=queryExact, size=1000)
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    #print("%(link)s %(lastupdate)s: %(speed)s" % hit["_source"], hit['_id'])
    print(hit['_id'], hit["_source"])