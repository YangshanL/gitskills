#!/usr/bin/python
import time

print('hello jenkins from python!')
file = r'/opt/jenkins/script.log'
with open(file,'a',encoding='utf8') as fi:
    fi.write(time.time())
