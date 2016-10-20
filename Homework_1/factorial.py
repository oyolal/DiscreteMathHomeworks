factorial = [12]
factorial[0] = 1
for l in range(1,10):
    factorial.append(l*factorial[l-1])
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            a = factorial[i] + factorial[j] + factorial[k]
            if(100 * i + 10 * j + k) == a:
                print 100 * i + 10 * j + k
