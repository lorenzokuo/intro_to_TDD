import unittest

def reverseList(list):
    pass

class reverseListTests(unittest.TestCase):
    def testOne(self):
        self.asserEqual(reverseList([1,2,3]), [3,2,1])
    def testTwo(self):
        self.asserEqual(reverseList([4,5,6]), [6,5,4])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()