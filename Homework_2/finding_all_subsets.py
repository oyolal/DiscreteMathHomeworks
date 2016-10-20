def bit(x):
    for i in range(n+1):
        if (x & (1 << i)):
            print i+1,


n = int(raw_input())
for i in range(2**n):
    bit(i)
    print
