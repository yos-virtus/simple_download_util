import urllib.request
import sys

def dl_progress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + file_url + "...%d%%" % percent)
    sys.stdout.flush()

files_base_url = input("Base url: ")
ext = input("files extention: ")
print("================================================================")

for n in range(45, 49):
    file_url = "{0}{1}.{2}".format(files_base_url, n, ext)
    urllib.request.urlretrieve(file_url, "{0}.mp4".format(n), reporthook=dl_progress)
    print("")
