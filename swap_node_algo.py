# basics_python
#conducted on binary tree


#!/bin/python3
from __future__ import print_function
import os
import sys

#to avoid runtime error-exceeding recusion limit for larger inputs
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self,data,step):
        self.info=data
        self.left=self.right=None
        self.level=step

def in_order(root,l1):
    if root:
        in_order(root.left,l1)

        l1.append(root.info)

        in_order(root.right,l1)

def swap_in_order(root, k, step):
    if root:
        
        swap_in_order(root.left,k,step+1)
        swap_in_order(root.right, k, step+1)

        if (step)%k==0 and root!=None:
            root.left, root.right= root.right, root.left




def swapNodes(indexes, queries):
    q=[]
    root=Node(1,1)
    q.append(root)
    for i in indexes:
        current=q.pop(0)
        left_node=Node(i[0],current.level+1)
        right_node=Node(i[1],current.level+1)
        if left_node.info!=-1:
            current.left=left_node
            q.append(left_node)
        if right_node.info!=-1:
            current.right=right_node
            q.append(right_node)
    result=[]
    for k in queries:
        l1=[]
        step=1
        swap_in_order(root,k,step)
        in_order(root, l1)
        result.append(l1)
    return result

#to print error in STDERR     
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    step=1

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    eprint(result)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
