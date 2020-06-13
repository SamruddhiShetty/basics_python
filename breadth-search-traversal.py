# basics_python
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        l1=[]
        l1.append(root)
        while len(l1)!=0:
            if l1[0].left:
                l1.append(l1[0].left)
            if l1[0].right:
                l1.append(l1[0].right)
            print(l1[0].data, end=" ")
            l1.remove(l1[0])


        
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
