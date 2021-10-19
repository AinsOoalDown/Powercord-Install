from logging import exception
import os
from git import Repo
folder = os.path.expanduser('~\Documents\powercord\src\Powercord\plugins')

pluginfile = open('urls.txt')
pluginlist = pluginfile.read()
plugins = pluginlist.split()
namefile = open('names.txt')
names = namefile.read().split()


for i in range(len(plugins)):
    try:
        Repo.clone_from(plugins[i], folder+'\\'+names[i])
        print(names[i])
    except Exception:
        continue
try:
    Repo.clone_from('https://github.com/ClearVision/ClearVision-v6',os.path.expanduser('~\Documents\powercord\src\Powercord\\themes\\ClearVision-v6'))
except:
    print("done")