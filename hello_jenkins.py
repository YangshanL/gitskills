#!/usr/bin/python
import time

print('hello jenkins from python!')
file = r'/opt/jenkins/script.log'
with open(file,'a') as fi:
    fi.write(time.time())
