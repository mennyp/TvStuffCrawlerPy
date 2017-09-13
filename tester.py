import requests
import sys, os
import time

def downloadFile(url, tsSize = 2000, fileName = "test", fullsize = None) :
    filePath = "/home/menny/Documents/m3uAnalyze/tsFiles/{0}.ts".format(fileName)
    try:
        with open(filePath, 'wb') as f:
            start = time.clock()
            r = requests.get(url, timeout=1, stream=True)

            if r.status_code == 200:
                #total_length = r.headers.get('content-length')
                dl = 0
                # if total_length is None: # no content length header
                #   f.write(r.content)
                # else:
                if fullsize == None:
                    for chunk in r.iter_content(tsSize):
                        dl += len(chunk)
                        f.write(chunk)
                        return (time.clock() - start)
                else:
                    size = 0
                    for chunk in r.iter_content(tsSize):
                        dl += len(chunk)
                        f.write(chunk)
                        size = tsSize + size
                        if size > fullsize:
                            os.remove(filePath)
                            return (time.clock() - start)
            else:
                return r.status_code
    except Exception ,e:
        return 0
    finally:
        if os._exists(filePath):
            os.remove(filePath)
  # return (time.clock() - start)


def main() :
  if len(sys.argv) > 1 :
        url = sys.argv[1]
  else :
        url = "http://s2.stream.cwdw.live:8080/368/8022/0e08c74dcc4e479dc00b8e50cdd593d397c27722"
        # raw_input("Enter the URL : ")

  time_elapsed = downloadFile(url, 10000, 'chk')
  print "Download complete..."
  print time_elapsed


if __name__ == "__main__" :
  main()
