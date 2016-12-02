import random, argparse

parser = argparse.ArgumentParser(description='Randomly generate a list number')
parser.add_argument('-n', metavar = 'N', type=int, default=10)
parser.add_argument('-max', metavar = 'Max', type=int, default=20)
args = parser.parse_args()

print ( [random.randrange(args.max) for _ in range(args.n)] )