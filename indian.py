#!/home/fds/freeware/python26/bin/python

#Generate indian names randomly

from random import randint

prefix = ['b', 'l', 'm','n','s', 't']
vowel = ['a', 'i', 'o', 'u']
suffix = ['nu', 'ni']

for i in range(1,10):
    name = ''
    name = prefix[randint(0,len(prefix)-1)] + vowel[randint(0,len(vowel)-1)] + suffix[randint(0,len(suffix)-1)]
    print name
