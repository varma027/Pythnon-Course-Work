Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
varma
naem = input("enter your name: ")
enter your name: varma
name
'varma'
age = input("enter your age: ")
enter your age: 21
age
'21'
age = int(input("enter your age: "))
enter your age: 21
age
21
#for float value
gpa = float(input("enter the cgpa: "))
enter the cgpa: 7.1
gpa
7.1
#for string
'generally the input() takes string values'
'generally the input() takes string values'
#for list
products = input().split()
laptop mouse keyboard mobile 
products
['laptop', 'mouse', 'keyboard', 'mobile']
#for tuple
type(age)
<class 'int'>
tup = tuple(input("enter the values").split())
enter the valuesa b c d e f r t h h g 
tup
('a', 'b', 'c', 'd', 'e', 'f', 'r', 't', 'h', 'h', 'g')
#for set
st = set(input("enter the values: ").split())
enter the values: sai subbu varma suri aditya
st
{'subbu', 'aditya', 'sai', 'suri', 'varma'}
type(st)
<class 'set'>
#how to take int input in a list
marks = list(map(int, input("enter the marks: ").split()))
enter the marks: 1 234567 89 8 76 54321  456 789  8765 4321 
marks
[1, 234567, 89, 8, 76, 54321, 456, 789, 8765, 4321]
#how to take int input in a tuple
prices = tuple(map(int,input("enter the prices: ").split()))
enter the prices: 3 6 5 4 3 56  7 9 09 87 65 4 3 
prices
(3, 6, 5, 4, 3, 56, 7, 9, 9, 87, 65, 4, 3)
#how to take int input in set
rating = set(map(int, input("enter the ratings: ").split))
enter the ratings: 4 323 4  455 67 65 43 22  67 8 87 654 32 1  67 76 4 4 4 44 4 
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    rating = set(map(int, input("enter the ratings: ").split))
TypeError: 'builtin_function_or_method' object is not iterable
rating = set(map(int , input("enter the ratings: ").split())
             rating
             
SyntaxError: '(' was never closed
#how to take float input in set
             
prices = set(map(int,input("enter the prices").split()))
             
enter the prices1 2 3 4 5 6 6 5 4 3 12 2 1 1
prices = set(map(float,input("enter the prices").split()))
             
enter the prices1 2 3 45 4 3 1 2 3 4 2 1
prices
             
{1.0, 2.0, 3.0, 4.0, 45.0}
'''
how to take double inputs
'''
             
'\nhow to take double inputs\n'

a , b = [1,2]
             
a
             
1
b
             
2
uname,passw = input("enter unaem and pass").split()
             
enter unaem and passsai
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    uname,passw = input("enter unaem and pass").split()
ValueError: not enough values to unpack (expected 2, got 1)
uname,passw = input("enter unaem and pass").split()
             
enter unaem and passsai varma@!
uname
             
'sai'
passw
             
'varma@!'
a,b,c,d = list(map(float, input("enter the 4 sides: ").split()))
             
enter the 4 sides: 2
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a,b,c,d = list(map(float, input("enter the 4 sides: ").split()))
ValueError: not enough values to unpack (expected 4, got 1)
2
             
2
a,b,c,d = list(map(float, input("enter the 4 sides: ").split()))
             
enter the 4 sides: 2 2 2 2
a
             
2.0
b
             
2.0
c
             
2.0
d
             
2.0

price,discount = list(map(flaot,input("enter the price and discount: ").split()))
             
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    price,discount = list(map(flaot,input("enter the price and discount: ").split()))
NameError: name 'flaot' is not defined. Did you mean: 'float'?
price,discount = list(map(float,input("enter the price and discount: ").split()))
             
enter the price and discount: 234567 23.456
price
...              
234567.0
>>> discount
...              
23.456
>>> #eval function takes input based on the iput given
...              
>>> a = eval(input())
...              
234567
>>> a
...              
234567
>>> a = eval(input())
...              
"sais sdfskfjs skdfjf"
>>> a
...              
'sais sdfskfjs skdfjf'
>>> a = eval(input())
...              
{1,2,3,4,5,6,8,9,9}
>>> a
...              
{1, 2, 3, 4, 5, 6, 8, 9}
>>> type(a)
...              
<class 'set'>
>>> #concatination of a string
...              
>>> a = 'codegnan'
...              
>>> b = 'pfs'
...              
>>> a+b
...              
'codegnanpfs'
>>> #repetation of a string
...              
>>> b*10
...              
'pfspfspfspfspfspfspfspfspfspfs'
>>> n = 'varma '*27
...              
>>> n
...              
'varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma varma '
>>> #slicing means extracting group of elements
...              
