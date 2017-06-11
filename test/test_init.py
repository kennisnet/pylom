from unittest import TestCase
from pylom.reader import LomReader

class InitTestCase(TestCase):
    def setUp(self):
        self.lomreader = LomReader()

    def test_illegal_path(self):
        with self.assertRaises(RuntimeError):
            self.lomreader.parsePath("nopath")
