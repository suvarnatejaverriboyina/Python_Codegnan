Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1,num2,num3=10,20,30
print(num1,num2,num3)
10 20 30
n1,n2,n3=10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    n1,n2,n3=10
TypeError: cannot unpack non-iterable int object
n1,n2,n3=10,10,10
print(n1,n2,n3)
10 10 10
n1=n2=n3=10
print(n1,n2,n3)
10 10 10
print(id(n1),id(n2),id(n3))
140727601019608 140727601019608 140727601019608
print(id(num1),id(num2),id(num3))
140727601019608 140727601019928 140727601020248
a.b=257,257
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.b=257,257
NameError: name 'a' is not defined
a,b=257,257
print(id(a),id(b))
1858562274288 1858562274288
>>> print(a is b)
True
>>> a=345
>>> print(id(a))
1858562274224
>>> print(a==b)
False
>>> a,b=1,2
>>> print(id(a),id(b))
140727601019320 140727601019352
>>> a,b=b,a
>>> print(id(a),id(b))
140727601019352 140727601019320
>>> print(a,b)
2 1
>>> a=10
>>> """This is multi line string Comment"""
'This is multi line string Comment'
>>> print(_doc_)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(_doc_)
NameError: name '_doc_' is not defined. Did you mean: '__doc__'?
>>> NameError: name '_doc_' is not defined. Did you mean: '__doc__'?
SyntaxError: invalid syntax
>>> print(__doc__)
None
>>> """This is multi line string Comment"""
'This is multi line string Comment'
>>> print(__doc__)
None
>>> """This is multi line string Comment"""print(__doc__)
SyntaxError: invalid syntax
>>> print(__doc__)
None
>>> print(bool(-9))
True
>>> print(True+False+True+True)
3
>>> print(True*False)
0
>>> print(False*False)
0
>>> print(False+False)
0
