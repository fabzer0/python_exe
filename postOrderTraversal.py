def postOrder(Tree):
    if Tree != None:
        postOrder(Tree.getLeftChild())
        postOrder(Tree.getRightChild())
        print(Tree.getRootVal()) #print comes at the end after the recursive calls since the root will be visited last
                  
