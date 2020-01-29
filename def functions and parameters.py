Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def about(name, age, likes)
SyntaxError: invalid syntax
>>> def about(name, age, likes)
SyntaxError: invalid syntax
>>> def about(name, age, likes):
	sentence = "Meet{}! They are P{ years old and they like P{".formate(name, age, likes)
	return sentence

>>> about("jack", 23,"Python")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    about("jack", 23,"Python")
  File "<pyshell#5>", line 2, in about
    sentence = "Meet{}! They are P{ years old and they like P{".formate(name, age, likes)
AttributeError: 'str' object has no attribute 'formate'
>>> def about(name, age, likes):
	sentence = "Meet{}! They are {} years old and they like {}".formate(name, age, likes)
	return sentence

>>> about
<function about at 0x03835C00>
>>> about("Jack", 23, "Python")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    about("Jack", 23, "Python")
  File "<pyshell#8>", line 2, in about
    sentence = "Meet{}! They are {} years old and they like {}".formate(name, age, likes)
AttributeError: 'str' object has no attribute 'formate'
>>> def about(name, age, likes):
	sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
	return sentence

>>> about("Jack", 23, "Python")
'Meet Jack! They are 23 years old and they like Python'
>>> about(age = 23, name = "Jack", likes = "Python")
'Meet Jack! They are 23 years old and they like Python'
>>> about ("jack", 23)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    about ("jack", 23)
TypeError: about() missing 1 required positional argument: 'likes'
>>> def about(name,age, likes = "Python"):
	sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
	return sentence

>>> about("Jack",23)
'Meet Jack! They are 23 years old and they like Python'
>>> #parameters with default values have to go last
>>> #default values are used and called with "def (variable)( variable = value, etc,) or (var/val, var/val, var = val)
>>> 
