"""
Tree
----

This file contains the tree data structure that will be used for interacting
with our coloured nodes.
The tree contains a "root" node, which is the topmost node of the tree.
It is interconnected through children and finally ends at external nodes ending
at the leaves.

*** Assignment Notes ***

This is the main file that will be tested, you must implement the related
functions with a TODO annotated.

Your task is to implement these methods.
"""

from node import Node
from colours import Colour
from typing import Tuple, List


class Tree:
    """
    Tree Class
    ----------

    Contains the data structure of a tree, where each node of the tree has a
    parent and children.
    If a node has no parent, it is considered the "root" of the tree.
    If a node has zero (0) children, it is a leaf (or is "external").

    Each node in the tree has the type `Node`, which is defined in `node.py`.

    ====== Functions ======

    - __init__ : Sets up the tree with a specified root.
    - put(node, child) : Adds the `child` to the `node`.
    - swap(subtree_a, subtree_b) : Swaps the position of the subtrees.
    - is_coloured_to_depth_k(node, colour, k) : Checks that the subtree rooted
        at `node` has the same colour until `k` levels deep.
    - is_colour_until(start_node, colour_a, colour_b): Checks that the subtree
        rooted at `start_node` has `colour_a` for all nodes in all paths until
        `colour_b`. E.g. (if colour_a is red, and colour_b is green, then all
        paths must have nodes that are Green until reaching a red.)

    == Things to note ==

    1. Every node given as an argument WILL be in the tree, you do not have to
        check whether it exists in the tree.
    2. Every node will be initialised with a parent (unless it is the root node
        of the tree).
    3. The ordering of the children does not matter.
    """

    def __init__(self, root: Node) -> None:
        """
        Initialises the tree with a root of type `Node` from `node.py`

        :param root: The root node of our tree.
        """

        self.root = root

    def update_node_colour(self, n: Node, new_colour: Colour) -> None:
        """
        Update the colour of a node.

        :param n: The node to change the colour of.
        :param new_colour: The new colour to change to.
        """
        # Call update_colour() on the node
        # TODO implement me please.
        if new_colour == None:
            return
        if Node == None:
            return
        n.update_colour(new_colour)
            

    def put(self, parent: Node, child: Node) -> None:
        """
        Inserts a node into the tree.
        Adds `child` to `parent`.

        :param parent: The parent node currently in the tree.
        :param child: The child to add to the tree.
        """
        # TODO implement me please.
        if child == None:
            return
        if parent == None:
            return
        parent.add_child(child)



    def rm(self, child: Node) -> None:
        """
        Removes child from parent.

        :param child: The child node to remove.
        """
        # TODO implement me please.
        if child == None:
            return
            
        current = self.root
        self.f(current, child)

    def f( self, node, child):
        if child in node.children:
            node.remove_child(child)
        else:
            for i in node.children:
                self.f(i,child)


    def swap(self, subtree_a: Node, subtree_b: Node) -> None:
        """
        Swaps subtree A with subtree B

        :param subtree_a : Root of the subtree A.
        :param subtree_b : Root of the subtree B.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """
        # TODO implement me please.
        if subtree_a == None:
            return
        if subtree_b == None:
            return
        
        parent_A = subtree_a.parent
        parent_B = subtree_b.parent
        self.rm(subtree_a)
        self.rm(subtree_b)
        self.put(parent_A, subtree_b)
        self.put(parent_B, subtree_a)



    def is_coloured_to_depth_k(self, start_node: Node, colour: Colour, k: int) -> bool:
        """
        Checks whether all nodes in the subtree (up and including level `k`
            starting from the start node) have the same colour!

        (This checks node.colour)

        :param start_node : The node to start checking.
        :param colour: The colour to compare a node's colour to.
        :param k: The depth we should check until.

        === Examples ===

        (start)---> G
                   / \
                  G   G
                 /|   |
                G R   G
                  |
                  R

        is_coloured_to_depth_k(start, Colours.GREEN, 0) => True
        is_coloured_to_depth_k(start, Colours.RED, 0) => False
        is_coloured_to_depth_k(start, Colours.GREEN, 1) => True
        is_coloured_to_depth_k(start, Colours.GREEN, 2) => False
        """

        # TODO implement me please.
   
        level = k+1
        current= start_node
        if self.check(start_node,level, colour) != 0:
            return False
        else:
            return True
    
    def check(self, node , level, colour ):
        ret = 0
        level -= 1
        if node.colour.cmp(colour) != 0:
            return 1
        if level:
            for i in node.children:
                ret += self.check(i, level, colour) 
        return ret
    def is_colour_until_condition(
            self,
            start_node: Node,
            colour_a: Colour,
            colour_b: Colour
        ) -> Tuple[bool, List[Node]]:
        """
        Checks whether the subtree rooted at `start_node` has colour_a until
        colour_b in all paths.

        We are checking the property: "In subtree rooted at start_node, is every
        path colour_a until colour_b?"

        If this condition fails, you must provide a path
        (given in the form of a list starting from `start_node to the failing
        node) as a "witness" to ensure that your answer is correct.

        NOTE: your path MUST be a valid path!
        If there are more than one paths - only one witness path is required.

        If the condition holds, then you return (True, None), as there is no
        required path.

        :param start_node: The node to start checking.
        :param colour_a: The first condition "colour_a holds until"
        :param colour_b: The stopping condition "until colour_b"


        === Examples ===

        (start)---> G
                   / \
                  G   G
                 /|   |
                R R   R
                  |
                  R

        is_colour_until_condition(start, Colours.GREEN, Colours.RED)
            -> (True, None)

        (start)---> G
                   / \
                  G   G (nodeA)
                 /|   |
                R R   G  (nodeD)
                  |
                  R

        is_colour_until_condition(start, Colours.GREEN, colours.RED)
            -> (False, [start, nodeA, nodeD])

        """

        # TODO implement me please.
        stack = []
        fail_node = self.f3(start_node, colour_a,colour_b, stack)
        if not stack:
            return True, None
        else:
            ret = []
            current = stack[0]
            ret.append(current)
            while current.parent != start_node.parent:
                ret.append(current.parent)
                current = current.parent
            ret2 = []
            while ret:
                ret2.append(ret.pop())
            return False, ret2
        

    def f3(self,node, start, end, stack):
        current = node
        if current.colour == start:
            if current.children:
                for i in current.children:
                    self.f3(i,start,end,stack) 
            else:
                stack.append(current)
                
        elif current.colour == end:
            return
        else:
            stack.append(current)
