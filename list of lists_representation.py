def binary_tree(r):
    return [r, [], []]

def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])

    return root

def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])

    return root

def insert_inner_left(parent, new_branch):
    t = parent.pop(1)
    if len(t) > 1:
        parent.insert(1, [new_branch, t, []])
    else:
        parent.insert(1, [new_branch, [], []])
        
    return parent

print(insert_left(binary_tree('documents'), 'school'))
print(insert_right(binary_tree('documents'), 'home'))
print(insert_inner_left(insert_left(binary_tree('documents'), 'class_work'), 'school'))

