#!/home/fds/freeware/python26/bin/python

from random import randint
 
prefix = ['Ram', 'Nag', 'Har', 'Gyan', 'Karam', 'Mohan', 'Mah','Sur','Shiv', 'Nah', 'Dharam', 'Dhyan']
suffix = ['chand', 'das', 'charan', 'prasad', 'raj', 'esh' ]
 
for i in range(1,100):
    name = ''
    name = prefix[randint(0,len(prefix))-1] + suffix[randint(0,len(suffix))-1]
    print name
