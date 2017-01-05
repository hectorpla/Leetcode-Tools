# generate a BST (displayed as Leetcode tree)
import random, sys, math, argparse

# MIN = 0
# MAX = 15

# argv = sys.argv
# argc = int(len(argv))
# # print(argc)
# if argc == 1:
#     pass
# elif argc == 3:
#     MIN = int(argv[1])
#     MAX = int(argv[2])
# else:
#     print('Usage: genBST [min max]')
#     quit()

parser = argparse.ArgumentParser(description='Randomly generate a list number')
parser.add_argument('-n', metavar = 'N', type=int, default=10)
parser.add_argument('-min', metavar = 'Min', type=int, default=0)
parser.add_argument('-max', metavar = 'Max', type=int, default=15)
parser.add_argument('-sym', metavar = 'Null_Symbol', type=str, default='null')
args = parser.parse_args()

MIN = args.min
MAX = args.max
null_sym = args.sym
# list that contain message of whether a number is assigned to a node
assigned = [False] * MAX

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def choose_from_unassigned(min, max):
    for i in range(5):
        temp = random.randrange(min, max)
        if assigned[temp]:
            continue
        assigned[temp] = True
        return temp
    return MIN - 1
        
def genTree(root, min, max):
    if root.val > min:
        left_val = choose_from_unassigned(min ,root.val);
        if left_val > MIN:                   
            root.left = TreeNode(left_val)
            genTree(root.left, min, root.val)
    
    if root.val + 1 < max:
        right_val = choose_from_unassigned(root.val + 1, max)
        if right_val > MIN:
            root.right = TreeNode(right_val)
            genTree(root.right, root.val, max)
        
def trav_by_level(root):
     q = []
     q.append(root)
     
     while ( len(q) ):
        node = q.pop(0)
        if ( node == None ):
            print(null_sym + ',', end='')
            continue
        print(str(node.val) + ',', end = '')
        q.append(node.left)
#         if ( node.right != None ):
        q.append(node.right) 
       
# execute
val = int( MIN / 2 + MAX / 2 )
root = TreeNode(val)
assigned[val] = True
genTree(root, MIN, MAX)

print('[', end = '')
trav_by_level(root)
print('%c' % 8, end='') # delete the last comma
print(']')


    
    