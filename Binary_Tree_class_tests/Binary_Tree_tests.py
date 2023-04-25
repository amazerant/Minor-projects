#tests written by Mazerant Adam https://github.com/amazerant

from Binary_Tree import BinaryTree
import pytest

def test_tree_type():
    tree = BinaryTree()
    assert type(tree) is BinaryTree

def test_len():
    tree = BinaryTree()
    assert len(tree) == 0, f"Empty tree has length 0, returned {len(tree)}"
    tree._add_root("root")
    assert len(tree) == 1, f"Tree with only root has length 1, returned {len(tree)}"

def test_root_index():
    tree = BinaryTree()
    assert tree.root_index() == None, f"Empty tree doesn't have root, got {tree.root_index()}"
    tree._add_root("root")
    assert tree.root_index() == 0, f"Root of a tree has index 0, got {tree.root_index()}"

def test_root():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree.root()
    assert 'tree has no root' == str(e.value), f"Error message should say 'tree has no root', says {str(e.value)} instead"
    assert e.type == ValueError, f"Type of error should be ValueError, raises {e.type} instead"
    tree._add_root('root')
    assert tree.root() == 'root', f"Expected to return 'root', returned {tree.root()} instead"

def test_is_root():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree.is_root(0)
    assert 'tree has no root' == str(e.value), f"Error message should say 'tree has no root', says {str(e.value)} instead"
    assert e.type == ValueError, f"Type of error should be ValueError, raises {e.type} instead"
    tree._add_root("root")
    assert tree.is_root(0) == True, f"Index of a root is 0, returned {tree.is_root(0)} instead of True"
    assert tree.is_root(1) == False, f"{1} is not a proper index of a root, returned {tree.is_root(1)} instead of False"

def test_parent_index():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree.parent_index(0)
    assert "invalid index" == str(e.value), f"Error message should say 'invalid index', says {str(e.valie)} instead"
    assert IndexError == e.type, f"Error type should be InvalidIndex, raises {e.type} instead"
    tree._add_root("root")
    with pytest.raises(Exception) as e:
        tree.parent_index(0)
    assert 'root has no parent' == str(e.value), f"Error message should say 'root has no parent', says {str(e.value)} instead"
    assert e.type == ValueError, f"Type of error should be ValueError, raises {e.type} instead"
    tree._add_left(0, "left_child_1")
    assert tree.parent_index(1) == 0, f"Parent index should be 0, returned {tree.parent_index(0)} instead"
    tree._add_left(1, "left_child_2")
    assert tree.parent_index(3) == 1, f"Parent index should be 1, returned {tree.parent_index(0)} instead"
    with pytest.raises(Exception) as e:
        tree.parent(6)
    assert "invalid index" == str(e.value), f"Error message should say 'invalid index', says {str(e.value)} instead"
    assert e.type == IndexError, f"Type of error should be IndexError, raises {e.type} instead"

def test_parent():
    tree = BinaryTree()
    tree._add_root("root")
    tree._add_left(0,"left_child")
    with pytest.raises(Exception) as e:
        tree.parent(0)
    assert 'root has no parent' == str(e.value), f"Error message should say 'root has no parent', says {str(e.value)} instead"
    assert e.type == ValueError, f"Type of error should be ValueError, raises {e.type} instead"
    assert tree.parent(1) == "root", f"Should return 'root', got {tree.parent(1)} instead"

def test_children_index():
    tree = BinaryTree()
    tree._add_root("root")
    assert [] == list(tree.children_index(0)), f"This root has no children, instead got those indices {list(tree.children_index(0))}"
    tree._add_left(0, "left_child1")
    assert [1] == list(tree.children_index(0)), f"This root has only left child, instead got those indices {list(tree.children_index(0))}"
    tree._add_right(0, "right_child1")
    assert [1,2] == list(tree.children_index(0)), f"This root has both children, got indices {list(tree.children_index(0))} instead of [1,2]"
    tree._add_left(1,"left_child2")
    tree._add_right(1,"left_right2")
    assert [3,4] == list(tree.children_index(1)), f"Children of node 1 have indices [3,4], got indces {list(tree.children_index(1))} instead"
    tree._add_left(2,"left_child3")
    tree._add_right(2,"left_right3")
    assert [5,6] == list(tree.children_index(2)), f"Children of node 2 have indices [5,6], got indices {list(tree.children_index(2))} instead"

