__author__ = 'PrasantJillella'
from urllib import request
def file_down(url_source):
    response1 =request.urlopen(url_source)
    csv = response1.read()
    csv_str=str(csv)
    lines=csv_str.split("\\n") ''''''
    dest_url=r"down_file.csv"
    fp=open(dest_url,"w")
    for line in lines:
        fp.write(line+"\n")
    fp.close()
file_down(str(input("Enter The url from where we want to download file")))