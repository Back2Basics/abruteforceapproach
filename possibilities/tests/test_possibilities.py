import numpy as np
from possibilities.posibility_generator import possibilities
import unittest
from _collections import defaultdict

class test_matrix_possibilities(unittest.TestCase):
    def setUp(self):
        self.start = np.arange(6).reshape(2, 3)
        self.finish = np.array([[0, 3],
                                        [1, 4],
                                        [2, 5]]
        )

    def tearDown(self):
        del(self.start)
        del(self.finish)

    def test_transpose(self):
        d = defaultdict(list)
        for k,v in possibilities(start = self.start, finish=self.finish, libs=[np]):
            d[k].append(v)
        self.assertIn('transpose' , d)
    

class test_unary_possibilities(unittest.TestCase):
    def setUp(self):
        self.start = np.array([-5])
        self.finish = np.array([5])
    
    def tearDown(self):
        del(self.start)
        del(self.finish)

    def test_abs(self):
        self.assertTrue(possibilities(start = self.start, finish=self.finish, libs=[np]))
    
    
if __name__ == '__main__':
    unittest.main()


