#!/home/fds/freeware/python26/bin/python
from random import randint

prefix = ['Ram', 'Nag', 'Har', 'Gyan', 'Karam', 'Mohan', 'Gan','Kam', 'Sur','Shiv', 'Dharam', 'Dhyan']
suffix = ['chand', 'das', 'charan', 'prasad', 'raj', 'esh' ]

for i in range(1,10):
    name = ''
    name = prefix[randint(0,len(prefix))-1] + suffix[randint(0,len(suffix))-1]
    print name
