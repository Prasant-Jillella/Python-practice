__author__ = 'PrasantJillella'
import urllib.request
'''Program to download images and it can also be written as--- from urllib import request  '''
import random
def image_download(url):
    n=random.randrange(1,100)
    full_name= str(n)+".jpg"
    urllib.request.urlretrieve(url,full_name) '''This function is default one to download images'''
image_download(input("Enter the url from which you want to download the image"))