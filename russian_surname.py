#!/home/fds/freeware/python26/bin/python
from random import randint

prefix = ['Kursh', 'Vlad', 'Tymos', 'Malen', 'Sara', 'Frad', 'Yanuko']
suffix = ['chev', 'chikov', 'shenko', 'pova', 'pov', 'vich', 'tsev', 'dev', 'kov', 'kev' ]

for i in range(1,10):
    name = ''
    name = prefix[randint(0,len(prefix))-1] + suffix[randint(0,len(suffix))-1]
    print name
