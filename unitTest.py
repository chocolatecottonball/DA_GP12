import unittest
import dataAnalysis as proj


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([proj.top_3.index[0], proj.top_3.index[1], proj.top_3.index[2]], [' Australia ', ' USA ', ' New Zealand '])

    def test_somethings(self):
        self.assertTrue([proj.top_3.index[0], proj.top_3.index[1], proj.top_3.index[2]], [' Australia ', ' USA ', ' New Zealand '])

if __name__ == '__main__':
    unittest.main()