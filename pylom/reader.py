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
        self.__setLanguage()
        self.__setDescription()
        self.__setKeyword()
        self.__setAggregationLevel()
        self.__setVersion()
        self.__setStatus()
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
            "language": [],
            "description": [],
            "keyword": [],
            "aggregationlevel": "",
            "version": "",
            "status": "",
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
                data = {"source": "", "value": ""}
                source = element[0].xpath("lom:source/lom:langstring", namespaces=self.ns)
                if source:
                    data["source"] = source[0].text
                value = element[0].xpath("lom:value/lom:langstring", namespaces=self.ns)
                if value:
                    data["value"] = value[0].text
                self.lom[lomkey] = data
            elif isinstance(self.lom[lomkey], list):
                for e in element:
                    data = {"source": "", "value": ""}
                    source = e.xpath("lom:source/lom:langstring", namespaces=self.ns)
                    if source:
                        data["source"] = source[0].text
                    value = e.xpath("lom:value/lom:langstring", namespaces=self.ns)
                    if value:
                        data["value"] = value[0].text
                    self.lom[lomkey].append(data)
            else:
                raise LookupError("bad type definition in empty LOM")
