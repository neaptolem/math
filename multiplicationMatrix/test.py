from multiplicationMatrix import *
import unittest

class TestMultMatrix(unittest.TestCase):


    def test_1(self):
        a = numpy.matrix('2 2 4; 2 1 1')
        b = numpy.matrix('6 1; 4 -1; 7 2')
        c = numpy.matrix('48 8; 23 3')
        self.assertTrue(numpy.allclose(multMatrix(a,b),c))

    def test_2(self):
        a = numpy.matrix('6 1; 4 -1; 7 2')
        b = numpy.matrix('2 2 4; 2 1 1')
        c = numpy.matrix('14 13 25; 6 7 15; 18 16 30')
        self.assertTrue(numpy.allclose(multMatrix(a,b),c))

    def test_3(self):
        a = numpy.matrix('2 2; 3 3')
        b = numpy.matrix('1')
        self.assertEqual(multMatrix(a,b),'error')
unittest.main()