def test_num_children():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.num_children(0) == 0, f"This root has no children, returned {tree.num_children(0)} instead"
    tree._add_left(0,"left_child1")
    assert tree.num_children(0) == 1, f"This root has one child, returned {tree.num_children(0)} instead"
    tree._add_right(0,"right_child1")
    assert tree.num_children(0) == 2, f"This root has both children, returned {tree.num_children(0)} instead"

def test_children():
    tree = BinaryTree()
    tree._add_root("root")
    with pytest.raises(Exception) as e:
        tree.children(0)
    assert "node has no children" == str(e.value), f"Error message should say 'node has no children', says {str(e.value)}"
    assert e.type == ValueError, f"Type of error should be ValueError, raises {e.type} instead"
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    assert ["left_child1","right_child1"] == list(tree.children(0)), f"Children of this root have values: 'left_child1' and 'right_child1', returned {list(tree.children(0))} instead"
    assert ["left_child2"] == list(tree.children(1)), f"Child of node 1 has value: 'left_child2', returned {list(tree.children(1))} instead"

def test_is_leaf():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.is_leaf(0) == True, f"This root is also a leaf, returned {tree.is_leaf(0)} instead of True"
    tree._add_left(0,"left_child1")
    assert tree.is_leaf(0) == False, f"This root is not a leaf, returned {tree.is_leaf(0)} instead of False"
    assert tree.is_leaf(1) == True, f"This node is a leaf, returned {tree.is_leaf(1)} instead of True"

def test_is_empty():
    tree = BinaryTree()
    assert tree.is_empty() == True, f"This tree is empty, returned {tree.is_empty()} instead of True"
    tree._add_root("root")
    assert tree.is_empty() == False, f"This tree is not empty, returned {tree.is_empty()} instead of False"

def test_depth():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree.depth(0)
    assert "tree has no root" == str(e.value), f"Error message should say 'tree has no root', says {str(e.value)} instead"
    assert e.type == ValueError, f"Type of error should be ValueError, raises {e.type} instead"
    tree._add_root("root")
    assert tree.depth(0) == 0, f"Depth of root should be 0, returns {tree.depth(0)} instead"
    with pytest.raises(Exception) as e:
        tree.depth(1)
    assert "invalid index" == str(e.value), f"Error message should say 'invalid index', says {str(e.value)} instead"
    assert e.type == IndexError, f"Type of error should be IndexError, raises {e.type} instead"

def test_height():
    tree = BinaryTree()
    assert tree.height() == 0, f"Empty tree has height 0, returns {tree.height()} instead"
    tree._add_root("root")
    assert tree.height() == 0, f"Root alone has height 0, returns {tree.height()} instead"
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    assert tree.height() == 1, f"Tree has height 1, returns {tree.height()} instead"
    tree._add_left(1,"left_child2")
    tree._add_left(3,"left_child3")
    assert tree.height() == 3, f"Tree has height 3, returns {tree.height()} instead"

def test_positions():
    tree = BinaryTree()
    assert list(tree.positions()) == [], f"Empty tree has no positions, returns {list(tree.positions())} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert [0,1,3,7,2,5,6] == list(tree.positions()), f"Preorder of positions of this tree are [0,1,3,7,2,5,6], returns {list(tree.positions())} instead"

def test_preorder_pos():
    tree = BinaryTree()
    assert list(tree.preorder_pos()) == [], f"Empty tree has no positions, returns {list(tree.preorder_pos())} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert [0,1,3,7,2,5,6] == list(tree.preorder_pos()), f"Preorder of positions of this tree are [0,1,3,7,2,5,6], returns {list(tree.preorder_pos())} instead"

