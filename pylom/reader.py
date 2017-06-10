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
        self.lomxml = etree.parse(path)

        if self.lomxml:
            self.parseFull()


    def parseFull(self):
        self.__setTitle()
        self.__setCatalogEntry()
        self.__setLanguage()
        self.__setDescription()
        self.__setKeyword()
        self.__setAggregationLevel()
        self.__setVersion()
        self.__setStatus()
        self.__setContribute()
        self.__setMetaCatalogEntry()
        self.__setMetaContribute()
        self.__setMetadataScheme()
        self.__setMetaLanguage()
        self.__setFormat()
        self.__setLocation()
        self.__setLearningResourceType()
        self.__setIntendedEndUserRole()
        self.__setContext()
        self.__setTypicalAgeRange()
        self.__setCost()
        self.__setCopyrightAndOtherRestrictions()
        self.__setCopyrightDescription()


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
            "aggregationlevel": "",
            "version": "",
            "status": "",
            "contribute": [],
            "metacatalogentry": [],
            "metacontribute": [],
            "metadatascheme": [],
            "metalanguage": "",
            "format": [],
            "location": "",
            "learningresourcetype": [],
            "intendedenduserrole": [],
            "context": [],
            "typicalagerange": [],
            "cost": "",
            "copyrightandotherrestrictions": "",
            "copyrightdescription": ""
                }

    def __setTitle(self):
        self.__setElement("/lom:lom/lom:general/lom:title/lom:langstring[@xml:lang='" + self.lang + "']", "title")

    def __setCatalogEntry(self):
        self.__setCatalogEntryElement("/lom:lom/lom:general/lom:catalogentry", "catalogentry")

    def __setLanguage(self):
        self.__setElement("/lom:lom/lom:general/lom:language","language")

    def __setDescription(self):
        self.__setElement("/lom:lom/lom:general/lom:description/lom:langstring[@xml:lang='" + self.lang + "']", "description")

    def __setKeyword(self):
        self.__setElement("/lom:lom/lom:general/lom:keyword/lom:langstring[@xml:lang='" + self.lang + "']", "keyword")

    def __setAggregationLevel(self):
        self.__setVocabularyElement("/lom:lom/lom:general/lom:aggregationlevel", "aggregationlevel")

    def __setVersion(self):
        self.__setElement("/lom:lom/lom:lifecycle/lom:version/lom:langstring","version")

    def __setStatus(self):
        self.__setVocabularyElement("/lom:lom/lom:lifecycle/lom:status", "status")

    def __setContribute(self):
        self.__setContributeElement("/lom:lom/lom:lifecycle/lom:contribute", "contribute")

    def __setMetaCatalogEntry(self):
        self.__setCatalogEntryElement("/lom:lom/lom:metametadata/lom:catalogentry", "metacatalogentry")

    def __setMetaContribute(self):
        self.__setContributeElement("/lom:lom/lom:metametadata/lom:contribute", "metacontribute")

    def __setMetadataScheme(self):
        self.__setElement("/lom:lom/lom:metametadata/lom:metadatascheme","metadatascheme")

    def __setMetaLanguage(self):
        self.__setElement("/lom:lom/lom:metametadata/lom:language","metalanguage")

    def __setFormat(self):
        self.__setElement("/lom:lom/lom:technical/lom:format","format")

    def __setLocation(self):
        self.__setElement("/lom:lom/lom:technical/lom:location","location")

    def __setLearningResourceType(self):
        self.__setVocabularyElement("/lom:lom/lom:educational/lom:learningresourcetype", "learningresourcetype")

    def __setIntendedEndUserRole(self):
        self.__setVocabularyElement("/lom:lom/lom:educational/lom:intendedenduserrole", "intendedenduserrole")

    def __setContext(self):
        self.__setVocabularyElement("/lom:lom/lom:educational/lom:context", "context")

    def __setTypicalAgeRange(self):
        self.__setElement("/lom:lom/lom:educational/lom:typicalagerange/lom:langstring", "typicalagerange")

    def __setCost(self):
        self.__setVocabularyElement("/lom:lom/lom:rights/lom:cost", "cost")

    def __setCopyrightAndOtherRestrictions(self):
        self.__setVocabularyElement("/lom:lom/lom:rights/lom:copyrightandotherrestrictions", "copyrightandotherrestrictions")

    def __setCopyrightDescription(self):
        self.__setElement("/lom:lom/lom:rights/lom:description/lom:langstring[@xml:lang='" + self.lang + "']", "copyrightdescription")


    def __setElement(self,xpath,lomkey):
        """ Sets the value from the xpath in the specified lomkey. """
        element = self.lomxml.xpath(xpath, namespaces=self.ns)
        if element:
            if isinstance(self.lom[lomkey], str):
                self.lom[lomkey] = element[0].text
            elif isinstance(self.lom[lomkey], list):
                for e in element:
                    self.lom[lomkey].append(e.text)
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
            if isinstance(self.lom[lomkey], list):
                for e in element:
                    data = {"catalog": "", "entry": ""}
                    catalog = e.xpath("lom:catalog", namespaces=self.ns)
                    if catalog:
                        data["catalog"] = catalog[0].text
                    entry = e.xpath("lom:entry/lom:langstring", namespaces=self.ns)
                    if entry:
                        data["entry"] = entry[0].text
                    self.lom[lomkey].append(data)
            else:
                raise LookupError("bad type definition in empty LOM")


    def __setContributeElement(self,xpath,lomkey):
        """ Sets each contribute from the xpath in a data structure. """
        element = self.lomxml.xpath(xpath, namespaces=self.ns)
        if element:
            for e in element:
                data = {"role": {}, "entity": [], "date": ""}
                role = e.xpath("lom:role", namespaces=self.ns)
                if role:
                    data["role"] = self.__getVocabularyElement(role[0])
                entity = e.xpath("lom:centity/lom:vcard", namespaces=self.ns)
                if entity:
                    for ent in entity:
                        data["entity"].append(ent.text)
                date = e.xpath("lom:date/lom:datetime", namespaces=self.ns)
                if date:
                    data["date"] = date[0].text

                self.lom[lomkey].append(data)


    def __getVocabularyElement(self,etreepart):
        """Just return a source-value dictionary based on an Etree element. """
        data = {"source": "", "value": ""}
        source = etreepart.xpath("lom:source/lom:langstring", namespaces=self.ns)
        if source:
            data["source"] = source[0].text
        value = etreepart.xpath("lom:value/lom:langstring", namespaces=self.ns)
        if value:
            data["value"] = value[0].text

        return data
