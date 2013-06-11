import unittest
import StringIO
from json2csv import to_keyvalue_pairs, dicts_to_csv

class JSON2CSVTests(unittest.TestCase):
    def test_to_keyvalue_pairs_if_parameter_is_a_string_then_a_value_pair_is_built(self):
        result = to_keyvalue_pairs('value1', ['key1'])
        self.assertEquals(result, [('key1', 'value1')])

    def test_to_keyvalue_pairs_if_parameter_is_a_number_then_a_value_pair_is_built(self):
        result = to_keyvalue_pairs(1, ['key1'])
        self.assertEquals(result, [('key1', 1)])

    def test_to_keyvalue_pairs_if_parameter_is_a_list_then_pairs_are_built(self):
        result = to_keyvalue_pairs(['a', 'b', 'c'], ['key'])
        self.assertEquals(result, [('key_0', 'a'), ('key_1', 'b'), ('key_2', 'c')])

    def test_to_keyvalue_pairs_if_parameter_is_a_dict_then_pairs_are_build(self):
        result = to_keyvalue_pairs({'a': 1, 'b': 2, 'c': 3}, ['key'])
        self.assertEquals(result.sort(), [('key_a', 1), ('key_b', 2), ('key_c', 3)].sort())

    def test_dicts_to_csv(self):
        output_file = StringIO.StringIO()

        obj1 = { 'a': 'v1', 'b': 'v2'}
        obj2 = { 'a': 'v"\'3', 'b': 'v4'}
        obj3 = { 'a': 'v5', 'c': 'v6'}

        dicts_to_csv([obj1, obj2, obj3], output_file)
        result = output_file.getvalue().strip('\r\n')

        self.assertEquals('a,b,c\r\nv1,v2,\r\n"v""\'3",v4,\r\nv5,,v6', result)

if __name__ == '__main__':
    unittest.main()