from random import randint
b = set([])
c = set([2,3,5,7,11,13,17,19,23,29,31,37])
while(len(b) < 7):
    b.add(randint(1,41))

print b
