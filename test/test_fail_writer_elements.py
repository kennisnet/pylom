from unittest import TestCase
from pylom.writer import LomWriter

class FailWriterElementsTestCase(TestCase):
    def setUp(self):
        self.lomwriter = LomWriter()

    def test_empty_element(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"language": ""})

    def test_empty_langstring_element(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"title": ""})

    def test_empty_catalogentry_element(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"catalogentry": [{"catalog": "", "entry": "https://www.wikidata.org/wiki/Q16987908"}]})
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"catalogentry": [{"catalog": "URI", "entry": ""}]})

    def test_missing_catalogentry_element(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"catalogentry": [{}] })
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"catalogentry": [{"entry": "https://www.wikidata.org/wiki/Q16987908"}]})
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"catalogentry": [{"catalog": "URI"}]})

    def test_empty_vocabulary_element(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"aggregationlevel": ""})

    def test_empty_vocabulary_element_dict(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"aggregationlevel": {"source": "", "value": "2"}})
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"aggregationlevel": {"source": "LOMv1.0", "value": ""}})

    def test_missing_vocabulary_element_dict(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"aggregationlevel": {} })
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"aggregationlevel": {"source": "LOMv1.0"}})
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"aggregationlevel": {"value": "2"}})

    def test_empty_datetime_element(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"duration": ""})

    def test_empty_datetime_element_dict(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"duration": {"datetime": "", "description": "technical reading time"}})
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"duration": {"datetime": "PT0H16M", "description": ""}})

    def test_missing_datetime_element_dict(self):
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"duration": {} })
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"duration": {"datetime": "PT0H16M"}})
        with self.assertRaises(ValueError):
            self.lomwriter.parseDict({"duration": {"description": "technical reading time"}})
