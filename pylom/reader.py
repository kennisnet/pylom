# -*- coding: utf-8 -*-

from pylom.lom import Lom
from lxml import etree
import vobject

class LomReader(Lom):
    def __init__(self,language="en"):
        Lom.__init__(self,language)
        self.ns = {'lom': 'http://www.imsglobal.org/xsd/imsmd_v1p2'}
        self.__setEmptyLom()
        self.fieldset = []


    def parsePath(self,path,fieldset=[]):
        """ Parse LOM XML based on path. """
        try:
            self.lomxml = etree.parse(path)
        except Exception as e:
            raise RuntimeError(e)

        self.fieldset = fieldset
        self.__parseLom()


    def parseString(self,lomstring,fieldset=[]):
        """ Parse LOM XML based on string. """
        try:
            self.lomxml = etree.fromstring(lomstring)
        except Exception as e:
            raise RuntimeError(e)

        self.fieldset = fieldset
        self.__parseLom()


    def setCustomEmptyLom(self,customdict):
        """ Sets a custom empty LOM dictionary. In this, the user can specify
        how answers should be formatted, for example always return the first title."""
        if isinstance(customdict, dict):
            self.lom = customdict
        else:
            raise TypeError("custom empty LOM should be a dictionary")


    def __parseLom(self):
        if self.lomxml is None:
            raise RuntimeError("there is no LOM Etree object")

        if self.fieldset:
            self.__parseFieldset()
        else:
            self.__parseFull()

    def __parseFull(self):
        """ Parses using all __setField* methods. """
        for fieldkey in self.fmethods:
            attribute = "_" + self.__class__.__name__ + self.fmethods[fieldkey]
            getattr(self,attribute)()

    def __parseFieldset(self):
        """ Parses using only the keys provided in fieldset. """
        for fieldkey in self.fmethods:
            if fieldkey in self.fieldset:
                attribute = "_" + self.__class__.__name__ + self.fmethods[fieldkey]
                getattr(self,attribute)()


    def __setEmptyLom(self):
        """ Creates an empty LOM dictionary. An empty string denotes a single
        value, and empty list a multiple value element. """
        self.lom = {
            "title": "",
            "catalogentry": [],
            "language": [],
            "description": [],
            "keyword": [],
            "coverage": [],
            "structure": "",
            "aggregationlevel": "",
            "version": "",
            "status": "",
            "contribute": [],
            "metacatalogentry": [],
            "metacontribute": [],
            "metadatascheme": [],
            "metalanguage": "",
            "format": [],
            "size": "",
            "location": "",
            "duration": "",
            "educational": [],
            "cost": "",
            "copyrightandotherrestrictions": "",
            "copyrightdescription": "",
            "relation": [],
            "classification": [] }


    def __setFieldTitle(self):
        self.__setElement("/lom:lom/lom:general/lom:title/lom:langstring[@xml:lang='" + self.lang + "']", "title")

    def __setFieldCatalogEntry(self):
        self.__setCatalogEntryElement("/lom:lom/lom:general/lom:catalogentry", "catalogentry")

    def __setFieldLanguage(self):
        self.__setElement("/lom:lom/lom:general/lom:language","language")

    def __setFieldDescription(self):
        self.__setElement("/lom:lom/lom:general/lom:description/lom:langstring[@xml:lang='" + self.lang + "']", "description")

    def __setFieldKeyword(self):
        self.__setElement("/lom:lom/lom:general/lom:keyword/lom:langstring[@xml:lang='" + self.lang + "']", "keyword")

    def __setFieldCoverage(self):
        self.__setElement("/lom:lom/lom:general/lom:coverage/lom:langstring[@xml:lang='" + self.lang + "']", "coverage")

    def __setFieldStructure(self):
        self.__setVocabularyElement("/lom:lom/lom:general/lom:structure", "structure")

    def __setFieldAggregationLevel(self):
        self.__setVocabularyElement("/lom:lom/lom:general/lom:aggregationlevel", "aggregationlevel")

    def __setFieldVersion(self):
        self.__setElement("/lom:lom/lom:lifecycle/lom:version/lom:langstring","version")

    def __setFieldStatus(self):
        self.__setVocabularyElement("/lom:lom/lom:lifecycle/lom:status", "status")

    def __setFieldContribute(self):
        self.__setContributeElement("/lom:lom/lom:lifecycle/lom:contribute", "contribute")

    def __setFieldMetaCatalogEntry(self):
        self.__setCatalogEntryElement("/lom:lom/lom:metametadata/lom:catalogentry", "metacatalogentry")

    def __setFieldMetaContribute(self):
        self.__setContributeElement("/lom:lom/lom:metametadata/lom:contribute", "metacontribute")

    def __setFieldMetadataScheme(self):
        self.__setElement("/lom:lom/lom:metametadata/lom:metadatascheme","metadatascheme")

    def __setFieldMetaLanguage(self):
        self.__setElement("/lom:lom/lom:metametadata/lom:language","metalanguage")

    def __setFieldFormat(self):
        self.__setElement("/lom:lom/lom:technical/lom:format","format")

    def __setFieldSize(self):
        self.__setElement("/lom:lom/lom:technical/lom:size","size")

    def __setFieldLocation(self):
        self.__setElement("/lom:lom/lom:technical/lom:location","location")

    def __setFieldDuration(self):
        self.lom["duration"] = self.__getDurationElement(self.lomxml,"/lom:lom/lom:technical/lom:duration")

    def __setFieldEducational(self):
        """ Parses the educational element. """
        element = self.lomxml.xpath("/lom:lom/lom:educational", namespaces=self.ns)
        if element:
            for e in element:
                data = {
                    "interactivitytype": "",
                    "learningresourcetype": [],
                    "interactivitylevel": "",
                    "semanticdensity": "",
                    "intendedenduserrole": [],
                    "context": [],
                    "typicalagerange": [],
                    "difficulty": "",
                    "typicallearningtime": "",
                    "description": [],
                    "language": [] }
                data["interactivitytype"] = self.__getSingleVocabularyElement(e,"lom:interactivitytype")
                data["learningresourcetype"] = self.__getMultipleVocabularyElement(e,"lom:learningresourcetype")
                data["interactivitylevel"] = self.__getSingleVocabularyElement(e,"lom:interactivitylevel")
                data["semanticdensity"] = self.__getSingleVocabularyElement(e,"lom:semanticdensity")
                data["intendedenduserrole"] = self.__getMultipleVocabularyElement(e,"lom:intendedenduserrole")
                data["context"] = self.__getMultipleVocabularyElement(e,"lom:context")
                data["typicalagerange"] = self.__getMultipleElement(e,"lom:typicalagerange/lom:langstring")
                data["difficulty"] = self.__getSingleVocabularyElement(e,"lom:difficulty")
                data["typicallearningtime"] = self.__getDurationElement(e,"lom:typicallearningtime")
                data["description"] = self.__getMultipleElement(e,"lom:description/lom:langstring[@xml:lang='" + self.lang + "']")
                data["language"] = self.__getMultipleElement(e,"lom:language")

                self.lom["educational"].append(data)

    def __setFieldCost(self):
        self.__setVocabularyElement("/lom:lom/lom:rights/lom:cost", "cost")

    def __setFieldCopyrightAndOtherRestrictions(self):
        self.__setVocabularyElement("/lom:lom/lom:rights/lom:copyrightandotherrestrictions", "copyrightandotherrestrictions")

    def __setFieldCopyrightDescription(self):
        self.__setElement("/lom:lom/lom:rights/lom:description/lom:langstring[@xml:lang='" + self.lang + "']", "copyrightdescription")
        if not self.lom["copyrightdescription"]:
            # fallback to x-none langstring
            self.__setElement("/lom:lom/lom:rights/lom:description/lom:langstring[@xml:lang='x-none']", "copyrightdescription")

    def __setFieldRelation(self):
        """ Parses the relation element. """
        element = self.lomxml.xpath("/lom:lom/lom:relation", namespaces=self.ns)
        if element:
            for e in element:
                data = {"kind": "", "resource": ""}
                data["kind"] = self.__getSingleVocabularyElement(e,"lom:kind")
                resource = e.xpath("lom:resource", namespaces=self.ns)
                if resource:
                    res_data = {"description": [], "catalogentry": []}
                    res_data["description"] = self.__getMultipleElement(resource[0],"lom:description/lom:langstring[@xml:lang='" + self.lang + "']")
                    if not res_data["description"]:
                        # fallback to x-none langstring
                        res_data["description"] = self.__getMultipleElement(resource[0],"lom:description/lom:langstring[@xml:lang='x-none']")
                    catalogentry = resource[0].xpath("lom:catalogentry", namespaces=self.ns)
                    if catalogentry:
                        res_data["catalogentry"] = self.__getCatalogEntryElement(catalogentry)
                    data["resource"] = res_data

                self.lom["relation"].append(data)

    def __setFieldClassification(self):
        """ Parses the classification element. """
        element = self.lomxml.xpath("/lom:lom/lom:classification", namespaces=self.ns)
        if element:
            for e in element:
                data = {"purpose": "", "taxonpath": []}
                data["purpose"] = self.__getSingleVocabularyElement(e,"lom:purpose")
                taxonpath = e.xpath("lom:taxonpath", namespaces=self.ns)
                if taxonpath:
                    for path in taxonpath:
                        tp_data = {"source": "", "taxon": []}
                        tp_data["source"] = self.__getSingleElement(path, "lom:source/lom:langstring")
                        taxon = path.xpath("lom:taxon", namespaces=self.ns)
                        if taxon:
                            for t in taxon:
                                t_data = {"id": "", "entry": ""}
                                t_data["id"] = self.__getSingleElement(t, "lom:id")
                                t_data["entry"] = self.__getSingleElement(t, "lom:entry/lom:langstring")
                                tp_data["taxon"].append(t_data)
                        data["taxonpath"].append(tp_data)

                self.lom["classification"].append(data)


    def __setElement(self,xpath,lomkey):
        """ Sets the value from the xpath in the specified lomkey. """
        if isinstance(self.lom[lomkey], str):
            self.lom[lomkey] = self.__getSingleElement(self.lomxml,xpath)
        elif isinstance(self.lom[lomkey], list):
            self.lom[lomkey] = self.__getMultipleElement(self.lomxml,xpath)
        else:
            raise LookupError("bad type definition in empty LOM")


    def __setVocabularyElement(self,xpath,lomkey):
        """ Sets the vocabulary source and value from the xpath in the specified lomkey. """
        if isinstance(self.lom[lomkey], str):
            self.lom[lomkey] = self.__getSingleVocabularyElement(self.lomxml,xpath)
        elif isinstance(self.lom[lomkey], list):
            self.lom[lomkey] = self.__getMultipleVocabularyElement(self.lomxml,xpath)
        else:
            raise LookupError("bad type definition in empty LOM")


    def __setCatalogEntryElement(self,xpath,lomkey):
        """ Sets the catalogs and entries from the xpath in the specified lomkey. """
        element = self.lomxml.xpath(xpath, namespaces=self.ns)
        if element:
            self.lom[lomkey] = self.__getCatalogEntryElement(element)


    def __setContributeElement(self,xpath,lomkey):
        """ Sets each contribute from the xpath in a data structure. """
        element = self.lomxml.xpath(xpath, namespaces=self.ns)
        if element:
            for e in element:
                data = {"role": "", "entity": [], "date": "", "vcard": []}
                data["role"] = self.__getSingleVocabularyElement(e,"lom:role")
                data["entity"] = self.__getMultipleElement(e, "lom:centity/lom:vcard")
                data["date"] = self.__getDurationElement(e, "lom:date")

                for entity in data["entity"]:
                    data["vcard"].append(self.__setVcard(entity))

                self.lom[lomkey].append(data)

    def __setVcard(self,entity):
        """ Simplified parsing for some vcard attributes. """
        data = {}
        try:
            v = vobject.readOne(entity)
        except Exception:
            return data

        if "fn" in v.contents:
            data["fn"] = v.fn.value
        if "n" in v.contents:
            data["n"] = v.n.value
        if "org" in v.contents:
            data["org"] = v.org.value[0]
        if "uid" in v.contents:
            data["uid"] = v.uid.value

        return data

    def __getDurationElement(self,etreepart,xpath):
        element = etreepart.xpath(xpath, namespaces=self.ns)
        if element:
            data = {"datetime": "", "description": ""}
            data["datetime"] = self.__getSingleElement(element[0],"lom:datetime")
            data["description"] = self.__getSingleElement(element[0],"lom:description/lom:langstring[@xml:lang='" + self.lang + "']")
            return data
        else:
            return ""

    def __getCatalogEntryElement(self,etreepart):
        """ Return all catalogentry elements as a list of dictionaries. """
        catalogentries = []
        for e in etreepart:
            data = {"catalog": "", "entry": ""}
            data["catalog"] = self.__getSingleElement(e,"lom:catalog")
            data["entry"] = self.__getSingleElement(e,"lom:entry/lom:langstring")
            catalogentries.append(data)
        return catalogentries


    def __getSingleVocabularyElement(self,etreepart,xpath):
        element = etreepart.xpath(xpath, namespaces=self.ns)
        if element:
            data = {"source": "", "value": ""}
            data["source"] = self.__getSingleElement(element[0],"lom:source/lom:langstring")
            data["value"] = self.__getSingleElement(element[0],"lom:value/lom:langstring")
            return data
        else:
            return ""

    def __getMultipleVocabularyElement(self,etreepart,xpath):
        data = []
        element = etreepart.xpath(xpath, namespaces=self.ns)
        if element:
            for e in element:
                vocab = {"source": "", "value": ""}
                vocab["source"] = self.__getSingleElement(e,"lom:source/lom:langstring")
                vocab["value"] = self.__getSingleElement(e,"lom:value/lom:langstring")
                data.append(vocab)
        return data

    def __getSingleElement(self,etreepart,xpath):
        element = etreepart.xpath(xpath, namespaces=self.ns)
        if element:
            if element[0].text:
                return element[0].text
            else:
                return ""
        else:
            return ""

    def __getMultipleElement(self,etreepart,xpath):
        data = []
        element = etreepart.xpath(xpath, namespaces=self.ns)
        if element:
            for e in element:
                if e.text:
                    data.append(e.text)
                else:
                    data.append("")
        return data
