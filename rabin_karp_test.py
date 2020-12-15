import unittest

from rabin_karp import findAllMatches


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(findAllMatches("aabaab", "aab"), [0, 3])
        self.assertEqual(findAllMatches("Aabaab", "aab"), [3])
        self.assertEqual(findAllMatches("Kids are talking by the door", "talk"), [9])
        self.assertEqual(findAllMatches("aaaaa", "aa"), [0, 1, 2, 3])



if __name__ == '__main__':
    unittest.main()
