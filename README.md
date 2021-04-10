# HashTable

HashTable is a python library (Data Structure) it has almost all functionality of dictionary in python.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install HashTable.

```bash
pip install hashtable-python
```

## Usage

```python
from hashtable import HashTable

my_hashtable = HashTable(5)  # Create instance of hashtable with fixed sized 5
my_hashtable['mango'] = 100  # Creating key='mango' and value=100
my_hashtable.items()         # Returns list of tuples of key and value [(kay, value),...)
my_hashtable.keys()          # Returns list of keys
my_hashtable.values()        # Returns list of values
my_hashtable['mango']        # Returns value of specified key
my_hashtable.delete('mango') # Deletes item in the specified key
```


## License
[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2021 Rosun GV