# Az eljárást készítette:
def szovegFordit(szoveg):
	ujSzoveg=""
	for x in range(len(szoveg)-1,-1,-1):
		ujSzoveg=ujSzoveg+szoveg[x] 
	return ujSzoveg
	
# Az eljárást készítette:	
def szovegCsere(szoveg):
	maganHangzo="aioőúűáéüóöí"
	for x in range(0,len(maganHangzo)):
		szoveg=szoveg.replace(maganHangzo[x],'e')
	return szoveg
	
# Az eljárást készítette: Jáger Attila	
def szovegParos(szoveg):
	# Ez egy tök jó eljárás!!!
	# Én írtam, és ma álmos is vagyok!	
	ujSzoveg=""
	for x in range(0,len(szoveg),2):
		ujSzoveg=ujSzoveg+szoveg[x] 
	return ujSzoveg
	
# Az eljárást készítette:	
def szovegParatlan(szoveg):
	# Ide írd meg az eljárást!
	ujSzoveg=""
	for x in range(1,len(szoveg),2):
		ujSzoveg=ujSzoveg+szoveg[x] 
	return ujSzoveg
	
# Itt kezdődik a főprogram
kor=1
while (kor <= 3):

	szoveg=input("Írj be egy szöveget:")
	#még nincs kész a szovegFordit metódus!
	#print(szovegFordit(szoveg))
	
	print("A szöveg csere:", szovegCsere(szoveg))
	print("A szöveg páros karakterei:", szovegParos(szoveg))
	
	print("A szöveg páratlan karakterei:", szovegParatlan(szoveg))
	print("A szöveg forditva:", szovegFordit(szoveg))
	#Cica keresése
	if("cica" in szoveg):
		print(szoveg)
	kor +=1
	print()

