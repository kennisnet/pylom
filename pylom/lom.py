# -*- coding: utf-8 -*-

from collections import OrderedDict

class Lom:
    def __init__(self,language):
        # the etree object
        self.lomxml = None
        # the language used in language specific langstring elements
        self.lang = language

        self.__setFieldMethods()

    def __setFieldMethods(self):
        """ Sets all field methods in correct order,
        indexed with the fieldset key. """
        self.fmethods = OrderedDict()
        self.fmethods["title"] = "__setFieldTitle"
        self.fmethods["catalogentry"] = "__setFieldCatalogEntry"
        self.fmethods["language"] = "__setFieldLanguage"
        self.fmethods["description"] = "__setFieldDescription"
        self.fmethods["keyword"] = "__setFieldKeyword"
        self.fmethods["coverage"] = "__setFieldCoverage"
        self.fmethods["structure"] = "__setFieldStructure"
        self.fmethods["aggregationlevel"] = "__setFieldAggregationLevel"
        self.fmethods["version"] = "__setFieldVersion"
        self.fmethods["status"] = "__setFieldStatus"
        self.fmethods["contribute"] = "__setFieldContribute"
        self.fmethods["metacatalogentry"] = "__setFieldMetaCatalogEntry"
        self.fmethods["metacontribute"] = "__setFieldMetaContribute"
        self.fmethods["metadatascheme"] = "__setFieldMetadataScheme"
        self.fmethods["metalanguage"] = "__setFieldMetaLanguage"
        self.fmethods["format"] = "__setFieldFormat"
        self.fmethods["size"] = "__setFieldSize"
        self.fmethods["location"] = "__setFieldLocation"
        self.fmethods["duration"] = "__setFieldDuration"
        self.fmethods["educational"] = "__setFieldEducational"
        self.fmethods["cost"] = "__setFieldCost"
        self.fmethods["copyrightandotherrestrictions"] = "__setFieldCopyrightAndOtherRestrictions"
        self.fmethods["copyrightdescription"] = "__setFieldCopyrightDescription"
        self.fmethods["relation"] = "__setFieldRelation"
        self.fmethods["classification"] = "__setFieldClassification"
