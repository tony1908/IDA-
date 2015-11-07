from puzzle import *
from nodo import *

# stack = []
mymatrix=[[5,1,3,4],[9,2,6,8],[10,14,7,0],[13,11,15,12]]
# stack2 = [mymatrix]
# lista = []
# final = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
# limit = HeuristicaMan(mymatrix)
resul = None
heur = 0;
encontrado = False
a = 0
limit = HeuristicaMan(mymatrix)
# print HeuristicaMan(mymatrix)
# node = Nodo(mymatrix)
# stack.append(node)

while resul == None :
	stack = []
	mymatrix=[[5,1,3,4],[9,2,6,8],[10,14,7,0],[13,11,15,12]]
	stack2 = [mymatrix]
	lista = []
	final = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
	node = Nodo(mymatrix)
	stack.append(node)
	while (encontrado != True) and (len(stack) > 0) :
		temp = stack.pop()
		nivel = temp.nivel
		pad = temp.padre
		i,j = posicion(temp.valor)
		print temp.valor[:]
		iz = moverIzquierda(temp.valor[:],i,j)
		de = moverDerecha(temp.valor[:],i,j)
		ar = moverArriba(temp.valor[:],i,j)
		ab = moverAbajo(temp.valor[:],i,j)
		izq = Nodo(iz,temp,nivel+1)
		der = Nodo(de,temp,nivel+1)
		arr = Nodo(ar,temp,nivel+1)
		aba = Nodo(ab,temp,nivel+1)
		if temp.valor[:] == final:
			print "Respuesta encontrada"
			resul = temp
			# print temp.padre.valor
			encontrado = True
			print resul.nivel
		else:
			# print HeuristicaMan(mymatrix)
			# print (izq.nivel+HeuristicaMan(izq.valor))
		# elif temp.nivel+1 <= limit:
			if izq.valor != None and stack2.count(izq.valor) == 0 and (izq.nivel+HeuristicaMan(izq.valor))<=limit:
				stack.append(izq)
				stack2.append(izq.valor)
				# print 'izq'
				# print izq.nivel+HeuristicaMan(izq.valor)
			if der.valor != None and stack2.count(der.valor) == 0 and (der.nivel+HeuristicaMan(der.valor))<=limit:
				stack.append(der)
				stack2.append(der.valor)
				# print 'der'
				# print izq.nivel+HeuristicaMan(der.valor)
			if arr.valor != None and stack2.count(arr.valor) == 0 and (arr.nivel+HeuristicaMan(arr.valor))<=limit:
				stack.append(arr)
				stack2.append(arr.valor)
				# print 'arr'
				# print izq.nivel+HeuristicaMan(arr.valor)
			if aba.valor != None and stack2.count(aba.valor) == 0 and (aba.nivel+HeuristicaMan(aba.valor))<=limit:
				stack.append(aba)
				stack2.append(aba.valor)
				# print 'aba'
				# print izq.nivel+HeuristicaMan(aba.valor)
	if resul == None:
		print 'ampliacion'
		limit = limit + 1
		pass

	pass


if encontrado == True:
	print "Camino:"
	print resul.valor
	print HeuristicaMan(resul.valor)
	while(resul.padre != None):
		print resul.padre.valor
		resul = resul.padre
		pass
