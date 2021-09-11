#import stuff
import os
from configparser import ConfigParser

#find powercord plugins folder
folder = os.path.expanduser('~\Documents\powercord\src\Powercord\plugins')
files = os.listdir(folder)

clone_url =[]
#find and mark unnnecessary files
bad=[]
for file in files:
    if('pc-'in file):
        
        bad.append(file)
#remove unnnecessary files
for i in bad:
    files.remove(i)

for file in files:
    path=(folder+'\\'+file+'\.git\\config')
    config_object = ConfigParser()
    config_object.read(path)
    #Get the repo
    config = config_object["remote \"origin\""]
    #append to array
    clone_url.append(config["url"])
#write to output
with open('output.txt', 'w') as output:
    for line in clone_url:
        output.write(line)
        output.write('\n')