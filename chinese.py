#!/home/fds/freeware/python26/bin/python
#generate Chinese names randomly

from random import randint

vowel = ['a', 'i', 'o', 'u']
alpha = ['g', 'h', 'j', 'l', 'm', 'n', 'q', 'w', 'x', 'y', 'z']
suffix = ['ng', 'zhou', 'ping', 'iang', 'eng', 'hua', 'ing']
for i in range(1,10):
    name = ''
    name = alpha[randint(0,len(alpha)-1)]
    if name == 'z':
        name = name+ 'h'
    name = name + vowel[randint(0,len(vowel)-1)] + suffix[randint(0,len(suffix)-1)]

    print name
