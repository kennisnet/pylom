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

    def test_broken_vcard(self):
        self.assertEqual(len(self.lomreader.lom["contribute"][0]["vcard"]), 2)
        self.assertEqual(self.lomreader.lom["contribute"][0]["vcard"][0], {})
        self.assertEqual(self.lomreader.lom["contribute"][0]["vcard"][1]["fn"], "Correct Vcard")
