def posicion(matrix):#funcion para obtener la posicion
	pos1 = 0
	pos2 = 0
	for mat in matrix:
	    for x in mat:
	        if x == 0:
	        	pos1 = matrix.index(mat)
	        	pos2 = mat.index(x)
	return pos1,pos2


def posicion2(matrix,val,matrix2):#funcion para obtener la posicion
	pos1 = 0
	pos2 = 0
	for mat in matrix:
	    for x in mat:
	        if x == val:
	        	pos1 = matrix.index(mat)
	        	pos2 = mat.index(x)
	for mat2 in matrix2:
	    for y in mat2:
	        if y == val:
	        	pos3 = matrix2.index(mat2)
	        	pos4 = mat2.index(y)
	return abs(abs((pos3-pos1))+abs((pos4-pos2)))

def moverIzquierda(matrix,x,y):#x = i, y =j
	if (y - 1) >= 0:
		matrix_temp = matrix[x][:]
		matrix_temp[y-1], matrix_temp[y] = 0, matrix_temp[y-1]
		matrix[x] = matrix_temp
		return matrix
	else:
		return None

def moverDerecha(matrix, x, y):
    size = len(matrix) - 1
    if (y + 1) <= size:
        matrix_temp = matrix[x][:]
        matrix_temp[y+1], matrix_temp[y] = 0, matrix_temp[y+1]
        matrix[x] = matrix_temp
        return matrix
    else:
        return None

def moverArriba(matrix, x, y):
	if (x - 1)>=0:
		matrix_temp = matrix[x-1][:]
		matrix_temp1 = matrix[x][:]
		matrix_temp[y], matrix_temp1[y] = 0, matrix_temp[y]
		matrix[x-1] = matrix_temp
		matrix[x] = matrix_temp1
		return matrix
	else:
		return None

def moverAbajo(matrix,x,y):
	size = len(matrix) - 1
	if (x + 1) <= size:
		matrix_temp = matrix[x+1][:]
		matrix_temp1 = matrix[x][:]
		matrix_temp[y], matrix_temp1[y] = 0, matrix_temp[y]
		matrix[x+1] = matrix_temp
		matrix[x] = matrix_temp1
		return matrix
	else:
		return None



def HeuristicaMan(matrix):
	plantilla = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
	# plantilla = [[n * i + j for j in xrange(n)] for i in xrange(n)]
	cuenta = 0
	for x in xrange(1,16):
		# print posicion2(matrix,x,plantilla)
		suma = posicion2(matrix,x,plantilla)
		cuenta = cuenta + suma
	return cuenta

print HeuristicaMan([[2,4,3],[7,1,6],[0,5,8]])