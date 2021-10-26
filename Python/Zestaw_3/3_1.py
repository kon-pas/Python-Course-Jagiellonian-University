""" Podpunkt 1

x = 2; y = 3;
if (x > y):
	result = x;
else:
	result = y;
	
Komentarz: zbedne sredniki na koncach linii, zbedne nawiasy w instrukcji
warunkowej if
"""
x = 2; y = 3
if x > y:
	result = x
else:
	result = y
   
""" Podpunkt 2

for i in "qwerty": if ord(i) < 100: print (i)

Komentarz: instrukcje powinny byc wypisane w osobnych liniach, odpowiednio 
zagniezdzone uzywajac wciec tabulatorem
"""
for i in "qwerty":
	if ord(i) < 100:
		print (i)
		
""" Podpunkt 3

for i in "axby": print (ord(i) if ord(i) < 100 else i)

Komentarz: Poprawne, niemniej dobra praktyka jest pisanie instrukcji w 
osobnej linii
"""
for i in "axby":
	print (ord(i) if ord(i) < 100 else i)
