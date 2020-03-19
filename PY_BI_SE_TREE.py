class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key
    def __str__(self):
        return s_p(self)

def insert(root, data):
    if root.val:
        if data < root.val:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        elif data > root.val:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)
    else:
        root.val = data
def s_p(root):
    if root==None:
        return ''
    else:
        return s_p(root.left)+' '+str(root.val)+' '+s_p(root.right)
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val,end= ' ')
        print_tree(root.right)
def crt_bst(l):
    root=Node(l[0])
    for i in l:
        insert(root,i)
    return root