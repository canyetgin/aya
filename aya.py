
import requests
link = "https://images-na.ssl-images-amazon.com/images/I/71CY05k-CxL._AC_SL1500_.jpg"
file_name = "download.data"


def  downloadfile (file_name,link):
      with open(file_name, "wb") as f:

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

            print("%s :[%s%s][%s%s]" % (  file_name,"%",done,'#' * done, ' ' * (50-done)), end="\r" )
           
        print("[OK] "+file_name,end=55*" "+"\n")

downloadfile ("download.data","https://images-na.ssl-images-amazon.com/images/I/71CY05k-CxL._AC_SL1500_.jpg")
downloadfile ("download2.data","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png")