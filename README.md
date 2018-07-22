# PyLom
This is a Python library for reading and writing IMS-LOM files. It's tested for Python 2.7 and 3.4.
Almost all fields are supported, but only one language will be supported for language-specific langstring elements.

## Reader Usage
Basically, import the class and tell it to parse a lom file. The parsed data will be available in the *lom* attribute dict.
By default, it reads the *en* language, but another can be set on init.
To start parsing, initialize the class and use one of two public methods, *parsePath* or *parseString*.

### basic example
```python
from pylom.reader import LomReader

lomreader = LomReader()
lomreader.parsePath("test/records/ims-complete.xml")

print(lomreader.lom["title"])
# Bloodbath of B-R5RB
```

### fieldset example
```python
from pylom.reader import LomReader

lomreader = LomReader()
lomreader.parsePath("test/records/ims-complete.xml", ["title","location"])

# Only the title and location field results are available in the lom dict
```

## Writer Usage
The writer class is used by providing it with a dictionary with all the values you want in your record. Like the reader class
the instance can be called with a language argument for all the langstring elements. After parsing, the lom record is available
in the *lom* attribute.

### basic example
```python
from pylom.writer import LomWriter

lomwriter = LomWriter()
lomwriter.parseDict({"title": "Bloodbath of B-R5RB"})
print(lomwriter.lom)
```

### custom vocabularies
By default, all vocabulary sources are set to *LOMv1.0*, but they can be changed by setting the *vocabulary_sources* after
creating the instance.

```python
from pylom.writer import LomWriter

lomwriter = LomWriter()
lomwriter.vocabulary_sources.update( { "aggregationlevel": "my-source" } )
lomwriter.parseDict({"aggregationlevel": "2"})
print(lomwriter.lom)
```

### input values
For easy implementation, many of the values can be provided as needed. For instance, any basic element or langstring element
can be provided as string or as a list of strings.

Vocabulary elements can be provided as a single string or a list of strings, using the class default vocabulary source, or as
a single dictionary, with separate source and value values.

More detailed examples can be inferred from the *test_writer_elements* test cases.

```python
from pylom.writer import LomWriter

lomwriter = LomWriter()
lomdict = {
    "title": "Bloodbath of B-R5RB",
    "keyword": ["Eve Online", "Halloween War"],
    "aggregationlevel": {"source": "my-source", "value": "2" },
    "context": ["school", "higher education"] }

lomwriter.parseDict(lomdict)
print(lomwriter.lom)
```

## Dependencies
- [lxml](http://lxml.de/)
- [setuptools](https://github.com/pypa/setuptools)

## To Do
### Reader
- implement all LOM fields
- support IEEE binding
- cleanup options, trim, unique, etc
- application profile validation
- value validation

### Writer
- vocabulary, provide list of source/value dicts
- more LOM-spec aware validation, for instance, prevent multiple title fields
