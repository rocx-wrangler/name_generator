#!/home/fds/freeware/python26/bin/python
from random import randint

prefix = ['Kud', 'Kond', 'Gud', 'Gol', 'Chil', 'Yed', 'Bop']
vowel = ['a', 'i', 'o', 'u']
suffix = ['parthy', 'palli', 'lla', 'llu', 'lli', 'ppi', 'ppu', 'lla', 'pudi']

print "Telugu Surnames only..."
for i in range(1,10):
    name = ''
    name = prefix[randint(0,len(prefix))-1] + vowel[randint(0,len(vowel))-1] + suffix[randint(0,len(suffix))-1]
    print name
