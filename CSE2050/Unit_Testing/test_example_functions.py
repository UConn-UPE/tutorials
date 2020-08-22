import unittest
from example_functions import *

class TestExampleFunctions(unittest.TestCase):
    def setUp(self):
        print('Start of a test method')

    def tearDown(self):
        print('End of a test method')

    @classmethod
    def setUpClass(cls):
        print('Start of a class')

    @classmethod
    def tearDownClass(cls):
        print('End of a class') 

    def test_absolute_value(self):
        print('test_absolute_value_method')
        self.assertEqual(absolute_value(2), 2)
        self.assertEqual(absolute_value(0), 0)
        self.assertEqual(absolute_value(3.14), 3.14)
        self.assertEqual(absolute_value(-1), 1)
        self.assertEqual(absolute_value(-2.5), 2.5)
        with self.assertRaises(TypeError) as _:
            absolute_value('test')
            absolute_value([1, 2, 3])
            absolute_value({1, 2, 3})

    def test_square(self):
        print('test_square_method')
        self.assertEqual(square(3), 9)
        self.assertEqual(square(0), 0)
        self.assertAlmostEqual(square(.2), .04)
        self.assertEqual(square(-1), 1)
        self.assertAlmostEqual(square(-2.5), 6.25)
        with self.assertRaises(TypeError):
            square('test')
            square([1, 2, 3])
            square({1, 2, 3})

if __name__ == '__main__':
    unittest.main()
