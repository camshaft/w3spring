import . as slk

import fnmatch
import os

fileList = []
for root, dirnames, filenames in os.walk('./../../assets/'):
  for filename in fnmatch.filter(filenames, '*.slk'):
      fileList.append(os.path.join(root, filename))

for relFile in fileList:
    slk.readSlk(relFile)
