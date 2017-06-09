# PyLom
This is a Python library for reading IMS-LOM files.

# Howto
The LomReader class accepts a *language* argument which is used to parse only those language-specific langstring elements.

## basic example
```python
from pylom.reader import LomReader

lomreader = LomReader()
lomreader.parsePath("test/records/ims-complete.xml")

print(lomreader.lom["title"])
# Bloodbath of B-R5RB
```

# Dependencies
- [lxml](http://lxml.de/)

# To Do
- implement all LOM fields
- selectable read using fieldset
- support IEEE binding
- cleanup options, trim, unique, etc
- application profile validation
- value validation
