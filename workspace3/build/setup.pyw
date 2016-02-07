
# setup.py
from distutils.core import setup
import py2exe

import sys

sys.stdout = open('screen.txt','w',0)
sys.stderr = open('errors.txt','w',0)

setup(name='joy',
      version='3',
      author='krdr',
      data_files=[('WiFi_car\\scr', ['WiFi_car\\scr\\background2.png'])],
      windows=[{'script':'joy.py',
                'icon_resources':[(1,'C:\Python27\DLLs\py.ico')],
                }])

print "---Done---"
