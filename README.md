# PyLom
This is a Python library for reading IMS-LOM files. It's tested for Python 2.7 and 3.4.
Almost all fields are supported, but only one language will be supported for language-specific langstring elements.

## Usage
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

## Dependencies
- [lxml](http://lxml.de/)
- [setuptools](https://github.com/pypa/setuptools)

## To Do
- implement all LOM fields
- support IEEE binding
- cleanup options, trim, unique, etc
- application profile validation
- value validation
