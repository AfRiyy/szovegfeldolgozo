"""
PUSKA

A szöveg hossza: len(szoveg)
A szöveg utolsó karater: szoveg[len(szoveg)-1]
Csere a szövegben : szoveg.replace("H", "J") // a nagy "H"-kat nagy "J"-re cserélem
A szöveg tartalmazza az alma karaktereket?: logikaiValtozo = "alma" in szoveg // not in - nem tartalmazza

Ciklus:
ujSzoveg=""
for x in range(0,len(szoveg)-1,2):
	ujSzoveg=ujSzoveg+szoveg[x] 

Eljáras:
def szovegFordit(szöveg):
	...
	return vissza
"""
# Az eljárást készítette:
def szovegFordit(szoveg):
	Újszoveg=""
	for x in range(0,len(szoveg)-1,-1,-1):
	ujSzoveg=ujSzoveg+szoveg[x] 
	return "ujSzoveg"
	
# Az eljárást készítette:	
def szovegCsere(szoveg):
	# Ide írd meg az eljárást!
	return ""
	
# Az eljárást készítette: Jáger Attila	
def szovegParos(szoveg):
<<<<<<< HEAD
	if ((len(szoveg)%2)	= 0):
		return szoveg
	
=======
	ujSzoveg=""
	for x in range(0,len(szoveg),2):
		ujSzoveg=ujSzoveg+szoveg[x] 
	return ujSzoveg
>>>>>>> 255c429ca222c077b71f68e5970993c30b1fd156
	
# Az eljárást készítette:	
def szovegParatlan(szoveg):
	# Ide írd meg az eljárást!
	return ""
	
# Itt kezdődik a főprogram
szoveg=input("Írj be egy szöveget:")
#még nincs kész a szovegFordit metódus!
#print(szovegFordit(szoveg))

szovegCsere("A szöveg csere:",szoveg)
szovegParos("Páros karakterek"szoveg)
szovegParatlan(szoveg)
#Cica keresése
if(szoveg.find("cica") != -1):
	print(szoveg)


