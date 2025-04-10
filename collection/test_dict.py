import unittest

from collection.Dict import Dict


class TestMyDict(unittest.TestCase):
    def test_MyDict_isEmpty(self):
        dict = Dict()
        self.assertTrue(dict.isEmpty())

    def test_MyDict_set_key(self):
        dict = Dict()
        dict.set("first","value")
        self.assertFalse(dict.isEmpty())unique

    import unittest

    from collection.Dict import Dict

    class TestMyDict(unittest.TestCase):
        def test_MyDict_isEmpty(self):
            dict = Dict()
            self.assertTrue(dict.isEmpty())

        def test_MyDict_set_key(self):
            dict = Dict()
            dict.set({"first": "value"})
            self.assertFalse(dict.isEmpty())