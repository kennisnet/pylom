from unittest import TestCase
from pylom.reader import LomReader

class FunctionsTestCase(TestCase):
    def setUp(self):
        self.lomreader = LomReader()

    def test_illegal_path(self):
        with self.assertRaises(RuntimeError):
            self.lomreader.parsePath("nopath")

    def test_fieldset(self):
        self.lomreader.parsePath("test/records/ims-complete.xml", ["title","structure"])
        self.assertEqual(self.lomreader.lom["title"],"Bloodbath of B-R5RB")
        self.assertEqual(self.lomreader.lom["structure"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["structure"]["value"],"hierarchical")
        self.assertEqual(self.lomreader.lom["size"],"")

    def test_stringread(self):
        with open("test/records/ims-complete.xml", "r") as f:
            lomstring = f.read()
        self.lomreader.parseString(lomstring)
        self.assertEqual(self.lomreader.lom["title"],"Bloodbath of B-R5RB")
