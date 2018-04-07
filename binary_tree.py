
from pythonds.trees.binaryTree import BinaryTree
from pythonds.basic.stack import Stack

class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def preOrder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preOrder()
        if self.right_child:
            self.right_child.preOrder()

    def postOrder(self):
        if self.left_child:
            self.left_child.postOrder()
        if self.right_child:
            self.right_child.postOrder()
        print(self.key)

    def inOrder(self):
        if self.left_child:
            self.left_child.inOrder()
        print(self.key)
        if self.right_child:
            self.right_child.inOrder()

    def build_parse_tree(fpexpr):
        fp_list = fpexpr.split()
        pstack = Stack()
        eTree = BinaryTree('')
        pstack.push(eTree)
        current_node = eTree

        for i in fp_list:
            if i == '(':
                current_node.insert_left('')
                pstack.push(current_node)
                current_node = current_node.get_left_child()
            elif i not in ['+', '-', '*', '/', ')']:
                current_node.set_root_val(int(i))
                parent = pstack.pop()
                current_node = parent
            elif i in ['+', '-', '*', '/']:
                current_node = set_root_val(i)
                current_node.insert_right('')
                pstack.push(current_node)
                current_node = current_node.get_right_child()
            elif i == ')':
                current_node = pstack.pop()
            else:
                raise ValueError
        return eTree

    def evaluate(build_parse_tree):
        opers = {'+':+,'-':-,'*':*,'/':/}

        leftC = build_parse_tree.get_left_child()
        rightC = build_parse_tree.get_right_child()

        if leftC and rightC:
            fn = opers[build_parse_tree.get_root_val()]
            return fn(evaluate(leftC), evaluate(rightC))

        else:
            return build_parse_tree.get_root_val()

    def postOrderEval(build_parse_tree):
        opers = {'+':+, '-':-, '*':*, '/':/}

        res1 = None
        res2 = None

        if build_parse_tree != None #or if build_parse_tree:
            res1 = postOrderEval(build_parse_tree.get_left_child())
            res2 = postOrderEval(build_parse_tree.get_right_child())

            if res1 and res2:
                return opers[build_parse_tree.get_root_val()](res1, res2)
            else:
                return build_parse_tree.get_root_val()
            
        


                
tree = BinaryTree('')
tree.set_root_value('+')
tree.insert_left(3)
t = tree.insert_right('*')
t.insert_left(4)
t.insert_right(5)

pt = build_parse_tree(tree)
print(pt.postOrderEval())



        
