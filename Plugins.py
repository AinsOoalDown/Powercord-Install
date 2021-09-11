from pickle import NONE
import time
from logging import exception
from multiprocessing.connection import wait
import os
#import ConfigParser
#parser = ConfigParser.ConfigParser()
folder = os.path.expanduser('~\Documents\powercord\src\Powercord\plugins')
files = os.listdir(folder)
import json
import requests

def search_commits(sha):
   headers = {'Accept': 'application/vnd.github.cloak-preview'}
   req = requests.get('http://api.github.com/search/commits',
       {'q': sha},
       headers=headers)
   return json.loads(req.text)

def asdf(config):
    try:
        return search_commits(config)['items'][0]['repository']['html_url']
    except IndexError:
        return file
    except KeyError:
        print("sleeping")
        time.sleep(20)
        print("done")
        return search_commits(config)['items'][0]['repository']['html_url']
#commit = search_commits('e83c5163316f89bfbde7d9ab23ca2e25604af290')['items'][0]
#commit = search_commits('e83c5163316f89bfbde7d9ab23ca2e25604af290')['items'][0]
#clone_url = commit['repository']['url']
clone_url =[]
bad=[]
for file in files:
    if('pc-'in file):
        
        bad.append(file)
for i in bad:
    files.remove(i)
for file in files:
    path=(folder+'\\'+file+'\.git\\refs\heads\\'+os.listdir(folder+'\\'+file+'\.git\\refs\heads')[0])
    configpath=open(path)
    config=configpath.read()
    configpath.close()
    clone_url.append(asdf(config))
    print("sleeping1")
    time.sleep(5)
    print("done")
print(clone_url)
with open('output.txt', 'w') as output:
    for line in clone_url:
        if type(line)==str:
            output.write(line)
            output.write('\n')
#print(search_commits('5986608aa0d4803df3a77eee73fbeca77836586d'))
#    config.find('url')
#    print(config)