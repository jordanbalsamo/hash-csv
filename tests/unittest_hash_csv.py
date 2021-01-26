import os
import unittest

class TestType(unittest.TestCase):

    def test_output_exists(self) -> None:

        case = os.path.isdir('../src/output')

        self.assertTrue(case)

    def test_output_dir_not_empty(self) -> None:

        case = len(os.listdir('../src/output/'))

        self.assertGreaterEqual(case, 1)

    def test_number_rows_match(self) -> None:
        with open('../data/customer.csv') as f:
            source = sum(1 for line in f)
        
        with open('../src/output/customer-obfuscated.csv') as f:
            target = sum(1 for line in f)

        self.assertEqual(source, target)


    # md5 hashsum source != target

    # sample hash equivalence


if __name__ == '__main__':
    
    unittest.main(verbosity=2)