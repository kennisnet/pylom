from unittest import TestCase
from pylom.reader import LomReader

class FailReaderElementsTestCase(TestCase):
    @classmethod
    def setUpClass(self):
        self.lomreader = LomReader()
        self.lomreader.parsePath("test/records/ims-incomplete.xml")

    def test_empty_element(self):
        self.assertIn("",self.lomreader.lom["keyword"])

    def test_empty_vocabulary_element(self):
        self.assertEqual(self.lomreader.lom["aggregationlevel"]["value"],"")

    def test_no_occurence(self):
        self.assertEqual(self.lomreader.lom["version"],"")
