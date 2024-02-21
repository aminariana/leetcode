import os
import json
from StringCompression.python import solution

class TestCompress:
    def test_compress(self):
        print("Testing ...")
        test_file_path = os.path.abspath(__file__)
        test_path = os.path.dirname(test_file_path)
        os.chdir(test_path)

        with open("../test/test.txt", "r") as testfile:
            for line in testfile:
                print(line)
                input, expected = (json.loads(x.strip()) for x in line.split(";"))
                print(f"Test: {input}, Expected: {expected}")
                actual = solution.compress(input) # length
                assert actual == len(expected)
                assert input[:actual] == expected # modifies input
