#!/home/fds/freeware/python26/bin/python
from random import randint

prefix = ['Hag', 'Nag', 'Har', 'Kich', 'Hir', 'Sach', 'Shin']
vowel = ['a', 'i']
suffix = ['chan', 'kiri', 'mochi', 'muchi', 'muri', 'saki', 'shimo', 'shima']

for i in range(1,10):
    name = ''
    name = prefix[randint(0,len(prefix))-1] + vowel[randint(0,len(vowel))-1] + suffix[randint(0,len(suffix))-1]
    print name
