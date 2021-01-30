
import requests

from win32api import GetFileVersionInfo, LOWORD, HIWORD
def get_version_number(filename):
    try:
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return "Unknown version"

version = ".".join([str (i) for i in get_version_number (
        r'download.data')])
print (version)

def  downloadfile (file_name,link):
      with open(file_name, "wb") as f:

       response = requests.get(link, stream=True)
       total_length = response.headers.get('content-length')

       if total_length is None: # no content l bvngth header
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
downloadfile ("download2.data","http://www.prolific.com.tw/UserFiles/files/PL2303_Prolific_DriverInstaller_v1200.zip")