Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = 10
>>> type(a)
<class 'int'>
>>> 
>>> b = 27.65
>>> type(b)
<class 'float'>
>>> 
>>> c = 2 + 3j
>>> type(c)
<class 'complex'>
>>> 
>>> d = 'string with single quotes'
>>> type(d)
<class 'str'>
>>> 
>>> d = "string with double quotes"
>>> type(d)
<class 'str'>
>>> 
>>> e = [1,2,3,4,5,6]
>>> type(e)
<class 'list'>
>>> 
>>> f = (1,1,1,1,34,5)
>>> type(f)
<class 'tuple'>
>>> f
(1, 1, 1, 1, 34, 5)
>>> 
>>> g = {1,1,1,4,5,6,67,5,4,3}
>>> type(g)
<class 'set'>
>>> g
{1, 3, 4, 5, 6, 67}
>>> 
>>> h = {'name' : 'varma', 'age' : }
SyntaxError: expression expected after dictionary key and ':'
h = {'name' : 'varma', 'age' : }
>>> h = {'name' : 'varma', 'age' : '10'}
>>> h
{'name': 'varma', 'age': '10'}
>>> type(h)
<class 'dict'>
>>> 
>>> status = True
>>> type(status)
<class 'bool'>
