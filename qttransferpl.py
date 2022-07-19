import json
import requests
import wget
import urllib.request
import asyncio
import os

from os import listdir
from os.path import isfile, join

from io import StringIO

import requests

# from importlib import reload
# qtloceditor = reload(qtloceditor) # reload of qtloceditor

# Get and set the current working directory (cwd)
# TIP: If you want to find the directory of the script use os.path.realpath(__file__)

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

cwd = os.chdir('C:/Users/RBecker001/Anaconda3/Lib/transfertest/cutietestrun28May2020')
print("Current working directory: {0}".format(cwd))
'''
qt30list = [cutietestrun28May2020,
cutietestrun4June2020,
cutietestrun18June2020,
cutietestrun30July2020,
cutietestrun2September2020,
cutietestrun22October2020,
cutiestestrun5November2020,
cutiestestrun19November2020,
cutiestestrun10December2020,
cutiestestrun14January2021,
cutiestestrun28january2021,
cutiestestrun18february2021,
cutiestestrun4march2021,
cutiestestrun18march2021,
cutiestestrun15april2021,
cutiestestrun29april2021,
cutietestrun20may2021,
cutietestrun27may2021,
cutietestrun10June2021,
cutietestrun24June2021,
cutietestrun8july2021,
qt11112021wtxt,
qt28102021wtxt,
qt14102021wtxt,
qt30092021wtxt,
qt16092021wtxt,
qt02092021wtxt,
qt19082021wtxt,
qt05082021wtxt,
qt22072021wtxt]
'''

# instead change directory here
outd = str(cwd) + "\\test"
# Read in the nodesets as a list
onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
print(onlyfiles)

'''
async def io_related(name):
	print(f'{name} started')
	url = 'http://corpora.aifdb.org/list.php/helpers/corporanodesets.php?shortname=qt14102021wtxt'
	nodeset = requests.get(url)
	await asyncio.sleep(5)
	print(f'{name} finished')

async def main():
	await asyncio.gather(
        io_related('first'),
        io_related('second'),
	)  # 1s + 1s = over 1s

if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
'''

url = ''
# QT urls
# url = 'http://corporaqt.arg.tech/cutiestestrun19November2020'
# url = 'http://ova3qt.arg.tech/db/22744'
# url = 'http://txtdbqt.arg.tech/view.php?id=22744'

# AIFdb urls
#url = 'http://ova.arg-tech.org/db/'
#url = 'http://corpora.aifdb.org/nodesets.php?shortname=qt14102021wtxt'
#url = 'http://corpora.aifdb.org/nodesets.php?shortname=qt05082021wtxt'
url = 'http://corpora.aifdb.org/nodesets.php?shortname=cutietestrun28May2020'
#url = 'http://aifdbqt.arg.tech/nodesets/t/18997'
#url = 'http://localhost:5000/nodesets/t/17857'
nodeset = wget.download(url)

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

# print(data)

for nodeid in data["nodeSets"]:
	print("----")
	print('Opening url with ' + str(nodeid))
	url = 'http://www.aifdb.org/pl/' + str(nodeid)
	print(url)
	wget.download(url)

print (nodeset.status_code)
