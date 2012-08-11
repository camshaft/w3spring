#!/usr/bin/python
# -*- coding: utf-8 -*-

import blp

import fnmatch
import os

assets = './../../assets/'
out = './test-images/'

fileList = []
for root, dirnames, filenames in os.walk(assets):
  for filename in fnmatch.filter(filenames, '*.blp'):
      path = os.path.relpath(os.path.join(root, filename),assets)
      fileList.append(path)

def testFiles(fileList):
  for filename in fileList:
    relPath = os.path.join(assets, filename)
    try:
      outName = out+filename.replace('.blp','.jpg')
      try:
        os.makedirs(os.path.dirname(outName))
      except Exception, e:
        pass
      blp.BLP(relPath).save(outName)
      print u"\u2714 " + filename
    except ValueError, e:
      errorString = e.__str__()
      print u"\u2717 " + errorString

testFiles(fileList)
