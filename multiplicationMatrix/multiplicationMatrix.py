import numpy
def multMatrix(a_matrix,b_matrix):
    height_matrix_a = a_matrix.shape[0]
    width_matrix_a = a_matrix.shape[1]
    width_matrix_b = b_matrix.shape[1]
    height_matrix_b = b_matrix.shape[0]

    if width_matrix_a != height_matrix_b:
        raise Exception('error')
    else:
        c_matrix = numpy.zeros(shape = (height_matrix_a, width_matrix_b));
        for i in range(0, height_matrix_a):
            for j in range(0, width_matrix_b):
                s = 0;
                for k in range(0, width_matrix_a):
                    a_item = a_matrix.item((i,k))
                    b_item = b_matrix.item((k,j))
                    s = s+a_item*b_item
                c_matrix.itemset((i,j),s)
        return c_matrix;
