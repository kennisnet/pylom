from unittest import TestCase
from pylom.reader import LomReader
from pylom.writer import LomWriter

class WriterElementsTestCase(TestCase):
    def setUp(self):
        self.lomreader = LomReader()


    def test_title(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"title": "Bloodbath of B-R5RB"})
        self.lomreader.parseString(lomwriter.lom,["title"])
        self.assertEqual(self.lomreader.lom["title"], "Bloodbath of B-R5RB")

    def test_title_unicode(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"title": u"Bloodbath of B-R5RB"})
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

    def test_structure_unicode(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"structure": u"hierarchical"})
        self.lomreader.parseString(lomwriter.lom,["structure"])
        self.assertEqual(self.lomreader.lom["structure"]["value"],"hierarchical")

    def test_aggregationlevel(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"aggregationlevel": {"source": "custom", "value": "5"}})
        self.lomreader.parseString(lomwriter.lom,["aggregationlevel"])
        self.assertEqual(self.lomreader.lom["aggregationlevel"]["source"],"custom")
        self.assertEqual(self.lomreader.lom["aggregationlevel"]["value"],"5")

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

    def test_location(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"location": "https://www.wikidata.org/wiki/Q16987908"})
        self.lomreader.parseString(lomwriter.lom,["location"])
        self.assertEqual(self.lomreader.lom["location"],"https://www.wikidata.org/wiki/Q16987908")

    def test_location_unicode(self):
        lomwriter = LomWriter()
        lomwriter.parseDict({"location": u"https://www.wikidata.org/wiki/Q16987908"})
        self.lomreader.parseString(lomwriter.lom,["location"])
        self.assertEqual(self.lomreader.lom["location"],"https://www.wikidata.org/wiki/Q16987908")

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
                          "typicalagerange": "12+",
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
        self.assertEqual(self.lomreader.lom["educational"][0]["typicalagerange"][0], "12+")

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

    def test_relation(self):
        relations = [
            { "kind": "references", 
                "resource": { 
                    "description": "Wikipedia article references", 
                    "catalogentry": [
                        {"catalog": "URI", "entry": "https://www.wired.com/gamelife/2014/02/eve-online-battle-of-b-r/"},
                        {"catalog": "URI", "entry": "http://www.polygon.com/2014/1/30/5360208/Eve-Onlines-Bloodbath"} ] } },
            { "kind": "isreferencedby", 
                "resource": { 
                    "description": "Wikipedia pages linking to this", 
                    "catalogentry": [
                        {"catalog": "URI", "entry": "https://www.wikidata.org/wiki/Q336177"}] } } ]
        lomwriter = LomWriter()
        lomwriter.parseDict({"relation": relations})
        self.lomreader.parseString(lomwriter.lom,["relation"])
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

    def test_classification(self):
        classifications = [
            { "purpose": "idea",
                "taxonpath": [ { "source": "https://en.wikipedia.org/wiki/Category:Articles", "taxon": [
                    { "id": "Category:Games", "entry": "Games" },
                    { "id": "Category:Space_MMORPGs", "entry": "Space MMORPGs" } ] } ] } ]
        lomwriter = LomWriter()
        lomwriter.parseDict({"classification": classifications})
        self.lomreader.parseString(lomwriter.lom,["classification"])
        self.assertEqual(self.lomreader.lom["classification"][0]["purpose"]["source"], "LOMv1.0")
        self.assertEqual(self.lomreader.lom["classification"][0]["purpose"]["value"], "idea")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["source"], "https://en.wikipedia.org/wiki/Category:Articles")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][0]["id"], "Category:Games")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][0]["entry"], "Games")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][1]["id"], "Category:Space_MMORPGs")
        self.assertEqual(self.lomreader.lom["classification"][0]["taxonpath"][0]["taxon"][1]["entry"], "Space MMORPGs")
