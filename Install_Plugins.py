import os
from git import Repo

folder = os.path.expanduser('~\Documents\powercord\src\Powercord\plugins')

pluginfile = open('output.txt')
pluginlist = pluginfile.read()
plugins = pluginlist.split()
namefile = open('output.txt')
names = namefile.read().split()


for plugin in plugins:
    for name in namefile:
        Repo.clone_from(plugin, folder+'\\'+name)
