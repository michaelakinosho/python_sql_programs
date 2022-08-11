import sparse_matrix_multiplication

class Test_Sparse_matrix_multiplication_Sparse_matrix_multiplication:
    def test_sparse_matrix_multiplication_1(self):
        result = sparse_matrix_multiplication.sparse_matrix_multiplication([1.0], [10.23])

    def test_sparse_matrix_multiplication_2(self):
        result = sparse_matrix_multiplication.sparse_matrix_multiplication([-1.0], [0.0])

    def test_sparse_matrix_multiplication_3(self):
        result = sparse_matrix_multiplication.sparse_matrix_multiplication([-1.0], [0.5])

    def test_sparse_matrix_multiplication_4(self):
        result = sparse_matrix_multiplication.sparse_matrix_multiplication([1.0], [10.0])

    def test_sparse_matrix_multiplication_5(self):
        result = sparse_matrix_multiplication.sparse_matrix_multiplication([10.23], [1.0])

    def test_sparse_matrix_multiplication_6(self):
        result = sparse_matrix_multiplication.sparse_matrix_multiplication([], [])

