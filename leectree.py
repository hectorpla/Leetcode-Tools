# Leetcode Tree generation
import random, sys

max_val = 100
null_weight = 0.1
n = 20

argc = len(sys.argv)
argv = sys.argv

if argc > 4:
    print('Usage: leectree [ n [null_weight [max_val]] ]')
    quit()

if argc > 1:
    n = int(argv[1])
if argc > 2:
    null_weight = float(argv[2])
    if null_weight < 0 or null_weight >= 1:
        print('second argument should be between 0 and 1')
        quit()
if argc == 4:
    max_val = int(argv[3])

    
n_null = int(null_weight * n)
n_num = n - n_null
l = random.sample(range(max_val), n_num)
l[n_num:n_num] = ['null'] * n_null
random.shuffle(l)

print('[', end='')
for i in l:
    print(str(i) + ',', end='')
print('%c' % 8, end='') # delete the last comma
print(']')