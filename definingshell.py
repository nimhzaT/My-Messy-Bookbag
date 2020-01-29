Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	x + y

	
>>> add(5,10)
>>> def add(x,y):
	return x+y

>>> add(5,10)
15
>>> answer = add(100,20)
>>> answer
120
>>> answer + answer
240
>>> answer = answer + answer
>>> answer
240
>>> answer = answer + answer - 100
>>> answer
380
>>> answer = answer + answer - answer
>>> answer
380
>>> def add(x,y):
	print(x+y)

	
>>> add(5,2)
7
>>> answer = add(5,2)
7
>>> answer
>>> type(answer)
<class 'NoneType'>
>>> a = print("hello")
hello
>>> #return is not the same as print
>>> type(a)
<class 'NoneType'>
>>> word = "pen"
>>> word[;;-1]
SyntaxError: invalid syntax
>>> word::-1]
SyntaxError: invalid syntax
>>> word [::-1]
'nep'
>>> def rev(text):
	return text[::-1]
rev("pen")
SyntaxError: invalid syntax
>>> rev([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    rev([1,2,3,4])
NameError: name 'rev' is not defined
>>> def rev(text):
		return textp::-1]
	
SyntaxError: invalid syntax
>>> def rev(text):
	return text[::-1]

>>> rev("pen")
'nep'
>>> 
