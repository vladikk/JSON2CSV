import filecmp
import os
from subprocess import call
import unittest


tests_folder = "tests/testcases"
input_file_ext = ".json"
expected_file_ext = ".csv"

class End2EndTests(unittest.TestCase):
  def test_all_testcases(self):
    output_file = os.path.join(tests_folder, "actual.csv")
    for f in self.get_all_test_cases():
      input_file = os.path.join(tests_folder, f+input_file_ext)
      expected_file = os.path.join(tests_folder, f+expected_file_ext)
      self.execute_test(input_file, output_file, expected_file)
    os.remove(output_file)

  def execute_test(self, input_file, output_file, expected_file):
    call(["json2csv", input_file, output_file])
    self.assertTrue(filecmp.cmp(output_file, expected_file))

  def get_all_test_cases(self):
    for f in os.listdir(tests_folder):
      if f.endswith(input_file_ext):
        yield os.path.splitext(f)[0]

if __name__ == '__main__':
    unittest.main()
