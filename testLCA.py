import unittest
import LCA

class TestLCA(unittest.TestCase):

    def test_LCA(self):
        # Driver program to test above function 
        root = LCA.Node(1) 
        self.assertIsNone(LCA.findLCA(root, 2, 3))
        root.left = LCA.Node(2) 
        root.right = LCA.Node(3) 
        root.left.left = LCA.Node(4) 
        root.left.right = LCA.Node(5) 
        root.right.left = LCA.Node(6) 
        root.right.right = LCA.Node(7) 
        
        self.assertEqual(2, LCA.findLCA(root, 4, 5).key)

        self.assertIsNone(LCA.findLCA(root, 4, 10))

        self.assertIsNone(LCA.findLCA(root, 10, 4))