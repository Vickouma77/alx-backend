# 0x01-caching
## Learning Objectives
### General
* What a caching system is
* What FIFO means
* What LIFO means
* What LRU means
* What MRU means
* What LFU means
* What the purpose of a caching system
* What limits a caching system have
## Requirements
### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Tasks
### 0. Basic dictionary
Create a class BasicCache that inherits from BaseCaching and is a caching system:
* You must use self.cache_data - dictionary from the parent class BaseCaching
* You can overload def put(self, key, item): and def get(self, key): from BaseCaching
* def put(self, key, item): must assign to the dictionary self.cache_data the item value for the key key.
* If key or item is None, this method should not do anything.
* If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
* you must discard the first item put in cache (FIFO algorithm)
* you must print DISCARD: with the key discarded and following by a new line
* def get(self, key): must return the value in self.cache_data linked to key.
* If key is None or if the key doesn’t exist in self.cache_data, return None.
