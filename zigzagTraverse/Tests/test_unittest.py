from zigzagTraverse import zigzagTraverse
import unittest

param_list = [[[[1,2,3]],[1,2,3]],[[[1,3,4]],[1,3,4]]]

class Test_zigzagTraverse(unittest.TestCase):
    
    def test_zigzagTraverse(self):
        for array, result in param_list:
            self.assertEqual(zigzagTraverse.zigzagTraverse(array), result)
            
if __name__ == '__main__':
    unittest.main()