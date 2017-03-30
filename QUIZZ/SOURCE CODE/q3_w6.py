
def tabuada1():
	tab = 1
	while tab <= 10:
		i = 1
		while i <= 10:
			print(tab,"x",i,"=",tab*i)
			i = i + 1
		print()
		tab = tab + 1
		
def tabuada2():	
	tab = 0
	while tab < 10:
		tab = tab + 1
		i = 0
		while i < 10:
			i = i + 1
			print(tab,"x",i,"=",tab*i)
		print()
		
def tabuada3():	
	tab = 1
	while tab <= 10:
		i = 1
		while i <= 10:
			print(tab*i, end = "\t")
			i = i + 1
		print()
		tab = tab + 1
		
def tabuada4():
	tab = 1
	while tab <= 10:
		i = 1
		print(tab*i, end = "\t")
		i = i + 1
		print()
		tab = tab + 1
		
def tabuada5():
	tab = 1
	i = 1
	while tab <= 10 and i <= 10:
		print(tab,"x",i,"=",tab*i)
		i = i + 1
		tab = tab + 1
	print()
	
tabuada1()		
tabuada2()
tabuada3()
tabuada4()
tabuada5()


