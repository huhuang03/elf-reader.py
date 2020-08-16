import unittest
import tools.data_convert as dc

class TestDataConvert(unittest.TestCase):
    def test_to_int(self):
        b1 = b'\x01'
        assert dc.b_to_int(b1) == 1
