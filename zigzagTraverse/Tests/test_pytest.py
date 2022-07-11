from zigzagTraverse import zigzagTraverse

param_list = [[[[1,2,3]],[1,2,3]],[[[1,3,4]],[1,3,4]]]

def test_zigzagTraverse():
    for array, result in param_list:
        assert zigzagTraverse.zigzagTraverse(array) == result