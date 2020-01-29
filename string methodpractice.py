Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> "helo".count("e")
1
>>> text = "happy irthday"
>>> text.count("a")
2
>>> text.count("day")
1
>>> x = "Happy Birthday"
>>> x.lower()
'happy birthday'
>>> x.upper()
'HAPPY BIRTHDAY'
>>> x
'Happy Birthday'
>>> x = x.upper()
>>> x
'HAPPY BIRTHDAY'
>>> x.lower()
'happy birthday'
>>> x
'HAPPY BIRTHDAY'
>>> x = x.lower()
>>> x
'happy birthday'
>>> x.capitalize()
'Happy birthday'
>>> x
'happy birthday'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x
'happy birthday'
>>> x.title()
'Happy Birthday'
>>> x
'happy birthday'
>>> x = x.title()
>>> x
'Happy Birthday'
>>> x
'Happy Birthday'
>>> x.islower()
False
>>> x.isupper9)
SyntaxError: invalid syntax
>>> x.isupper()
False
>>> x.istitle()
True
>>> x.isalpha()
False
>>> x
'Happy Birthday'
>>> "abcd".isalpha()
True
>>> x.isdigit()
False
>>> x
'Happy Birthday'
>>> "123".isdigit()
True
>>> y = "happybirthday123"
>>> y.isalnum()
True
>>> y = "happybirthday!123"
>>> y.isalnum()
False
>>> 
