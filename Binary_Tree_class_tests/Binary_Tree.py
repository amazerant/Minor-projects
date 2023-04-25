#Class methods written by Pogorzelski Krystian https://github.com/KrystianPog and Mazerant Adam https://github.com/amazerant

import ctypes

class Tree:
    '''Tree'''
    pass

class BinaryTree(Tree):

    def __init__(self):
        """A constructor of an array"""
        self._size = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(self,c):
        """A way to make an array"""
        return (c*ctypes.py_object)()

    def _resize(self,c):
        """Changing the size of an array"""
        B = self._make_array(c)
        for k in range(self._capacity):
            if self._validate(k):
                B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def __len__(self):
        """returns numbers of elements in tree"""
        return self._size

    def __iter__(self):
        """a way to iterate"""
        for p in self.positions():
            yield self.element(p) 

    def root_index(self):
        """returns the index of root"""
        if self._size:
            return 0
        else:
            return None

    def root(self):
        """returns the value of root"""
        if self._size:
            return self._A[0]
        else:
            raise ValueError('tree has no root')

    def is_root(self, p):
        """checks if p is the root index"""
        if self._size:
            return p == 0
        else:
            raise ValueError('tree has no root')

    def parent_index(self, p):
        """returns the index of a parent"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if p == 0:
            raise ValueError('root has no parent')
        if p%2 == 0:
            return (p-2)//2
        else:
            return (p-1)//2

    def parent(self, p):
        """returns the value of parent"""
        return self._A[self.parent_index(p)]

    def children_index(self, p):
        """returns indices of children"""
        if self._validate(p):
            if self._validate(2*p+1):
                yield 2*p+1
            if self._validate(2*p+2):
                yield 2*p+2
        else:
            raise IndexError('invalid index')

    def num_children(self, p):
        """returns the number of children"""
        if self._validate(p):
            return self._validate(2*p+1) + self._validate(2*p+2)
        else:
            raise IndexError('invalid index')

    def children(self, p):
        """returns values of children"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self.num_children(p):
            return (self._A[c] for c in self.children_index(p))
        else:
            raise ValueError('node has no children')

    def is_leaf(self, p):
        """checks if a node is a leaf"""
        if not self._validate(p):
            return False
        if self._validate(2*p+1) or self._validate(2*p+2):
            return False
        else:
            return True

    def is_empty(self):
        """checks if a tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """returns the depth from an index"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent_index(p))

    def height(self, p=None):
        """returns the height of a tree"""
        if self.is_empty():
            return 0
        if p is None:
            p = self.root_index()
        return self._height2(p)

    def positions(self):
        """returns positions of indices in preorder form of a whole tree"""
        return self.preorder_pos() 

    def preorder_pos(self):
        """preorders the indeces of a whole tree"""
        if not self.is_empty():
            for p in self._subtree_preorder_pos(self.root_index()):
                yield p

    def preorder(self):
        """preorders the elemenets of a whole tree"""
        return str([self[position] for position in self.preorder_pos()])[1:-1]

    def postorder_pos(self):
        """postorders the indeces of a whole tree"""
        if not self.is_empty():
            for p in self._subtree_postorder_pos(self.root_index()):
                yield p
    
    def postorder(self):
        """postorders the elements of a whole tree"""
        return str([self[position] for position in self.postorder_pos()])[1:-1]

    def inorder_pos(self):
        """orders the indeces of a whole tree"""
        if not self.is_empty():
            for p in self._subtree_inorder_pos(self.root_index()):
                yield p

    def inorder(self):
        """orders the elements of a whole tree"""
        return str([self[position] for position in self.inorder_pos()])[1:-1]

    def traversal_pos(self):
        """traverses the indecies of a whole tree"""
        if not self.is_empty():
            for p in self._subtree_traversal_pos(self.root_index()):
                yield p

    def traversal(self):
        """traverses the elements of a whole tree"""
        return str([self[position] for position in self.traversal_pos()])[1:-1]

    def add(self,p, e):
        """adds a value e in position p"""
        if p == 0:
            parent = 0
        elif p%2 == 0:
            parent=(p-2)//2
        else:
            parent=(p-1)//2

        if self._validate(parent) or p==0:
            try:
                self._A[p]
                raise IndexError('position has a value')
            except ValueError:
                if self._capacity-1 <= p:
                    self._resize(2**(self.height()+2)-1)
                self._A[p]=e
                self._size+=1
        else:
            raise IndexError('invalid index')

    def get_left_child(self, p):
        """returns the value of a left child"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self._validate(2*p+1):
            return self.element(2*p+1)
        else:
            return None

    def get_right_child(self, p):
        """returns the value of a right child"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self._validate(2*p+2):
            return self.element(2*p+2)
        else:
            return None

    def sibling(self, p):
        """returns the value of a sibling of p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if p == 0:
            return None
        else:
            if self.element(p) == self.get_left_child(self.parent_index(p)):
                return self.get_right_child(self.parent_index(p))
            else:
                return self.get_left_child(self.parent_index(p))

    def element(self, p):
        """returns the value of index p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        return self._A[p]

    def __getitem__(self,p):
        """returns the value of index p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        return self._A[p]

    def has_left_child(self,p):
        """checks if index p has a left child"""
        if not self._validate(p):
            raise IndexError('invalid index')
        for index in self.children_index(p):
            if index%2 == 1:
                return True
        return False

    def has_right_child(self,p):
        """checks if index p has a right child"""
        if not self._validate(p):
            raise IndexError('invalid index')
        for index in self.children_index(p):
            if index%2 == 0:
                return True
        return False

    def get_left_child_pos(self,p):
        """returns the position of a left child of index p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        for index in self.children_index(p):
            if index%2 == 1:
                return index
        return None

    def get_right_child_pos(self,p):
        """returns the position of a right child of index p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        for index in self.children_index(p):
            if index%2 == 0:
                return index
        return None

    def pop(self, p):
        """removes a leaf and returns it's value"""
        if self.is_leaf(p):
            val = self._A[p]
            B = self._make_array(self._capacity)
            for k in range(self._capacity):
                if self._validate(k) and k!=p:
                    B[k] = self._A[k]
            self._A = B
            self._size-=1
            if self._capacity > 2**(self.height()+2)-1:
                    self._resize(2**(self.height()+2)-1)
            return val
        else:
            raise IndexError('cannot pop from not a leaf')

    def remove(self, p):
        """removes the branch begining with position p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self.has_left_child(p):
            self.remove(self.get_left_child_pos(p))
        if self.has_right_child(p):
            self.remove(self.get_right_child_pos(p))
        if self.is_leaf(p):
            self.pop(p)


    def _validate(self, p):
        """checks if index p has a value"""
        if type(p) is not int:
            raise ValueError("p must be 0 or natural number")
        if p < 0:
            raise ValueError("p must be 0 or natural number")
        try:
            self._A[p]
            if self.is_root(p):
                return True
            elif p%2 == 0:
                return self._validate((p-2)//2)
            else:
                return self._validate((p-1)//2)
        except(ValueError, IndexError):
            return False

    def _height1(self):
        """returns the longest way to root"""
        return max(self.depth(p) for p in range(self._capacity) if self.is_leaf(p))

    def _height2(self, p):
        """returns the longest way to a leaf from index p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children_index(p))

    def _subtree_preorder_pos(self, p):
        """preorders the indecies of a part of a tree"""
        if not self._validate(p):
            raise IndexError('invalid index')
        yield p
        for c in self.children_index(p):
            for other in self._subtree_preorder_pos(c):
                yield other

    def _subtree_postorder_pos(self, p):
        """postorders the indecies of a part of a tree"""
        if not self._validate(p):
            raise IndexError('invalid index')
        for c in self.children_index(p):
            for other in self._subtree_postorder_pos(c):
                yield other
        yield p

    def _subtree_inorder_pos(self, p):
        """orders the indecies of a part of a tree"""
        if self.has_left_child(p):
            for other in self._subtree_inorder_pos(self.get_left_child_pos(p)):
                yield other
        yield p
        if self.has_right_child(p):
            for other in self._subtree_inorder_pos(self.get_right_child_pos(p)):
                yield other

    def _subtree_traversal_pos(self, p, perfect=False):
        """traverses the indecies of a part of a tree, if full is True it asumes that the tree is perfect"""
        l=r=p
        for _ in range(self.height(p)+1):
            for i in range(l,r+1):
                if self._validate(i) or perfect:
                    yield i
            l,r = 2*l+1,2*r+2

    def _add_root(self, e):
        """adds the root"""
        if self._size:
            raise ValueError('root exists')
        self._resize(3)
        self._size = 1
        self._A[0] = e

    def _add_left(self, p, e):
        """adds a left child"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self._validate(2*p+1):
            raise ValueError('left child exists')
        if self._capacity-1 < 2*p+1:
            self._resize(2**(self.height()+2)-1)
        self._A[2*p+1] = e
        self._size += 1

    def _add_right(self, p, e):
        """adds a right child"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self._validate(2*p+2):
            raise ValueError('right child exists')
        if self._capacity-1 < 2*p+2:
            self._resize(2**(self.height()+2)-1)
        self._A[2*p+2] = e
        self._size += 1

    def set(self, p, e):
        """changes the value conected with index p for value e"""
        if self._validate(p):
            self._A[p] = e
        else:
            raise IndexError('invalid index')

    def _delete(self, p):
        """if index p has at most one child, it removes its value and places its subtree in place of it"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if self.num_children(p) == 2:
            raise ValueError('position has two children')
        if self.is_leaf(p):
            self.pop(p)
        else:
            indecies_1 = list(self._subtree_traversal_pos(p, perfect=True))
            indecies_2 = list(self._subtree_traversal_pos(next(self.children_index(p)), perfect=True))
            B = self._make_array(self._capacity)
            for k in range(self._capacity):
                if k not in indecies_1 and self._validate(k):
                    B[k] = self._A[k]
                if k < len(indecies_2):
                    if self._validate(indecies_2[k]):
                        B[indecies_1[k]] = self._A[indecies_2[k]]

            self._A = B
            self._size-=1
            if self._capacity > 2**(self.height()+2)-1:
                    self._resize(2**(self.height()+2)-1)

    def _attach(self, p, t1, t2):
        """adds tree t1 as left child, tree t2 as right child of position p"""
        if not self._validate(p):
            raise IndexError('invalid index')
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not issubclass(type(t1),Tree) or not issubclass(type(t2),Tree):
            raise TypeError('t1 and t2 must be object of subclass Tree')
        self._resize(2**(self.height()+max(t1.height(),t2.height())+2)-1)

        if t1._size == 1:
            self._add_left(p, t1.root())
            t1.pop(t1.root_index())
        if t2._size == 1:
            self._add_right(p, t2.root())
            t2.pop(t2.root_index())

        if not t1.is_empty():
            t3 = BinaryTree()
            t3._add_root(t1.root())
            t3._resize(t1._capacity)
            if t1.has_left_child(t1.root_index()):
                indecies_1 = t1._subtree_traversal_pos(t1.get_left_child_pos(t1.root_index()))
                for k in indecies_1:
                    t3._A[k] = t1._A[k]
                    t3._size+=1
            t3._delete(t3.root_index())

            t4 = BinaryTree()
            t4._add_root(t1.root())
            t4._resize(t1._capacity)
            if t1.has_right_child(t1.root_index()):
                indecies_2 = t1._subtree_traversal_pos(t1.get_right_child_pos(t1.root_index()))
                for k in indecies_2:
                    t4._A[k] = t1._A[k]
                    t4._size+=1
            t4._delete(t4.root_index())

            self._add_left(p, t1.root())
            self._attach(self.get_left_child_pos(p), t3, t4)

        if not t2.is_empty():
            t3 = BinaryTree()
            t3._add_root(t2.root())
            t3._resize(t2._capacity)
            if t2.has_left_child(t2.root_index()):
                indecies_1 = t2._subtree_traversal_pos(t2.get_left_child_pos(t2.root_index()))
                for k in indecies_1:
                    t3._A[k] = t2._A[k]
                    t3._size+=1
            t3._delete(t3.root_index())

            t4 = BinaryTree()
            t4._add_root(t2.root())
            t4._resize(t2._capacity)
            if t2.has_right_child(t2.root_index()):
                indecies_2 = t2._subtree_traversal_pos(t2.get_right_child_pos(t2.root_index()))
                for k in indecies_2:
                    t4._A[k] = t2._A[k]
                    t4._size+=1
            t4._delete(t4.root_index())

            self._add_right(p, t2.root())
            self._attach(self.get_right_child_pos(p), t3, t4)


    def __str__(self):
        """a way to represent the tree like a graphical representation"""
        if self.is_empty():
            return ''
        if self._size == 1:
            return str(self._A[self.root_index()])
        tree = []
        row = ''
        arrows = ''
        backslash = r'\ '.strip()
        a=1
        for h in range(self.height()+1):
            space_size = 2**(self.height()+3-h)-2**(self.height()+1-h)
            for p in range(2**h,2**(h+1)):
                if self._validate(p-1):
                    element = str(self.element(p-1))
                    if len(element) < space_size:
                        row += element.center(space_size)
                    else:
                        row += (element[:space_size-4]+'...').center()
                    if a%2==0:
                        left_pointer = ' /'.center(space_size)
                        arrows += left_pointer
                        a+=1
                    else:
                        right_pointer = backslash.center(space_size)
                        arrows += right_pointer[1:] + ' '
                        a+=1
                else:
                    row += ' '.center(space_size)
                    arrows += ' '.center(space_size)
                    a+=1

            tree.append(arrows)
            tree.append(row)
            row = ''
            arrows = ''

        value = ''
        for line in tree:
            if line != tree[0]:
                value+=f'{line.rstrip()}\n'
        return value
    

    def __repr__(self):
        """a way to represent the tree in a list containing tuples that have the position and value of a node in them"""
        sequence = []
        for position in self.positions():
            sequence.append((position,self[position]))
        return str(sorted(sequence))

if __name__ == "__main__":
    pass