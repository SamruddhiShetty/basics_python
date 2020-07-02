# basics_python

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def buildHash(root, dictionary,  hd):
    q=[]

    q.append(root)
    q.append(hd)

    while q:
        node=q.pop(0)
        hd=q.pop(0)

        if node.left:
            q.append(node.left)
            q.append(hd-1)
        if node.right:
            q.append(node.right)
            q.append(hd+1)

        dictionary.setdefault(hd, []).append(node.info)

def topView(root):
    dictionary={}
    hd=0
    buildHash(root, dictionary, hd)
    y=sorted(dictionary)
    for i in y:
        print(dictionary[i][0], end = " ")




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
