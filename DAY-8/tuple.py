Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = ()
t (1,2,3,4,5,6,7,8)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t (1,2,3,4,5,6,7,8)
TypeError: 'tuple' object is not callable

t = (1,2,3,5,3,2,24)
len(t)
7
min(t)
1
max(t)
24
sum(t)
40
t.count(0)
0
t.count(2)
2
>>> t.index(2)
1
>>> t.index(1)
0
>>> #packing and unpacking
>>> a = (1,2,4,5)
>>> a
(1, 2, 4, 5)
>>> x,y,c,v = a
>>> x
1
>>> y
2
>>> c
4
>>> v
5
>>> t = (1,2,[3,4,5,6],7,8,9)
>>> t[2]
[3, 4, 5, 6]
>>> t[2].append(99)
>>> t
(1, 2, [3, 4, 5, 6, 99], 7, 8, 9)
>>> t[1] = 4
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t[1] = 4
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [3, 4, 5, 6, 99], 7, 8, 9)
>>> #only imutable items are alowed in the set such as list set dictnoary Traceback (most recent call last):
>>> s = set()
>>> s = {1,2,3,5,3,22,,34,5678,9,98,7654,32,34,5,9,87654,32,345,67,09,87654,321,23,456890,09,8765,4321,3,45,09,87654}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> s = {23,4,876,543,2,34,567,89,87,6543,2,5,69,09,8765,43}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> s= {2,3456,54,32,34,567,654,3234,569,8765432,345679,87651}
>>> s = {1,2,3,4,5,6}
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.add(9)
>>> s
{1, 2, 3, 4, 5, 6, 9}
>>> '''
... cannot add list values because these are the mutable values
... 
... '''
'\ncannot add list values because these are the mutable values\n\n'
