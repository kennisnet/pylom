from unittest import TestCase
from pylom.reader import LomReader

class ElementsTestCase(TestCase):
    @classmethod
    def setUpClass(self):
        self.lomreader = LomReader()
        self.lomreader.parsePath("test/records/ims-complete.xml")

    def test_title(self):
        self.assertEqual(self.lomreader.lom["title"],"Bloodbath of B-R5RB")

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