def test_preorder():
    tree = BinaryTree()
    assert tree.preorder() == '', f"Empty tree has no positions, returns {tree.preorder()} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert tree.preorder() == "'root', 'left_child1', 'left_child2', 'left_child4', 'right_child1', 'left_child3', 'right_child2'",\
        f"Tree elements in preorder are 'root', 'left_child1', 'left_child2', 'left_child4', 'right_child1', 'left_child3', 'right_child2',\
        returns {tree.preorder()} instead"

def test_postorder_pos():
    tree = BinaryTree()
    assert list(tree.preorder_pos()) == [], f"Empty tree has no positions, returns {list(tree.postorder_pos())} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert [7,3,1,5,6,2,0] == list(tree.postorder_pos()), f"Preorder of positions of this tree are [7,3,1,5,6,2,0], returns {list(tree.postorder_pos())} instead"

def test_postorder():
    tree = BinaryTree()
    assert tree.postorder() == '', f"Empty tree has no positions, returns {tree.postorder()} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert tree.postorder() == "'left_child4', 'left_child2', 'left_child1', 'left_child3', 'right_child2', 'right_child1', 'root'",\
        f"Tree elements in preorder are 'left_child4', 'left_child2', 'left_child1', 'left_child3', 'right_child2', 'right_child1', 'root',\
            returns {tree.postorder()} instead"

def test_inorder_pos():
    tree = BinaryTree()
    assert list(tree.inorder_pos()) == [], f"Empty tree has no positions, returns {list(tree.inorder_pos())} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert [7,3,1,0,5,2,6] == list(tree.inorder_pos()), f"Preorder of positions of this tree are [7,3,1,0,5,2,6], returns {list(tree.inorder_pos())} instead"

def test_inorder():
    tree = BinaryTree()
    assert tree.inorder() == '', f"Empty tree has no positions, returns {tree.inorder()} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert tree.inorder() == "'left_child4', 'left_child2', 'left_child1', 'root', 'left_child3', 'right_child1', 'right_child2'",\
        f"Tree elements in preorder are 'left_child4', 'left_child2', 'left_child1', 'root', 'left_child3', 'right_child1', 'right_child2',\
            returns {tree.inorder()} instead"

def test_traversal_pos():
    tree = BinaryTree()
    assert list(tree.traversal_pos()) == [], f"Empty tree has no positions, returns {list(tree.traversal_pos())} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert [0,1,2,3,5,6,7] == list(tree.traversal_pos()), f"Preorder of positions of this tree are [0,1,2,3,5,6,7], returns {list(tree.traversal_pos())} instead"

def test_traversal():
    tree = BinaryTree()
    assert tree.traversal() == '', f"Empty tree has no positions, returns {tree.traversal()} instead of []"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    assert tree.traversal() == "'root', 'left_child1', 'right_child1', 'left_child2', 'left_child3', 'right_child2', 'left_child4'",\
        f"Tree elements in preorder are 'root', 'left_child1', 'right_child1', 'left_child2', 'left_child3', 'right_child2', 'left_child4',\
            returns {tree.traversal()} instead"

def test_get_left_child():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.get_left_child(0) == None, f"Root has no left child, returns {tree.get_left_child(0)} instead of None"
    tree._add_left(0,"left_child1")
    assert tree.get_left_child(0) == 'left_child1', f"Value of left child of root is 'left_child1', returns {tree.get_left_child(0)} instead"

def test_get_right_child():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.get_right_child(0) == None, f"Root has no right child, returns {tree.get_right_child(0)} instead of None"
    tree._add_right(0,"right_child1")
    assert tree.get_right_child(0) == 'right_child1', f"Value of right child of root is 'right_child1', returns {tree.get_right_child(0)} instead"

def test_sibling():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.sibling(0) == None, f"Root has no sibling, returns {tree.sibling(0)} instead of None"
    tree._add_left(0,"left_child1")
    assert tree.sibling(1) == None, f"Node 1 has no sibling, returns {tree.sibling(1)} instead of None"
    tree._add_right(0,"right_child1")
    assert tree.sibling(1) == "right_child1", f"Sibling of node 1 has value 'right_child1', returns {tree.sibling(1)} instead"
    assert tree.sibling(2) == "left_child1", f"Sibling of node 2 has value 'left_child1', returns {tree.sibling(2)} instead"

