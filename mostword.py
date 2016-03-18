# -*- coding: utf-8 -*-

#Creates a List, which words are most often in the ID3Tags of a folder of
#mp3s.... script includes all subfolders

import os, re, operator
from mutagen.mp3 import EasyMP3 as MP3

inFol = ".../Music/" #folder that contains all mp3, subfolders allowed

#Write all filenames from a folder and its subfolder to a list
fileList = []
for root,dirs,files in os.walk(inFol):
    
    for name in files:
        #print(os.path.join(root, name))
        fileList.append(os.path.join(root, name))
    for name in dirs:
        #print(os.path.join(root, name))
        fileList.append(os.path.join(root, name))

#read songtitles from file ID3 Tags
titleList = []
for files in fileList:
    if files[-3:].lower() == "mp3":
        try:
            songName = MP3(files)['title']
            titleList.append(songName)
        except:
            print(files + " not working")
            pass

 
songDict = {'x':0}

#add all title words to the dictionary, split them first to words by re
for songName in titleList:
    songNameWords = re.split(';|,| |_|\.',songName[0])
    for i in songNameWords:
        smallCaps = i.lower()
        if smallCaps in songDict:
            oldVal = songDict[smallCaps]
            newVal = oldVal + 1
            songDict[smallCaps] = newVal
        else:
            songDict[smallCaps] = 1

#delete certain keys that should not appear in the final list
delList = ["the",'','of','a','to','in','and','my','me',
           'for','at', 'tim','timebomb', 'on', 'is',
           'don\'t', 'we', 'this', 'be', '&', 'are',
           'with','what', 'so', 'here', 'at', 'that',
           'have', 'version', 'do', 'la', 'el', 'der']
for delWord in delList:
    if delWord in songDict:
        del songDict[delWord]


#sort entries to a list (forward and reverse)                                                                                              
sorted_x = sorted(songDict.items(), key=operator.itemgetter(1))
sorted_rev = sorted_x[::-1]
