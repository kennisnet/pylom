from unittest import TestCase
from pylom.reader import LomReader

class ReaderElementsTestCase(TestCase):
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

    def test_coverage(self):
        self.assertIn("YC 116",self.lomreader.lom["coverage"])

    def test_structure(self):
        self.assertEqual(self.lomreader.lom["structure"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["structure"]["value"],"hierarchical")

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
        self.assertEqual(self.lomreader.lom["contribute"][0]["entity"][0],"BEGIN:VCARD\nFN:Wikipedia\nORG:Wikipedia\nEND:VCARD")
        self.assertEqual(self.lomreader.lom["contribute"][0]["date"]["datetime"],"2014-02-02T15:30:00Z")
        self.assertEqual(self.lomreader.lom["contribute"][0]["vcard"][0]["fn"],"Wikipedia")
        self.assertEqual(self.lomreader.lom["contribute"][0]["vcard"][0]["org"],"Wikipedia")
        self.assertEqual(self.lomreader.lom["contribute"][1]["role"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["contribute"][1]["role"]["value"],"author")
        self.assertEqual(self.lomreader.lom["contribute"][1]["entity"][0],"BEGIN:VCARD\nFN:3family6\nEND:VCARD")
        self.assertEqual(self.lomreader.lom["contribute"][1]["date"]["datetime"],"2017-06-08T03:16:00Z")
        self.assertEqual(self.lomreader.lom["contribute"][1]["vcard"][0]["fn"],"3family6")

    def test_metacatalogentry(self):
        self.assertEqual(self.lomreader.lom["metacatalogentry"][0]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["metacatalogentry"][0]["entry"], "https://github.com/kennisnet/pylom/blob/master/test/records/ims-complete.xml")

    def test_metacontribute(self):
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["role"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["role"]["value"],"creator")
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["entity"][0],"BEGIN:VCARD\nUID:https://github.com/wimmuskee\nEND:VCARD")
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["date"]["datetime"],"2017")
        self.assertEqual(self.lomreader.lom["metacontribute"][0]["vcard"][0]["uid"],"https://github.com/wimmuskee")

    def test_metadatascheme(self):
        self.assertIn("LOMv1.0", self.lomreader.lom["metadatascheme"])

    def test_metalanguage(self):
        self.assertEqual(self.lomreader.lom["metalanguage"],"en")

    def test_format(self):
        self.assertIn("text/html", self.lomreader.lom["format"])

    def test_size(self):
        self.assertEqual(self.lomreader.lom["size"],"23450")

    def test_location(self):
        self.assertEqual(self.lomreader.lom["location"],"https://en.wikipedia.org/wiki/Bloodbath_of_B-R5RB")

    def test_duration(self):
        self.assertEqual(self.lomreader.lom["duration"]["datetime"],"PT0H16M")
        self.assertEqual(self.lomreader.lom["duration"]["description"],"technical reading time")

    def test_educational(self):
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
        self.assertEqual(self.lomreader.lom["educational"][1]["context"][0]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][1]["context"][0]["value"], "higher education")
        self.assertIn("16-60", self.lomreader.lom["educational"][0]["typicalagerange"])
        self.assertEqual(self.lomreader.lom["educational"][0]["difficulty"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["educational"][0]["difficulty"]["value"], "difficult")
        self.assertEqual(self.lomreader.lom["educational"][0]["typicallearningtime"]["datetime"],"PT0H30M")
        self.assertEqual(self.lomreader.lom["educational"][0]["typicallearningtime"]["description"],"understanding reading time")
        self.assertEqual(self.lomreader.lom["educational"][0]["description"][0],"for individual reading")
        self.assertEqual(self.lomreader.lom["educational"][0]["language"][0],"en")

    def test_cost(self):
        self.assertEqual(self.lomreader.lom["cost"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["cost"]["value"],"no")

    def test_copyrightandotherrestrictions(self):
        self.assertEqual(self.lomreader.lom["copyrightandotherrestrictions"]["source"],"LOMv1.0")
        self.assertEqual(self.lomreader.lom["copyrightandotherrestrictions"]["value"],"yes")

    def test_copyrightdescription(self):
        self.assertEqual(len(self.lomreader.lom["copyrightdescription"]),47)

    def test_relation(self):
        self.assertEqual(self.lomreader.lom["relation"][0]["kind"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["relation"][0]["kind"]["value"], "references")
        self.assertEqual(self.lomreader.lom["relation"][0]["resource"]["description"][0], "Wikipedia article references")
        self.assertEqual(self.lomreader.lom["relation"][0]["resource"]["catalogentry"][0]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["relation"][0]["resource"]["catalogentry"][0]["entry"], "https://www.wired.com/gamelife/2014/02/eve-online-battle-of-b-r/")
        self.assertEqual(self.lomreader.lom["relation"][0]["resource"]["catalogentry"][1]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["relation"][0]["resource"]["catalogentry"][1]["entry"], "http://www.polygon.com/2014/1/30/5360208/Eve-Onlines-Bloodbath")
        self.assertEqual(self.lomreader.lom["relation"][1]["kind"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["relation"][1]["kind"]["value"], "isreferencedby")
        self.assertEqual(self.lomreader.lom["relation"][1]["resource"]["description"][0], "Wikipedia pages linking to this")
        self.assertEqual(self.lomreader.lom["relation"][1]["resource"]["catalogentry"][0]["catalog"], "URI")
        self.assertEqual(self.lomreader.lom["relation"][1]["resource"]["catalogentry"][0]["entry"], "https://www.wikidata.org/wiki/Q336177")
        self.assertEqual(self.lomreader.lom["relation"][2]["kind"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["relation"][2]["kind"]["value"], "hasformat")
        self.assertEqual(self.lomreader.lom["relation"][2]["resource"]["description"][0], "application/pdf")
        self.assertEqual(self.lomreader.lom["relation"][2]["resource"]["catalogentry"][0]["entry"], "https://en.wikipedia.org/w/index.php?title=Special:DownloadAsPdf&page=Bloodbath_of_B-R5RB&action=show-download-screen")

    def test_classification(self):
        self.assertEqual(self.lomreader.lom["classification"][0]["purpose"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["classification"][0]["purpose"]["value"], "idea")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["source"], "https://en.wikipedia.org/wiki/Category:Articles")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][0]["id"], "Category:Games")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][0]["entry"], "Games")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][1]["id"], "Category:Space_MMORPGs")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][1]["entry"], "Space MMORPGs")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][2]["id"], "Category:Eve_Online")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][2]["entry"], "Eve Online")
