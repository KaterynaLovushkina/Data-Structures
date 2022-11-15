import unittest
from boyer_moore import PatternSearch
import time
pattern1 = 'kkkkkkk'
pattern2 = 'abbddmnkk'
pattern3 = "absababab"

class MyTestCase(unittest.TestCase):
    def test_bm_worst_case(self):
        ps1 = PatternSearch(pattern1,"../resources/worst_case.txt", "result1.txt")
        start = time.perf_counter()
        ps1.boyer_moore_search()
        end = time.perf_counter()
        print(f"Time taken: {(end - start) * 10 ** 3:5f}ms - worst case")
        ps1.write_to_file()

    def test_bm_best_case(self):
        ps2 = PatternSearch(pattern2, "../resources/average_case.txt", "result2.txt")
        start = time.perf_counter()
        ps2.boyer_moore_search()
        end = time.perf_counter()
        print(f"Time taken: {(end - start) * 10 ** 3:5f}ms - best case")
        ps2.write_to_file()

    def test_bm_average_case(self):
        ps3 = PatternSearch(pattern3,"../resources/average_case.txt", "result3.txt")
        start = time.perf_counter()
        ps3.boyer_moore_search()
        end = time.perf_counter()
        print(f"Time taken: {(end - start) * 10 ** 3:5f}ms - average case")
        ps3.write_to_file()


if __name__ == '__main__':
    unittest.main()
