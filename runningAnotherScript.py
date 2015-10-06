#!/usr/bin/env python
from os import system
from time import sleep
from datetime import datetime

#os.system("gnome-terminal --disable-factory")
#os.system("gnome-terminal -e {command}")
print(datetime.now(),"-+- Starting")
system('python eee.py')
print(datetime.now(),"-+- Crash")
