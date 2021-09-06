import unittest
import temperature_conversion


class TestTemp(unittest.TestCase):
    def test_temperature_conversion(self):
        value_one = ['33 C']
        result = temperature_conversion.temp_conv(value_one)
        self.assertIsNotNone(result)

