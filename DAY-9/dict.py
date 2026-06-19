Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> '''
... we can take key only immutable things such as int float...........
... we cannot take input as mutabel things such as llist set dict
... and
... value can be of any datatype it accepts
... '''
'\nwe can take key only immutable things such as int float...........\nwe cannot take input as mutabel things such as llist set dict\nand\nvalue can be of any datatype it accepts\n'
>>> 
>>> d = {}
>>> d[1] = 12
>>> d
{1: 12}
>>> d][124.2] = 'float'
SyntaxError: unmatched ']'
>>> 
>>> d[12.3] = 'float'
>>> d
{1: 12, 12.3: 'float'}
>>> d['demo'] = 'string'
>>> d
{1: 12, 12.3: 'float', 'demo': 'string'}
>>> d[2+3j] 'complex'
SyntaxError: invalid syntax
>>> d[2+3j] = 'complex'
>>> d
{1: 12, 12.3: 'float', 'demo': 'string', (2+3j): 'complex'}
>>> #we can access the elements using key
>>> d[12.3]
'float'
>>> '''
... if the element is not in the data it gives an error so to handle the error we use get() function
... 
... '''
'\nif the element is not in the data it gives an error so to handle the error we use get() function\n\n'
>>> 
>>> d[12243]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d[12243]
KeyError: 12243
>>> d.get(1234567)
>>> d.get(1)
12
