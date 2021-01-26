import requests
import sys
link = "http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf"
file_name = "download.data"
with open(file_name, "wb") as f:
    print ("Downloading %s" % file_name)
    response = requests.get(link, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None: # no content length header
        f.write(response.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in response.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            print("[%s%s]" % ('=' * done, ' ' * (50-done)), end="\r" )    
           
        print("[OK]",end=49*" "+"\r")    