def test_element():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.element(0) == "root", f"Root has value 'root', returns {tree.elemenet(0)} instead"
    tree._add_left(0,"left_child1")
    assert tree.element(1) == "left_child1", f"Node 1 has value 'left_child1', returns {tree.elemenet(1)} instead"

def test_getitem():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree[0] == "root", f"Root has value 'root', returns {tree[0]} instead"
    tree._add_left(0,"left_child1")
    assert tree[1] == "left_child1", f"Node 1 has value 'left_child1', returns {tree[1]} instead"

def test_validate():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree._validate(-5)
    assert "p must be 0 or natural number" == str(e.value), f"Error message should say 'p must be 0 or natural number', says {str(e.value)} instead"
    assert ValueError == e.type, f"Error type should be ValueError, raises {e.type} instead"
    with pytest.raises(Exception) as e:
        tree._validate(0.5)
    assert "p must be 0 or natural number" == str(e.value), f"Error message should say 'p must be 0 or natural number', says {str(e.value)} instead"
    assert ValueError == e.type, f"Error type should be ValueError, raises {e.type} instead"
    assert not tree._validate(0), f"Root doesn't exist, returs {tree._validate(0)} instead of False"
    tree._add_root("root")
    assert tree._validate(0), f"Root exists, returs {tree._validate(0)} instead of True"

def test_height1():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree._height1() == 0, f"Longest way from root to root has length 0, returns {tree._height1()} instead"
    tree._add_left(0,"left_child1")
    assert tree._height1() == 1, f"Longest way to root has length 1, returns {tree._height1()} instead"
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_right(1,"right_child2")
    tree._add_left(3,"left_child3")
    tree._add_right(3,"right_child3")
    tree._add_left(7,"left_child4")
    assert tree._height1() == 4, f"Longest way to root has length 4, returns {tree._height1()} instead"

def test_height2():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree._height2(0) == 0, f"Longest way to leaf is 0, returns {tree._height2(0)} instead"
    tree._add_left(0,"left_child1")
    assert tree._height2(0) == 1, f"Longest way to leaf is 0, returns {tree._height2(0)} instead"
    assert tree._height2(1) == 0, f"Longest way to leaf is 1, returns {tree._height2(1)} instead"
    tree._add_left(1,"left_child2")
    tree._add_right(1,"right_child1")
    tree._add_left(3,"left_child3")
    tree._add_right(3,"right_child2")
    tree._add_right(8,"right_child3")
    tree._add_left(18,"left_child4")
    assert tree._height2(0) == 5, f"Longest way to leaf is 4, returns {tree._height2(0)} instead"

def test_subtree_preorder_pos():
    tree = BinaryTree()
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    tree._add_right(1,"right_child4")
    assert list(tree.preorder_pos()) == list(tree._subtree_preorder_pos(0)), f"preorder_pos and _subtree_preorder_pos from index 0 should be equal,\
        returns False instead"
    assert [1,3,7,4] == list(tree._subtree_preorder_pos(1)), f"_subtree_preorder_pos from index 1 is [1,3,7,4],\
        returns {list(tree._subtree_preorder_pos(1))} instead"

def test_subtree_postorder_pos():
    tree = BinaryTree()
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    tree._add_right(1,"right_child4")
    assert list(tree.postorder_pos()) == list(tree._subtree_postorder_pos(0)), f"postorder_pos and _subtree_postorder_pos from index 0 should be equal,\
        returns False instead"
    assert [7,3,4,1] == list(tree._subtree_postorder_pos(1)), f"_subtree_postorder_pos from index 1 is [7,3,4,1],\
        returns {list(tree._subtree_postorder_pos(1))} instead"

