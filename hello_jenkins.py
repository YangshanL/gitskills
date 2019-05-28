#!/usr/bin/python
import time

print('hello jenkins from python!')
file = r'/opt/jenkins_data/script.log'
with open(file,'a') as fi:
    fi.write(str(time.time()))
