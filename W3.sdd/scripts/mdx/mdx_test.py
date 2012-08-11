import mdx

import fnmatch
import os

fileList = []
for root, dirnames, filenames in os.walk('./../../assets/'):
  for filename in fnmatch.filter(filenames, '*.mdx'):
      fileList.append(os.path.join(root, filename))

def testFiles(fileList):
  for filename in fileList:
    r = mdx.Reader()
    try:
      mdxModel = r.loadFile(filename)
      print u"\u2714 " + filename
    except mdx.MDXFileFormatError, e:
      errorString = e.__str__()
      print u"\u2717 " + errorString

testFiles(fileList)
