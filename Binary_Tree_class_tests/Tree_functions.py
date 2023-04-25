#Functions written by Mazerant Adam https://github.com/amazerant

import Binary_Tree

def list_to_tree(sequence):
    """Creates tree from given sequence of tuples"""
    if type(sequence) not in (list,tuple):
        raise ValueError("Unable to create tree - wrong type of input")
    sequence = list(sequence)
    sequence.sort()
    if type(sequence[0]) not in (list,tuple) or sequence[0][0] != 0:
        raise ValueError("Unable to create tree - tree has no root")
    tree = Binary_Tree.BinaryTree()
    used_indicies = [0]
    tree._add_root(sequence[0][1])
    height = 0
    n = sequence[-1][0]
    while n != 0:
        height += 1
        if n%2 == 0:
            n = (n-2)/2
        else:
            n = (n-1)/2
    tree._resize(2**(height+2)-1)
    for element in sequence[1:]:
        if type(element) not in (list,tuple):
            raise ValueError("Unable to create tree - wrong type of input")
        if element[0] < 0 or type(element[0]) is not int:
            raise ValueError("Unable to create tree - index value must be 0 or natural number")
        if element[0] in used_indicies:
            raise ValueError("Unable to create tree - creating the same node twice")
        tree._A[element[0]] = element[1]
        if not tree._validate(element[0]):
            raise ValueError("Unable to create tree - index is invalid")
    return tree


def generate_random_tree(size,left_child_chance,right_child_chance):
    """Generates random tree of given size, with given chance of creating left and right children"""
    from random import random, choice
    if abs(left_child_chance + right_child_chance-1) > 10**6:
        raise ValueError("chances of creating leaves must add up to 1")
    if size < 0 or type(size) is not int:
        raise ValueError("size of tree must be 0 or natural number")
    if left_child_chance < 0 or left_child_chance > 1:
        raise ValueError("chance of creating left child must be in range [0;1]")
    if right_child_chance < 0 or right_child_chance > 1:
        raise ValueError("chance of creating right child must be in range [0;1]")
    tree = Binary_Tree.BinaryTree()
    if size == 0:
        return tree
    nodes = 1
    indices = [0]
    tree._add_root(f"{tree._size}")
    while nodes < size:
        index = choice(indices)
        if tree.num_children(index) == 2:
            indices.remove(index)
        else:
            if random() < 0.5:
                if tree.get_left_child(index) == None:
                    if left_child_chance >= random():
                        tree._add_left(index,f"{tree._size}")
                        nodes += 1
                        indices.append(2*index+1)
                        if nodes >= size:
                            return tree
                if tree.get_right_child(index) == None:
                    if right_child_chance >= random():
                        tree._add_right(index,f"{tree._size}")
                        nodes += 1
                        indices.append(2*index+2)
                        if nodes >= size:
                            return tree
            else:
                if tree.get_right_child(index) == None:
                    if right_child_chance >= random():
                        tree._add_right(index,f"{tree._size}")
                        nodes += 1
                        indices.append(2*index+2)
                        if nodes >= size:
                            return tree
                if tree.get_left_child(index) == None:
                    if left_child_chance >= random():
                        tree._add_left(index,f"{tree._size}")
                        nodes += 1
                        indices.append(2*index+1)
                        if nodes >= size:
                            return tree
    return tree


if __name__ == "__main__":
    pass