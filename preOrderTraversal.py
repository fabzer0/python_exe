def preOrder(Tree):

    '''This fn is external since its written outside tree class'''
    if Tree:
        print(Tree.getRootVal()) #print comes at the beginning before the recurseve calls since the root is visited first
        preOrder(Tree.getLeftChild())
        preOrder(Tree.getRightChild())
    