def test_subtree_traversal_pos():
    tree = BinaryTree()
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    tree._add_right(1,"right_child4")
    assert list(tree.traversal_pos()) == list(tree._subtree_traversal_pos(0)), f"traversal_pos and _subtree_traversal_pos from index 0 should be equal,\
        returns False instead"
    assert [1,3,4,7] == list(tree._subtree_traversal_pos(1)), f"_subtree_traversal_pos from index 1 is [1,3,4,7],\
        returns {list(tree._subtree_traversal_pos(1))} instead"

def test_subtree_inorder_pos():
    tree = BinaryTree()
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    tree._add_right(1,"right_child4")
    assert list(tree.inorder_pos()) == list(tree._subtree_inorder_pos(0)), f"inorder_pos and _subtree_inorder_pos from index 0 should be equal,\
        returns False instead"
    assert [7,3,1,4] == list(tree._subtree_inorder_pos(1)), f"_subtree_inorder_pos from index 1 is [7,3,1,4],\
        returns {list(tree._subtree_inorder_pos(1))} instead"

def test_add_root():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.root() == "root", f"Root has value 'root', returns {tree.root()} instead"
    with pytest.raises(Exception) as e:
        tree._add_root("second root")
    assert "root exists" == str(e.value), f"Error message should say 'root exists', says {str(e.value)} instead"
    assert e.type == ValueError, f"Error type should be ValueError, raises {e.type} instead"

def test_add_left():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree._add_left(0, "left_child_1")
    assert "invalid index" == str(e.value), f"Error message should say 'invalid index', says {str(e.value)} instead"
    assert e.type == IndexError, f"Error type should be IndexError, raises {e.type} instead"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    assert 1 == tree.num_children(0), f"Root has only one child, returns {tree.num_children(0)} instead"
    assert [1] == list(tree.children_index(0)), f"Root has only left child with index 1, returns {list(tree.children_index(0))} instead"
    assert ["left_child1"] == list(tree.children(0)), f"Left child has value 'left_child1', returns {list(tree.children(0))} instead"
    with pytest.raises(Exception) as e:
        tree._add_left(0,"left_child2")
    assert "left child exists" == str(e.value), f"Error message should say 'left child exists', says {str(e.value)} instead"
    assert e.type == ValueError, f"Error type should be ValueError, raises {e.type} instead"

def test_add_right():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree._add_right(0, "right_child_1")
    assert "invalid index" == str(e.value), f"Error message should say 'invalid index', says {str(e.value)} instead"
    assert e.type == IndexError, f"Error type should be IndexError, raises {e.type} instead"
    tree._add_root("root")
    tree._add_right(0,"right_child1")
    assert 1 == tree.num_children(0), f"Root has only one child, returns {tree.num_children(0)} instead"
    assert [2] == list(tree.children_index(0)), f"Root has only right child with index 2, returns {list(tree.children_index(0))} instead"
    assert ["right_child1"] == list(tree.children(0)), f"Right child has value 'right_child1', returns {list(tree.children(0))} instead"
    with pytest.raises(Exception) as e:
        tree._add_right(0,"right_child2")
    assert "right child exists" == str(e.value), f"Error message should say 'right child exists', says {str(e.value)} instead"
    assert e.type == ValueError, f"Error type should be ValueError, raises {e.type} instead"

def test_set():
    tree = BinaryTree()
    with pytest.raises(Exception) as e:
        tree.set(0,"set")
    assert 'invalid index' == str(e.value), f"Error message should say 'invalid index', says {str(e.value)} instead"
    assert IndexError == e.type, f"Error type should be IndexError, raises {e.type} instead"
    tree._add_root("root")
    tree.set(0,"root_set")
    assert "root_set" == tree[0], f"Root value should be 'root_set', returns {tree[0]} instead"
    tree._add_left(0,"left_child1")
    tree.set(1,"left_child1_set")
    assert "left_child1_set" == tree[1], f"Node 1 value should be 'left_child1_set', returns {tree[1]} instead"

