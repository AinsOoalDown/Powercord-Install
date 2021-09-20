from logging import exception
import os
from git import Repo
folder = os.path.expanduser('~\Documents\powercord\src\Powercord\plugins')

pluginfile = open('urls.txt')
pluginlist = pluginfile.read()
plugins = pluginlist.split()
namefile = open('names.txt')
names = namefile.read().split()


for plugin in plugins:
    for name in names:
        try:
            Repo.clone_from(plugin, folder+'\\'+name)
            print(name)
        except Exception:
            continue
try:
    Repo.clone_from('https://github.com/ClearVision/ClearVision-v6',os.path.expanduser('~\Documents\powercord\src\Powercord\\themes\\ClearVision-v6'))
except:
    print("done")