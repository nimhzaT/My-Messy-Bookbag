Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> not True
False
>>> not False
True
>>> not 2 < 3
False
>>> not 3 > 1
False
>>> not 4 == 3
True
>>> x = 10
>>> y = 20
>>> if not y < x:
	print("it worked")

	
it worked
>>> C = 10
>>> D = 5
>>> if C > 10 and D > 1:
	print("it worked")

	
>>> False and True
False
>>> if C>= 10 and D > 1:
	print("it worked")

	
it worked
>>> if C>= 10 and D > 1:
	print("it worked")

	
it worked
>>> if C > 10 and D > 1:
	print("it worked")

	
>>> if not (C > 10 and D > 1):
	print("it worked")

	
it worked
>>> C = 5
>>> D = -1
>>> if C > 1 or D > 1:
	print(""it worked)
	
SyntaxError: invalid syntax
>>> 
>>> if C > 1 or D > 1:
	print("it worked")

	
it worked
>>> True or False
True
>>> D = 5
>>> if C > 1 or D > 1:
	print("it worked")

	
it worked
>>> if C > 100 or D > 100:
	print("it worked")

	
>>> if not (C > 100 or D > 100):

	print("it worked")

	
it worked
>>> 
>>> 
>>> C = 6
>>> D = 2
>>> if (C>5 and D > 5) or (C > 1 and D> 1):
	print("it worked")

	
it worked
>>> False or True
True
>>> 
