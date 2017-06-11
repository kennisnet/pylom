# -*- coding: utf-8 -*-

from lxml import etree

class LomReader:
    def __init__(self,language="en"):
        self.lomxml = None
        self.ns = {'lom': 'http://www.imsglobal.org/xsd/imsmd_v1p2'}
        self.lang = language
        self.__setEmptyLom()


    def parsePath(self,path):
        """ Parse LOM XML based on path. """
        try:
            self.lomxml = etree.parse(path)
        except Exception as e:
            raise RuntimeError(e)

        if self.lomxml:
            self.parseFull()


    def parseFull(self):
        """ Parses using all __setField* methods. """
        for attribute in dir(self):
            if attribute[0:20] == "_LomReader__setField":
                getattr(self,attribute)()


    def setCustomEmptyLom(self,customdict):
        """ Sets a custom empty LOM dictionary. In this, the user can specify
        how answers should be formatted, for example always return the first title."""
        if isinstance(customdict, dict):
            self.lom = customdict
        else:
            raise TypeError("custom empty LOM should be a dictionary")


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
            "learningresourcetype": [],
            "intendedenduserrole": [],
            "context": [],
            "typicalagerange": [],
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
        self.__setDurationElement("/lom:lom/lom:technical/lom:duration","duration")

    def __setFieldLearningResourceType(self):
        self.__setVocabularyElement("/lom:lom/lom:educational/lom:learningresourcetype", "learningresourcetype")

    def __setFieldIntendedEndUserRole(self):
        self.__setVocabularyElement("/lom:lom/lom:educational/lom:intendedenduserrole", "intendedenduserrole")

    def __setFieldContext(self):
        self.__setVocabularyElement("/lom:lom/lom:educational/lom:context", "context")

    def __setFieldTypicalAgeRange(self):
        self.__setElement("/lom:lom/lom:educational/lom:typicalagerange/lom:langstring", "typicalagerange")

    def __setFieldCost(self):
        self.__setVocabularyElement("/lom:lom/lom:rights/lom:cost", "cost")

    def __setFieldCopyrightAndOtherRestrictions(self):
        self.__setVocabularyElement("/lom:lom/lom:rights/lom:copyrightandotherrestrictions", "copyrightandotherrestrictions")

    def __setFieldCopyrightDescription(self):
        self.__setElement("/lom:lom/lom:rights/lom:description/lom:langstring[@xml:lang='" + self.lang + "']", "copyrightdescription")

    def __setFieldRelation(self):
        self.__setRelationElement()

    def __setFieldClassification(self):
        self.__setClassificationElement()


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
        element = self.lomxml.xpath(xpath, namespaces=self.ns)
        if element:
            if isinstance(self.lom[lomkey], str):
                self.lom[lomkey] = self.__getVocabularyElement(element[0])
            elif isinstance(self.lom[lomkey], list):
                for e in element:
                    self.lom[lomkey].append(self.__getVocabularyElement(e))
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
                data = {"role": {}, "entity": [], "date": ""}
                role = e.xpath("lom:role", namespaces=self.ns)
                if role:
                    data["role"] = self.__getVocabularyElement(role[0])
                data["entity"] = self.__getMultipleElement(e, "lom:centity/lom:vcard")
                data["date"] = self.__getSingleElement(e, "lom:date/lom:datetime")

                self.lom[lomkey].append(data)


    def __setDurationElement(self,xpath,lomkey):
        element = self.lomxml.xpath(xpath, namespaces=self.ns)
        if element:
            self.lom[lomkey] = self.__getDurationElement(element[0])


    def __setRelationElement(self):
        """ Parses the relation element. """
        element = self.lomxml.xpath("/lom:lom/lom:relation", namespaces=self.ns)
        if element:
            for e in element:
                data = {"kind": {}, "resource": {}}
                kind = e.xpath("lom:kind", namespaces=self.ns)
                if kind:
                    data["kind"] = self.__getVocabularyElement(kind[0])
                resource = e.xpath("lom:resource", namespaces=self.ns)
                if resource:
                    res_data = {"description": [], "catalogentry": []}
                    res_data["description"] = self.__getMultipleElement(resource[0],"lom:description/lom:langstring[@xml:lang='" + self.lang + "']")
                    catalogentry = resource[0].xpath("lom:catalogentry", namespaces=self.ns)
                    if catalogentry:
                        res_data["catalogentry"] = self.__getCatalogEntryElement(catalogentry)
                    data["resource"] = res_data

                self.lom["relation"].append(data)


    def __setClassificationElement(self):
        """ Parses the classification element. """
        element = self.lomxml.xpath("/lom:lom/lom:classification", namespaces=self.ns)
        if element:
            for e in element:
                data = {"purpose": {}, "taxonpath": []}
                purpose = e.xpath("lom:purpose", namespaces=self.ns)
                if purpose:
                    data["purpose"] = self.__getVocabularyElement(purpose[0])
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


    def __getVocabularyElement(self,etreepart):
        """Just return a source-value dictionary based on an Etree element. """
        data = {"source": "", "value": ""}
        data["source"] = self.__getSingleElement(etreepart,"lom:source/lom:langstring")
        data["value"] = self.__getSingleElement(etreepart,"lom:value/lom:langstring")
        return data

    def __getDurationElement(self,etreepart):
        """ Return a datetime-description dictionary based on an Etree element. """
        data = {"datetime": "", "description": ""}
        data["datetime"] = self.__getSingleElement(etreepart,"lom:datetime")
        data["description"] = self.__getSingleElement(etreepart,"lom:description/lom:langstring[@xml:lang='" + self.lang + "']")
        return data

    def __getCatalogEntryElement(self,etreepart):
        """ Return all catalogentry elements as a list of dictionaries. """
        catalogentries = []
        for e in etreepart:
            data = {"catalog": "", "entry": ""}
            data["catalog"] = self.__getSingleElement(e,"lom:catalog")
            data["entry"] = self.__getSingleElement(e,"lom:entry/lom:langstring")
            catalogentries.append(data)
        return catalogentries


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
