import random, argparse

parser = argparse.ArgumentParser(description='Randomly generate a list number')
parser.add_argument('-n', metavar = 'N', type=int, default=10)
parser.add_argument('-max', metavar = 'Max', type=int, default=20)
parser.add_argument('-s', default=False, action='store_true')
args = parser.parse_args()

list = [random.randrange(args.max) for _ in range(args.n)]
if args.s:
    list.sort()
print ( list )