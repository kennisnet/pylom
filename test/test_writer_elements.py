from unittest import TestCase
from pylom.reader import LomReader
from pylom.writer import LomWriter

class WriterElementsTestCase(TestCase):
    @classmethod
    def setUpClass(self):
        self.lomreader = LomReader()

    def test_title(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"title": "Bloodbath of B-R5RB"})
        self.lomreader.parseString(lomwriter.lom,["title"])
        self.assertEqual(self.lomreader.lom["title"], "Bloodbath of B-R5RB")

    def test_catalogentry(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"catalogentry": [{"catalog": "URI", "entry": "https://www.wikidata.org/wiki/Q16987908"}]})
        self.lomreader.parseString(lomwriter.lom,["catalogentry"])
        self.assertEqual(self.lomreader.lom["catalogentry"][0]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["catalogentry"][0]["entry"], "https://www.wikidata.org/wiki/Q16987908")

    def test_language(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"language": "en"})
        self.lomreader.parseString(lomwriter.lom,["language"])
        self.assertIn("en",self.lomreader.lom["language"])

    def test_keyword(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"keyword": ["Eve Online", "Halloween War"]})
        self.lomreader.parseString(lomwriter.lom,["keyword"])
        self.assertIn("Eve Online",self.lomreader.lom["keyword"])
        self.assertIn("Halloween War",self.lomreader.lom["keyword"])

    def test_structure(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"structure": "hierarchical"})
        self.lomreader.parseString(lomwriter.lom,["structure"])
        self.assertEqual(self.lomreader.lom["structure"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["structure"]["value"],"hierarchical")

    def test_aggregationlevel(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"aggregationlevel": {"source": "custom", "value": "hierarchical"}})
        self.lomreader.parseString(lomwriter.lom,["aggregationlevel"])
        self.assertEqual(self.lomreader.lom["aggregationlevel"]["source"],"custom")
        self.assertEqual(self.lomreader.lom["aggregationlevel"]["value"],"hierarchical")

    def test_status(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"status": "final"})
        self.lomreader.parseString(lomwriter.lom,["status"])
        self.assertEqual(self.lomreader.lom["status"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["status"]["value"],"final")

    def test_contribute(self):
        contributions = [{"role": "publisher", "entity": "BEGIN:VCARD\nFN:Wikipedia\nEND:VCARD", "date": "2014-02-02T15:30:00Z"}]
        lomwriter = LomWriter()
        lomwriter.parseDict({"contribute": contributions})
        self.lomreader.parseString(lomwriter.lom,["contribute"])
        self.assertEqual(self.lomreader.lom["contribute"][0]["role"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["contribute"][0]["role"]["value"],"publisher")
        self.assertEqual(self.lomreader.lom["contribute"][0]["entity"][0],"BEGIN:VCARD\nFN:Wikipedia\nEND:VCARD")
        self.assertEqual(self.lomreader.lom["contribute"][0]["date"]["datetime"],"2014-02-02T15:30:00Z")

    def test_duration(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"duration": {"datetime": "PT0H16M", "description": "technical reading time"}})
        self.lomreader.parseString(lomwriter.lom,["duration"])
        self.assertEqual(self.lomreader.lom["duration"]["datetime"],"PT0H16M")
        self.assertEqual(self.lomreader.lom["duration"]["description"],"technical reading time")

    def test_educational(self):
        educationals = [ {"interactivitytype": "expositive",
                          "learningresourcetype": "narrative text",
                          "interactivitylevel": "low",
                          "semanticdensity": "high",
                          "intendedenduserrole": "learner",
                          "context": ["school", "higher education"],
                          "difficulty": "difficult" }]
        lomwriter = LomWriter()
        lomwriter.parseDict({"educational": educationals})
        self.lomreader.parseString(lomwriter.lom,["educational"])
        self.assertEqual(self.lomreader.lom["educational"][0]["interactivitytype"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["interactivitytype"]["value"], "expositive")
        self.assertEqual(self.lomreader.lom["educational"][0]["learningresourcetype"][0]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["learningresourcetype"][0]["value"], "narrative text")
        self.assertEqual(self.lomreader.lom["educational"][0]["interactivitylevel"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["interactivitylevel"]["value"], "low")
        self.assertEqual(self.lomreader.lom["educational"][0]["semanticdensity"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["semanticdensity"]["value"], "high")
        self.assertEqual(self.lomreader.lom["educational"][0]["intendedenduserrole"][0]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["intendedenduserrole"][0]["value"], "learner")
        self.assertEqual(self.lomreader.lom["educational"][0]["context"][0]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["context"][0]["value"], "school")
        self.assertEqual(self.lomreader.lom["educational"][0]["context"][1]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["context"][1]["value"], "higher education")
        self.assertEqual(self.lomreader.lom["educational"][0]["difficulty"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["difficulty"]["value"], "difficult")

    def test_cost(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"cost": "no"})
        self.lomreader.parseString(lomwriter.lom,["cost"])
        self.assertEqual(self.lomreader.lom["cost"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["cost"]["value"],"no")

    def test_copyrightandotherrestrictions(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"copyrightandotherrestrictions": "yes"})
        self.lomreader.parseString(lomwriter.lom,["copyrightandotherrestrictions"])
        self.assertEqual(self.lomreader.lom["copyrightandotherrestrictions"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["copyrightandotherrestrictions"]["value"],"yes")
