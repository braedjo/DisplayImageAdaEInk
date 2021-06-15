import os
import time
from distutils.dir_util import copy_tree

yos = os.listdir("queued")

while True:
  copy_tree("queued/", "active/")
  for shid in yos:
    os.rename("active/{}".format(shid), "CurDis.png")
    print('Image Swapped')
    time.sleep(5)