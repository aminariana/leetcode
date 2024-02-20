import os
import json
from FindTheDifferenceOfTwoArrays.python import array_difference

class TestArrayDifference:
    def test_find_difference(self):
        print("Testing ...")
        test_file_path = os.path.abspath(__file__)
        test_path = os.path.dirname(test_file_path)
        os.chdir(test_path)

        with open("../test/test.txt", "r") as testfile:
            for line in testfile:
                print(line)
                input1, input2, expected = (json.loads(x.strip()) for x in line.split(";"))
                print(f"array_difference: {input1} vs {input2}, Expected: {expected}")
                actual = array_difference.find_difference(input1, input2)
                assert actual == expected
