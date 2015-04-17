#!/home/fds/freeware/python26/bin/python
from random import randint

prefix = ['Amar', 'Aman', 'Param', 'Har', 'Gur', 'Bal']
suffix = ['deep', 'jeet', 'prit', 'jot', 'minder', 'mit']
surname = ['Singh', 'Kaur']

for i in range(1,10):
    name = ''
    name = prefix[randint(0,len(prefix))-1] + suffix[randint(0,len(suffix))-1] + ' '+ surname[randint(0,len(surname))-1]
    print name
