# Coded By Sameera a.k.a άλφα Χ

import os
import collections
import hashlib

banner = r'''
     ___                      _
    | . \ ___  ___  ___  ___ | | ___  ___ ._ _  ___  ___  _ _
    | | |/ . \| . \| . \/ ._>| |/ . |<_> || ' |/ . |/ ._>| '_>
    |___/\___/|  _/|  _/\___.|_|\_. |<___||_|_|\_. |\___.|_|
              |_|  |_|          <___'          <___'

                [Coded By Sameera a.k.a άλφα Χ]

'''
print(banner)
path = input("Select a directory to begin scan - ")
print('\n', end="")

if not os.path.isdir(path):
    print('Oops!! Directory not found!')
else:

    file_path = []
    for root, dir, files in os.walk(path):
        for f in files:
            filepath = os.path.join(root, f)
            file_path.append(filepath)

    filesize = {}

    for filenames in file_path:
        size = os.path.getsize(filenames)

        if size in filesize.keys():
            filesize[size].append(filenames)
        else:
            filesize[size] = []
            filesize[size].append(filenames)

    samefilesize = {}

    for size in filesize:
        x = filesize[size]
        if (len(x) > 1):
            samefilesize[size] = x

    def md5(f):

        md5Hash = hashlib.md5()
        with open(f, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5Hash.update(chunk)
        return md5Hash.hexdigest()

    hashlist = {}

    for size in samefilesize:
        file_path = samefilesize[size]
        for filenames in file_path:
            y = md5(filenames)
            if y in hashlist.keys():
                hashlist[y].append(filenames)
            else:
                hashlist[y] = []
                hashlist[y].append(filenames)

    duplicateFiles = {}

    for y in hashlist:
        File = hashlist[y]
        if (len(File) > 1):
            duplicateFiles[y] = File
    if not duplicateFiles:
        print("No duplicate files found")
    else:
        d = len(duplicateFiles)
        if d == 1:
            print(str(d) + " Duplicate file found")
            print('\n', end="")
        else:
            print(str(d) + " Duplicate files found")
            print('\n', end="")
        for k, v in duplicateFiles.items():
            print('\n', end="")
            print(str(k) + '\n' + str(v))
