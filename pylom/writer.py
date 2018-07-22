# -*- coding: utf-8 -*-

""" LomWriter
Some more in-depth information on how this class works.

Different type of methodes:
 __setField* sets the individual fields
 __check*Element validates the different kinds of input that should be supported for that element and returns element, single or in list
 __setField, actually sets the returned element or list of elements
 __get*Element return the actual etree parts
"""

from pylom.lom import Lom
from lxml import etree

class LomWriter(Lom):
    def __init__(self,language="en"):
        Lom.__init__(self,language)
        self.lomns = '{http://www.imsglobal.org/xsd/imsmd_v1p2}'
        self.lomxml = etree.Element(self.lomns + 'lom', nsmap={"lom": 'http://www.imsglobal.org/xsd/imsmd_v1p2', "xsi": "http://www.w3.org/2001/XMLSchema-instance"})
        self.lom = ""

        # these will not be appended if they have no children
        self.general = etree.Element(self.lomns + "general")
        self.lifecycle = etree.Element(self.lomns + "lifecycle")
        self.metametadata = etree.Element(self.lomns + "metametadata")
        self.technical = etree.Element(self.lomns + "technical")
        self.educational = []
        self.rights = etree.Element(self.lomns + "rights")
        self.relation = []
        self.classification = []

        # used in educational, relation and classification
        self.tmp_element = None

        # python 2/3 compatible basestring instance checking
        try:
            basestring
            self.basestring = basestring
        except NameError:
            self.basestring = str


    def parseDict(self,lomdict):
        """ Parses dict into LOM string and sets this in the lom attribute. """
        for fieldkey in self.fmethods:
            if fieldkey in lomdict:
                attribute = "_" + self.__class__.__name__ + self.fmethods[fieldkey]
                getattr(self,attribute)(lomdict[fieldkey])

        self.__compileLom()


    def __compileLom(self):
        """ Aggregates all the main subelements and writes object to string. """
        if self.general.getchildren():
            self.lomxml.append(self.general)
        if self.lifecycle.getchildren():
            self.lomxml.append(self.lifecycle)
        if self.metametadata.getchildren():
            self.lomxml.append(self.metametadata)
        if self.technical.getchildren():
            self.lomxml.append(self.technical)
        for e in self.educational:
            if e.getchildren():
                self.lomxml.append(e)
        if self.rights.getchildren():
            self.lomxml.append(self.rights)
        for e in self.relation:
            self.lomxml.append(e)
        for e in self.classification:
            self.lomxml.append(e)

        self.lom = etree.tostring(self.lomxml, pretty_print=True)


    def __setFieldTitle(self,value):
        self.__setField(self.general,self.__checkLangstringElement("title",value))

    def __setFieldCatalogEntry(self,value):
        for v in value:
            self.__setField(self.general,self.__checkCatalogEntryElement(v))

    def __setFieldLanguage(self,value):
        self.__setField(self.general,self.__checkElement("language",value))

    def __setFieldDescription(self,value):
        self.__setField(self.general,self.__checkLangstringElement("description",value))

    def __setFieldKeyword(self,value):
        self.__setField(self.general,self.__checkLangstringElement("keyword",value))

    def __setFieldCoverage(self,value):
        self.__setField(self.general,self.__checkLangstringElement("coverage",value))

    def __setFieldStructure(self,value):
        self.__setField(self.general,self.__checkVocabularyElement("structure",value))

    def __setFieldAggregationLevel(self,value):
        self.__setField(self.general,self.__checkVocabularyElement("aggregationlevel",value))

    def __setFieldVersion(self,value):
        self.__setField(self.lifecycle,self.__checkLangstringElement("version",value,"x-none"))

    def __setFieldStatus(self,value):
        self.__setField(self.lifecycle,self.__checkVocabularyElement("status",value))

    def __setFieldContribute(self,value):
        for v in value:
           self.__setContributeElement(self.lifecycle,v)

    def __setFieldMetaCatalogEntry(self,value):
        for v in value:
            self.__setField(self.metametadata,self.__checkCatalogEntryElement(v))

    def __setFieldMetaContribute(self,value):
        for v in value:
           self.__setContributeElement(self.metametadata,v)

    def __setFieldMetadataScheme(self,value):
        self.__setField(self.metametadata,self.__checkElement("metadatascheme",value))

    def __setFieldMetaLanguage(self,value):
        self.__setField(self.metametadata,self.__checkElement("language",value))

    def __setFieldFormat(self,value):
        self.__setField(self.technical,self.__checkElement("format",value))

    def __setFieldSize(self,value):
        self.__setField(self.technical,self.__checkElement("size",value))

    def __setFieldLocation(self,value):
        self.__setField(self.technical,self.__checkElement("location",value))

    def __setFieldDuration(self,value):
        self.__setField(self.technical,self.__checkDateTime("duration",value))

    def __setFieldEducational(self,value):
        for v in value:
            self.tmp_element = self.__getElement("educational")

            if "interactivitytype" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("interactivitytype",v["interactivitytype"]))
            if "learningresourcetype" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("learningresourcetype",v["learningresourcetype"]))
            if "interactivitylevel" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("interactivitylevel",v["interactivitylevel"]))
            if "semanticdensity" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("semanticdensity",v["semanticdensity"]))
            if "intendedenduserrole" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("intendedenduserrole",v["intendedenduserrole"]))
            if "context" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("context",v["context"]))
            if "typicalagerange" in v:
                self.__setField(self.tmp_element, self.__checkLangstringElement("typicalagerange",v["typicalagerange"],"x-none"))
            if "difficulty" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("difficulty",v["difficulty"]))
            if "typicallearningtime" in v:
                self.__setField(self.tmp_element, self.__checkDateTime("typicallearningtime",v["typicallearningtime"]))
            if "description" in v:
                self.__setField(self.tmp_element, self.__checkVocabularyElement("learningresourcetype",v["learningresourcetype"]))
            if "language" in v:
                self.__setField(self.tmp_element, self.__checkElement("language",v["language"]))

            self.educational.append(self.tmp_element)
            self.tmp_element = None

    def __setFieldCost(self,value):
        self.__setField(self.rights,self.__checkVocabularyElement("cost",value))

    def __setFieldCopyrightAndOtherRestrictions(self,value):
        self.__setField(self.rights,self.__checkVocabularyElement("copyrightandotherrestrictions",value))

    def __setFieldCopyrightDescription(self,value):
        self.__setField(self.rights,self.__checkLangstringElement("description",value))

    def __setFieldRelation(self,value):
        for v in value:
            if "kind" not in v or "resource" not in v:
                raise ValueError("bad definition for input field: relation")

            self.tmp_element = self.__getElement("relation")
            self.__setField(self.tmp_element, self.__checkVocabularyElement("kind",v["kind"]))

            if not isinstance(v["resource"], dict) or not "catalogentry" in v["resource"]:
                raise ValueError("bad definition for input field: relation resource")

            resource = self.__getElement("resource")
            if "description" in v["resource"]:
                description = self.__checkLangstringElement("description", v["resource"]["description"])
                if isinstance(description,list):
                    for e in description:
                        resource.append(e)
                else:
                    resource.append(description)

            for c in v["resource"]["catalogentry"]:
                resource.append(self.__checkCatalogEntryElement(c))

            self.tmp_element.append(resource)
            self.relation.append(self.tmp_element)
            self.tmp_element = None

    def __setFieldClassification(self,value):
        for v in value:
            if "purpose" not in v or "taxonpath" not in v:
                raise ValueError("bad definition for input field: classification")

            self.tmp_element = self.__getElement("classification")
            self.__setField(self.tmp_element, self.__checkVocabularyElement("purpose",v["purpose"]))
            if not isinstance(v["taxonpath"], list):
                raise ValueError("bad definition for input field: classification taxonpath")

            for tp in v["taxonpath"]:
                if "source" not in tp or "taxon" not in tp:
                    raise ValueError("bad definition for input field: classification taxonpath")

                taxonpath = self.__getElement("taxonpath")

                if not isinstance(tp["source"], str) or not tp["source"]:
                    raise ValueError("bad definition for input field: classification taxonpath source")
                taxonpath.append(self.__getLangstringElement("source", tp["source"]))

                if not isinstance(tp["taxon"], list):
                    raise ValueError("bad definition for input field: classification taxonpath taxon")

                for t in tp["taxon"]:
                    if not self.__validateTaxon(t):
                        raise ValueError("bad definition for input field: classification taxonpath taxon")

                    taxon = self.__getElement("taxon")
                    taxon.append(self.__getElement("id", t["id"]))
                    taxon.append(self.__getLangstringElement("entry", t["entry"]))
                    taxonpath.append(taxon)

                self.tmp_element.append(taxonpath)

            self.classification.append(self.tmp_element)
            self.tmp_element = None


    def __setField(self,root,element):
        """ Append element; single or from list. """
        if isinstance(element,list):
            for e in element:
                root.append(e)
        else:
            root.append(element)


    def __checkElement(self,field,value):
        if isinstance(value, self.basestring) and value:
            return self.__getElement(field,value)
        elif isinstance(value, list):
            l = []
            for v in (v for v in value if v):
                l.append(self.__getElement(field,v))
            return l
        else:
            raise ValueError("bad definition for input field: " + field)

    def __checkLangstringElement(self,field,value,language=None):
        if isinstance(value, self.basestring) and value:
            return self.__getLangstringElement(field,value,language)
        elif isinstance(value, list):
            l = []
            for v in (v for v in value if v):
                l.append(self.__getLangstringElement(field,v,language))
            return l
        else:
            raise ValueError("bad definition for input field: " + field)

    def __checkCatalogEntryElement(self,value):
        if isinstance(value, dict) and self.__validateCatalogEntry(value):
            return self.__getCatalogEntryElement(value)
        else:
            raise ValueError("bad definition for input field: catalogentry")

    def __checkVocabularyElement(self,field,value,source=None):
        """ Parses value to one or more vocabulary elements.
        vocabulary values can be string, add one and lookup source,
        list of values and lookup source as well,
        or dict, or list of dicts, specifying the source. """
        if isinstance(value, self.basestring) and value:
            return self.__getVocabularyElement(field,value,source)
        elif isinstance(value, dict) and self.__validateVocabulary(value):
            return self.__getVocabularyElement(field,value["value"],value["source"])
        elif isinstance(value, list) and value:
            l = []
            if isinstance(value[0], self.basestring):
                for v in (v for v in value if v):
                    l.append(self.__getVocabularyElement(field,v,source))
            else:
                # TODO support list of source/value dicts
                raise ValueError("bad definition for input field: " + field)
            return l
        else:
            raise ValueError("bad definition for input field: " + field)

    def __checkDateTime(self,field,value):
        if isinstance(value, str) and value:
            date = self.__getElement(field)
            date.append(self.__getElement("datetime",value))
            return date
        elif isinstance(value, dict) and self.__validateDateTime(value):
            date = self.__getElement(field)
            date.append(self.__getElement("datetime",value["datetime"]))
            date.append(self.__getLangstringElement("description",value["description"]))
            return date
        else:
            raise ValueError("bad definition for input field: date")


    def __setContributeElement(self,root,value):
        # initial input validation
        if "role" not in value or ("entity" not in value and "date" not in value):
            raise ValueError("bad definition for input field: contribute, provide a role and an entity or date")

        contribute = self.__getElement("contribute")
        role_default_source = self.vocabulary_sources[self.__getElementName(root) + "-contribute-role"]
        contribute.append(self.__checkVocabularyElement("role",value["role"],role_default_source))

        if "entity" in value:
            if isinstance(value["entity"], str) and value["entity"]:
                entity = self.__getElement("centity")
                entity.append(self.__getElement("vcard",value["entity"]))
                contribute.append(entity)
            elif isinstance(value["entity"], list):
                for v in (v for v in value["entity"] if v):
                    entity = self.__getElement("centity")
                    entity.append(self.__getElement("vcard",value["entity"]))
                    contribute.append(entity)
            else:
                raise ValueError("bad definition for input field: contribute entity")

        if "date" in value:
            contribute.append(self.__checkDateTime("date",value["date"]))

        root.append(contribute)


    def __getElement(self,element,value=None):
        """ Returns a basic xml etree element, empty if no value. """
        e = etree.Element(self.lomns + element)
        if value:
            e.text = value
        return e

    def __getLangstringElement(self,element,value,language=None):
        if not language:
            language = self.lang

        e = etree.Element(self.lomns + element)
        lang = etree.Element(self.lomns + "langstring", {'{http://www.w3.org/XML/1998/namespace}lang':language})
        lang.text = value
        e.append(lang)
        return e

    def __getCatalogEntryElement(self,value):
        e = etree.Element(self.lomns + "catalogentry")
        e.append(self.__getElement("catalog",value["catalog"]))
        e.append(self.__getLangstringElement("entry",value["entry"],"x-none"))
        return e

    def __getVocabularyElement(self,element,value,source=None):
        if not source:
            source = self.vocabulary_sources[element]

        e = etree.Element(self.lomns + element)
        e.append(self.__getLangstringElement("source",source,"x-none"))
        e.append(self.__getLangstringElement("value",value,"x-none"))
        return e


    def __validateCatalogEntry(self,value):
        """ Validates provided dict in __setCatalogEntryElement. """
        if self.__validateDictionaryKey(value,"catalog") and self.__validateDictionaryKey(value,"entry"):
            return True
        else:
            return False
 
    def __validateVocabulary(self,value):
        """ Validates provided value in __setVocabularyElement. """
        if self.__validateDictionaryKey(value,"source") and self.__validateDictionaryKey(value,"value"):
            return True
        else:
            return False

    def __validateDateTime(self,value):
        """ Validates provided value in for a datetime. """
        if self.__validateDictionaryKey(value,"datetime") and self.__validateDictionaryKey(value,"description"):
            return True
        else:
            return False

    def __validateTaxon(self,value):
        """ Validates provided value in for a classification taxon. """
        if self.__validateDictionaryKey(value,"id") and self.__validateDictionaryKey(value,"entry"):
            return True
        else:
            return False

    def __validateDictionaryKey(self,value,key):
        """ Base validator used for validating input catalogentries and vocabularies. """
        if key in value and value[key] and isinstance(value[key], str):
            return True
        else:
            return False

    def __getElementName(self,element):
        """ Easy function to return namespaceless element name. """
        nslen = len(self.lomns)
        return element.tag[nslen:]
