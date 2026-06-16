Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = 'python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('  ')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ord('  ')
TypeError: ord() expected a character, but string of length 2 found
ord(' ')
32
ord("a")
97
ord('A')
65
chr('32')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    chr('32')
TypeError: 'str' object cannot be interpreted as an integer
chr(48)\
         chr(48)
SyntaxError: invalid syntax
chr(48)
'0'
chr(37)
'%'
chr(27)
'\x1b'


s = 'pyhton programmning'
s.upper()
'PYHTON PROGRAMMNING'
s.lower()
'pyhton programmning'
s.captalize()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
s.capitalize()
'Pyhton programmning'
s.tittle()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
s.title()
'Pyhton Programmning'
s.swapcase()
'PYHTON PROGRAMMNING'
>>> 
>>> 
>>> s.conter(28,'*')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.conter(28,'*')
AttributeError: 'str' object has no attribute 'conter'. Did you mean: 'center'?
>>> s.center(28,'*')
'****pyhton programmning*****'
>>> s.ljust(28,'*')
'pyhton programmning*********'
>>> s.rjust(28,'*')
'*********pyhton programmning'
>>> '124',zfill(7)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    '124',zfill(7)
NameError: name 'zfill' is not defined
>>> '123'.zfill(7)
'0000123'
>>> '123'.zfill(4)
'0123'
>>> 

>>> #search and find methods
>>> len(s)
19
>>> 
>>> s.find('g')
10
>>> s.find('o')
4
>>> s.find('z')
-1
>>> s.rfing('o')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.rfing('o')
AttributeError: 'str' object has no attribute 'rfing'. Did you mean: 'rfind'?
>>> s.rfind('o')
9
>>> s.index('o')
4
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s.index('z')
ValueError: substring not found
