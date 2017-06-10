from unittest import TestCase
from pylom.reader import LomReader

class ElementsTestCase(TestCase):
    @classmethod
    def setUpClass(self):
        self.lomreader = LomReader()
        self.lomreader.parsePath("test/records/ims-complete.xml")

    def test_title(self):
        self.assertEqual(self.lomreader.lom["title"],"Bloodbath of B-R5RB")

    def test_catalogentry(self):
        self.assertEqual(self.lomreader.lom["catalogentry"][0]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["catalogentry"][0]["entry"], "https://en.wikipedia.org/wiki/Bloodbath_of_B-R5RB")
        self.assertEqual(self.lomreader.lom["catalogentry"][1]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["catalogentry"][1]["entry"], "https://www.wikidata.org/wiki/Q16987908")

    def test_language(self):
        self.assertIn("en",self.lomreader.lom["language"])

    def test_description(self):
        self.assertEqual(len(self.lomreader.lom["description"][0]),195)

    def test_keyword(self):
        self.assertIn("Eve Online",self.lomreader.lom["keyword"])
        self.assertIn("Halloween War",self.lomreader.lom["keyword"])

    def test_aggregationlevel(self):
        self.assertEqual(self.lomreader.lom["aggregationlevel"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["aggregationlevel"]["value"],"2")

    def test_version(self):
        self.assertEqual(self.lomreader.lom["version"],"1.0.0")

    def test_status(self):
        self.assertEqual(self.lomreader.lom["status"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["status"]["value"],"final")

    def test_contribute(self):
        self.assertEqual(self.lomreader.lom["contribute"][0]["role"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["contribute"][0]["role"]["value"],"publisher")
        self.assertEqual(self.lomreader.lom["contribute"][0]["entity"][0],"BEGIN:VCARD\nFN:Wikipedia\nEND:VCARD")
        self.assertEqual(self.lomreader.lom["contribute"][0]["date"],"2014-02-02T15:30:00Z")
        self.assertEqual(self.lomreader.lom["contribute"][1]["role"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["contribute"][1]["role"]["value"],"author")
        self.assertEqual(self.lomreader.lom["contribute"][1]["entity"][0],"BEGIN:VCARD\nFN:3family6\nEND:VCARD")
        self.assertEqual(self.lomreader.lom["contribute"][1]["date"],"2017-06-08T03:16:00Z")

    def test_metacatalogentry(self):
        self.assertEqual(self.lomreader.lom["metacatalogentry"][0]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["metacatalogentry"][0]["entry"], "https://github.com/kennisnet/pylom/blob/master/test/records/ims-complete.xml")

    def test_metacontribute(self):
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["role"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["role"]["value"],"creator")
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["entity"][0],"BEGIN:VCARD\nUID:https://github.com/wimmuskee\nEND:VCARD")
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["date"],"2017")

    def test_metadatascheme(self):
        self.assertIn("LOMv1.0", self.lomreader.lom["metadatascheme"])

    def test_metalanguage(self):
        self.assertEqual(self.lomreader.lom["metalanguage"],"en")

    def test_format(self):
        self.assertIn("text/html", self.lomreader.lom["format"])

    def test_location(self):
        self.assertEqual(self.lomreader.lom["location"],"https://en.wikipedia.org/wiki/Bloodbath_of_B-R5RB")

    def test_learningresourcetype(self):
        self.assertEqual(self.lomreader.lom["learningresourcetype"][0]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["learningresourcetype"][0]["value"], "narrative text")

    def test_intendedenduserrole(self):
        self.assertEqual(self.lomreader.lom["intendedenduserrole"][0]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["intendedenduserrole"][0]["value"], "learner")

    def test_context(self):
        self.assertEqual(self.lomreader.lom["context"][0]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["context"][0]["value"], "school")
        self.assertEqual(self.lomreader.lom["context"][1]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["context"][1]["value"], "higher education")

    def test_typicalagerange(self):
        self.assertIn("16-60", self.lomreader.lom["typicalagerange"])

    def test_cost(self):
        self.assertEqual(self.lomreader.lom["cost"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["cost"]["value"],"no")

    def test_copyrightandotherrestrictions(self):
        self.assertEqual(self.lomreader.lom["copyrightandotherrestrictions"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["copyrightandotherrestrictions"]["value"],"yes")

    def test_copyrightdescription(self):
        self.assertEqual(len(self.lomreader.lom["copyrightdescription"]),47)
