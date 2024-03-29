"""

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |
 |  Methods defined here:
 |
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None

Dictionary is just like maps with key value pair
Symbol = {}

"""

Dict1 = {'Fruit': 'Orange', 'Animal': 'Tiger', 1: 'One', 'Two': 2}
Dict2 = {'FName': 'Dhiraj', 'LName': 'Kumar'}
Dict4 = {'FName': 'Dhiraj', 'LName': 'Sharma'}

print(Dict2)  # {'FName': 'Dhiraj', 'LName': 'Kumar'}
Dict2.clear()
print(Dict2)  # {}

Dict3 = Dict1.copy()
print(Dict3)  # {'Fruit': 'Orange', 'Animal': 'Tiger', 1: 'One', 'Two': 2}

print(Dict1['Fruit'])  # Orange
# print(Dict1['Place'])  # KeyError: 'Place'

print(Dict1.get('Place'))  # None

print(Dict3.items())  # dict_items([('Fruit', 'Orange'), ('Animal', 'Tiger'), (1, 'One'), ('Two', 2)])

print(Dict1.keys())  # dict_keys(['Fruit', 'Animal', 1, 'Two'])

print(Dict1.values())  # dict_values(['Orange', 'Tiger', 'One', 2])

Dict1.update(Dict4)
print(Dict1)  # {'Fruit': 'Orange', 'Animal': 'Tiger', 1: 'One', 'Two': 2, 'FName': 'Dhiraj', 'LName': 'Kumar'}

Dict4.update({'MName': 'Kumar'})
print(Dict4)  # {'FName': 'Dhiraj', 'LName': 'Sharma', 'MName': 'Kumar'}

Dict4.pop('MName')
print(Dict4)  # {'FName': 'Dhiraj', 'LName': 'Sharma'}
Dict1.popitem()
print(Dict1)  # {'Fruit': 'Orange', 'Animal': 'Tiger', 1: 'One', 'Two': 2, 'FName': 'Dhiraj'}

employeeIdList = [100, 101, 102, 103]
Dict5 = dict.fromkeys(employeeIdList)
print(Dict5)  # {100: None, 101: None, 102: None, 103: None}

Dict5.update({102: 'Dhiraj'})
print(Dict5)  # {100: None, 101: None, 102: 'Dhiraj', 103: None}
