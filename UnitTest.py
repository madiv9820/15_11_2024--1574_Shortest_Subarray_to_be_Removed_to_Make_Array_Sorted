from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: ([1,2,3,10,4,2,3,5], 3), 2: ([5,4,3,2,1], 4), 3: ([1,2,3], 0)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case1(self):
        arr, output = self.__testCases[1]
        result = self.__obj.findLengthOfShortestSubarray(arr = arr)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case2(self):
        arr, output = self.__testCases[2]
        result = self.__obj.findLengthOfShortestSubarray(arr = arr)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case3(self):
        arr, output = self.__testCases[3]
        result = self.__obj.findLengthOfShortestSubarray(arr = arr)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()