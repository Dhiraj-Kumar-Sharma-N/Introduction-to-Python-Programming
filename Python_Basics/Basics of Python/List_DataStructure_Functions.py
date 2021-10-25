"""
Help on list object:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
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
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |
 |  __imul__(self, value, /)
 |      Implement self*=value.
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
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |
 |  append(self, object, /)
 |      Append object to the end of the list.
 |
 |  clear(self, /)
 |      Remove all items from list.
 |
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  insert(self, index, object, /)
 |      Insert object before index.
 |
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
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

List is mutable and collection of data which can be modified
Symbol = []

"""

List1 = [2, 6, 9, 4, 6, 5, 1]
List2 = ['Dhiraj', 'Kumar', 'Sharma']
List2C = ['Dhiraj', 'Kumar', 'Sharma']
List1A = [22, 11]

print(List2)  # ['Dhiraj', 'Kumar', 'Sharma']

print(List1.__add__(List1A))  # [2, 6, 9, 4, 6, 5, 1, 22, 11]

print(List1.__contains__('Dhiraj'))  # False
print(List2.__contains__('Dhiraj'))  # True

List1.__delitem__(1)  # Index 1
print(List1)  # [2, 9, 4, 6, 5, 1]

print(List2.__eq__(List2C))  # True
print(List1.__eq__(List2C))  # False

List1A.extend(List1)
print(List1A)  # [22, 11, 2, 9, 4, 6, 5, 1]

List2.append('N')
print(List2)  # ['Dhiraj', 'Kumar', 'Sharma', 'N']

List2C.clear()
print(List2C)  # []

List3 = List1A.copy()
print(List3)  # [22, 11, 2, 9, 4, 6, 5, 1]

List4 = [2, 5, 6, 9, 2, 4, 4, 7, 2, 0, 6]
print(List4.count(2))  # 3
print(List4.count(4))  # 2

print(List2.index('Kumar'))  # 1

# list.insert(pos, element)
List2.insert(2, '99')
print(List2)  # ['Dhiraj', 'Kumar', '99', 'Sharma', 'N']

List2.pop()
print(List2)  # ['Dhiraj', 'Kumar', '99', 'Sharma']
List2.pop(2)
print(List2)  # ['Dhiraj', 'Kumar', 'Sharma']

List1.sort()
print(List1)  # [1, 2, 4, 5, 6, 9]

List1.remove(2)
print(List1)  # [1, 4, 5, 6, 9]

List1.reverse()
print(List1)  # [9, 6, 5, 4, 1]
