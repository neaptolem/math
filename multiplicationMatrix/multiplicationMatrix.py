import numpy
def multMatrix(aMatrix,bMatrix):
    heightOfMatrixA=aMatrix.shape[0]
    widthOfMatrixA=aMatrix.shape[1]
    widthOfMatrixB=bMatrix.shape[1]
    heightOfMatrixB=bMatrix.shape[0]

    if widthOfMatrixA!=heightOfMatrixB:
        return 'Error'
    else:
        cMatrix=numpy.zeros(shape=(heightOfMatrixA, widthOfMatrixB));
        for i in range(0, heightOfMatrixA):
            for j in range(0, widthOfMatrixB):
                s=0;
                for k in range(0, widthOfMatrixA):
                    aItem=aMatrix.item((i,k))
                    bItem=bMatrix.item((k,j))
                    s=s+aItem*bItem
                cMatrix.itemset((i,j),s)
        return cMatrix;
