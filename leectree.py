# Leetcode Tree generation
import random, sys, argparse

# argc = len(sys.argv)
# argv = sys.argv

# if argc > 4:
#     print('Usage: leectree [ n [null_weight [max_val]] ]')
#     quit()
# 
# if argc > 1:
#     n = int(argv[1])
# if argc > 2:
#     null_weight = float(argv[2])
#     if null_weight < 0 or null_weight >= 1:
#         print('second argument should be between 0 and 1')
#         quit()
# if argc == 4:
#     max_val = int(argv[3])
parser = argparse.ArgumentParser(description='Randomly generate binary tree')
parser.add_argument('-n', metavar = 'N', type=int, default=10)
parser.add_argument('-max', metavar = 'Max', type=int, default=100)
parser.add_argument('-w', metavar = 'Null_Weight', type=float, default=0.2)
parser.add_argument('-sym', metavar = 'Null_Symbol', type=str, default='null')
args = parser.parse_args()

n = args.n
max_val = args.max
null_weight = args.w
null_symbol = args.sym

    
n_null = int(null_weight * n)
n_num = n - n_null
l = random.sample(range(max_val), n_num)
l[n_num:n_num] = [null_symbol] * n_null
random.shuffle(l)

print('[', end='')
for i in l:
    print(str(i) + ',', end='')
print('%c' % 8, end='') # delete the last comma
print(']')