def test_add():
    tree = BinaryTree()
    tree.add(0,"root")
    assert tree[0] == "root", f"Value of node 0 should be 'root', set {tree[0]} instead"
    with pytest.raises(Exception) as e:
        tree.add(0,"second_root")
    assert "position has a value" == str(e.value), f"Error message should say 'position has a value', says {str(e.value)} instead"
    assert IndexError == e.type, f"Error type should be IndexError, raises {e.type} instead"
    tree.add(1,"left_child_1")
    assert tree[1] == "left_child_1", f"Value of node 0 should be 'left_child_1', set {tree[1]} instead"

def test_pop():
    tree = BinaryTree()
    tree._add_root("root")
    val = tree.pop(0)
    assert val == "root", f"Node 0 had value 'root', returns {val} instead"
    assert tree.is_empty() == True, f"After removing root tree should be empty, returns {tree.is_empty()} instead of True"

def test_remove():
    tree = BinaryTree()
    tree._add_root("root")
    tree.remove(0)
    assert tree.is_empty() == True, f"After removing root tree should be empty, returns {tree.is_empty()} instead"
    tree = BinaryTree()
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    tree._add_left(1,"left_child2")
    tree._add_left(2,"left_child3")
    tree._add_right(2,"right_child2")
    tree._add_left(3,"left_child4")
    tree._add_right(1,"right_child4")
    tree.remove(1)
    assert [0,5,2,6] == list(tree.inorder_pos()), f"After removing from node 1, positions of tree should be [0,5,2,6],\
        returns {list(tree.inorder_pos())} instead"

def test_has_left_child():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.has_left_child(0) == False, f"Tree doesn't have a left child, returned {tree.has_left_child(0)} instead of False"
    tree._add_left(0,"left_child_1")
    assert tree.has_left_child(0) == True, f"Tree has a left child, returned {tree.has_left_child(0)} instead of True"

def test_has_right_child():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.has_right_child(0) == False, f"Node 0 doesn't have a right child, returned {tree.has_right_child(0)} instead of False"
    tree._add_right(0,"right_child_1")
    assert tree.has_right_child(0) == True, f"Node 0 has a right child, returned {tree.has_right_child(0)} instead of True"

def test_get_left_child_pos():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.get_left_child_pos(0) == None, f"Node 0 doesn't have a left child, returned {tree.get_left_child_pos(0)} instead of None"
    tree._add_left(0,"left_child_1")
    assert tree.get_left_child_pos(0) == 1, f"Node 0 has a left child with index 1, returned {tree.get_right_child_pos(0)} instead"

def test_get_right_child_pos():
    tree = BinaryTree()
    tree._add_root("root")
    assert tree.get_right_child_pos(0) == None, f"Node 0 doesn't have a left child, returned {tree.get_left_child_pos(0)} instead of None"
    tree._add_left(0,"right_child_1")
    assert tree.get_right_child_pos(0) == None, f"Node 0 has a right child with index 1, returned {tree.get_right_child_pos(0)} instead"

def test_attach():
    tree1 = BinaryTree()
    tree1._add_root("root")
    tree2 = BinaryTree()
    tree3 = BinaryTree()
    tree1._attach(0,tree2,tree3)
    assert len(tree1) == 1, f"tree2 and tree3 have length 0, so len(tree1) should be 1, returns {len(tree1)} instead"
    tree2._add_root("root2")
    tree3._add_root("root3")
    tree1._attach(0,tree2,tree3)
    assert len(tree1) == 3, f"tree2 and tree3 have length 1, so len(tree1) should be 1, returns {len(tree1)} instead"
    assert list(tree1.positions()) == [0,1,2], f"tree1 positions should be [0,1,2]"

def test_delete():
    tree = BinaryTree()
    tree._add_root("root")
    tree._delete(0)
    assert tree.is_empty() == True, f"After deleating root this tree should be empty, returns {tree.is_empty()} instead"
    tree._add_root("root")
    tree._add_left(0,"left_child1")
    tree._add_right(0,"right_child1")
    with pytest.raises(Exception) as e:
        tree._delete(0)
    assert "position has two children" == str(e.value), f"Error message should say 'position has two children', says {str(e.value)} instead"
    assert ValueError == e.type, f"Error type should be ValueError, raises {e.type} instead"
