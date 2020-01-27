'''
 Write a function which accepts the root of a tree, and returns a Linked List which contains the leaf nodes of the tree from left to right order.
Assumptions:

(*) Structure of the node of tree is as follows:
struct TreeNode
{
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};

(*) Don't allocate extra memory for Linked List, just let the right pointer of a leaf
node point to the next leaf node to form a linked list.

Example:
            10 
         /      \               
       20        100          
      /  \       / \             
    30    40    9   66

Output: 30 -> 40 -> 9 -> 66 
'''

class Node:  
      
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Function to Print all the leaf nodes  
# of Binary tree using two stacks  
def PrintLeafLeftToRight(root):  
  
    # Stack to store all the nodes  
    # of tree  
    s1 = []  
  
    # Stack to store all the 
    # leaf nodes  
    s2 = []  
  
    # Push the root node  
    s1.append(root)  
  
    while len(s1) != 0:  
        curr = s1.pop()  
  
        # If current node has a left child  
        # push it onto the first stack  
        if curr.left: 
            s1.append(curr.left)  
  
        # If current node has a right child  
        # push it onto the first stack  
        if curr.right:  
            s1.append(curr.right)  
  
        # If current node is a leaf node  
        # push it onto the second stack  
        elif not curr.left and not curr.right:  
            s2.append(curr)  
      
    # Print all the leaf nodes  
    while len(s2) != 0:  
        print(s2.pop().data, end = " ") 
      
# Driver code  
if __name__ == "__main__":  
  
    root = Node(10)  
    root.left = Node(20)  
    root.right = Node(100)  

    root.left.left = Node(30)
    root.left.right = Node(40) 

    root.right.left = Node(9)  
    root.right.right = Node(66)  
    
  
    PrintLeafLeftToRight(root) 