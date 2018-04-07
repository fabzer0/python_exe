def inOrder(Tree):
    ''' if we perform a smple inorder traversal of a parse tree we get our original
        expression back without the parenthesis. The fn below modifies.
        The only modification we will make is print left parethesis before the recursive
        call to the left subtree, and print the right par after the recursive call to the right
        subtree'''
    if Tree:
        inOrder(Tree.getLeftChild())
        print(Tree.getRootVal()) # print comes at the middle since the root is visited after the left then to the right
        inOrder(Tree.getRightChild())

def print_expr(Tree):
    sVal = ''
    if Tree:
        sVal = '(' + print_expr(Tree.getLeftChild())
        sVal = sVal + str(Tree.getRootVal())
        sVal = sVal + print_expr(Tree.getRightChild()) + ')'

    return sVal
