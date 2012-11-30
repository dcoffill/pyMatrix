def matrixRowReduce(L): # L is a python List consisting of several lists, where each list is a row in a matrix
	matrixFirstEntry = []
	for i in range(len(L)-1): # first ensure that the leftmost, nonzero column is used
		if L[0][0]==0: # if the top left digit is zero, interchange the 1st and 2nd rows
			L[0], L[i+1] = L[i+1], L[0]
	for row in range( len(L) ):
		matrixFirstEntry.append(L[row][0])
#		print(L[row][0])
	for row in range(len(L)-1): # iterates through rows of the matrix, eliminates row 1
		for col in range(len(L[0])): # iterates through the columns of the matrix
#				print(L[i][j], '*', L[i+1][0], '-', L[i+1][j])
			print(- L[row][col], '*', matrixFirstEntry[row+1], '+', L[row+1][col])
			L[row+1][col] = - L[0][col] * matrixFirstEntry[row+1] + L[row+1][col]
		for col in range(1, len(L[0]) -1 ):
			print(- L[row+1][col] * matrixFirstEntry[row+1] + L[row+1][col])
			L[row+1][col+1] = - L[row+1][col+1] * matrixFirstEntry[row+1] + L[row+1][col+1]

			continue

def RowReduce(L): # L is a list of lists, where each sublist is a matrix row
	for i in L:
		for j in L[i]:
			pass
M = [[1, 2, 3], [4, 5, 6]]
			
L=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#matrixRowReduce(L)

#		if L[row+1][0] == 0: # if the next row is zero, do not perform an operation
#			continue
#		else:

#alright, the biggest problem so far is that the matrix is being reduced and the original list is being edited.  YOu really ought to keep seperate lists, and change new list

## (C) 2012 COFFILL INDUSTRIES, ALL RIGHTS RESERVED

class Matrix:
	'This class implements matrices, and allows for some basic matrix operations'
	def __init__(self, matrixL=[[]]):
		for i in range(len(matrixL)):
			if len(matrixL[0]) != len(matrixL[i]):
				raise ValueError('Matrix row size mismatch')
#				print('ERROR: MATRIX ROW SIZE MISMATCH')
				# return
			for j in range(len(matrixL[i])): # cycles through sublists (aka individual)
				if type(matrixL[i][j]) != int and type(matrixL[i][j]) != float:
					# print('ERROR: MATRIX MAY ONLY CONTAIN INTEGERS AND FLOATS')
					# return
					raise ValueError('Matrix may only contain integers and floats')
		self.matrixL = matrixL # matrixL is a list of lists, where each sublist is the same length
		self.matrix = matrixL

	def __repr__(self):
		return 'Matrix' + str((self.matrix))

	def __str__(self):
		returnString = '' # initializes
		for i in range( len(self.matrixL)):
			returnString+=str(self.matrixL[i])
			if i != len(self.matrixL)-1:
				returnString+='\n'  ## Consider replacing all of this with some sort of .format() statement for jusified rows

		return returnString
	def __len__(self):
		return len(self.matrixL)

	def __getitem__(self, idx):
		return self.matrixL[idx]

	def __add__(self, matrix2):
		# matrix1 = list(tuple(self)) #probably a better way to do this, but keeps lists from being linked to each other
		matrix1 = self
		m, n = self.size()
#		matrix3 = Matrix([([0]*len(matrix1[0]))])
		matrix3 = Matrix.newMatrix(m, n)

		if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]): # ensures matrices have same no. of rows, columns
			pass
		else:
			# print('ERROR: ADDITION/SUBTRACTION REQUIRES MATRICES TO BE THE SAME SIZE')
			# return
			raise ValueError('Addition requires matrices to be the same size')

		for i in range(len(matrix1)): # loops through rows
			for j in range(len(matrix1[i])): # loop through row entries
				matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
		return Matrix(list(matrix3))

	def __sub__(self, matrix2):
		# matrix1 = list(tuple(self)) #probably a better way to do this, but keeps lists from being linked to each other
		matrix1 = self
		m, n = self.size()
#		matrix3 = Matrix([([0]*len(matrix1[0]))])
		matrix3 = Matrix.newMatrix(m, n)

		if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]): # ensures matrices have same no. of rows, columns
			pass
		else:
			# print('ERROR: ADDITION/SUBTRACTION REQUIRES MATRICES TO BE THE SAME SIZE')
			# return
			raise ValueError('Subtraction requires matrices to be the same size')

		for i in range(len(matrix1)): # loops through rows
			for j in range(len(matrix1[i])): # loop through row entries
				matrix3[i][j] = matrix1[i][j] - matrix2[i][j]
		return Matrix(list(matrix3))

	def newMatrix(m, n): # creates an m * n matrix of zeros
		newMatrixL =  list()
		for i in range(m): # creates m * n matrix, m rows
			newMatrixL.append(n * [0]) # each row has n columns
		return Matrix(newMatrixL)

	def size(self):
		m = len(self.matrixL)
		n = len(self.matrixL[0])
		return (m, n)

	def getList(self): # returns the matrix as a list of lists (individual rows)
		return self.matrixL

	def transpose(self): # transposes a matrix
		matrixT = []
		m, n = self.size() # gets size of matrix as m * n
		for i in range(n): # creates n * m matrix, n rows
			matrixT.append(m * ['x']) # each row has m columns
		for i in range( len( self.matrixL)):
			for j in range( len(self.matrixL[i])):
				matrixT[j][i] = self.matrixL[i][j]
		return Matrix(matrixT)

	def __mul__(self, matrix2):
		matrix1 = self

		matrix1Size = matrix1.size() # tuple of matrix size as m, n
		matrix2Size = matrix2.size() # tuple of matrix size as m, n

		matrix3 = Matrix.newMatrix(matrix1Size[0], matrix2Size[0]) # creates a matrix the size of the end result, aka with row # of 1st, col. # of 2nd.  should be matrix2Size[1]

		## validation code, ensures the matrices will multiply correctly
		if matrix1Size[1] != matrix2Size[0]: # matrix 1's n must equal matrix 2's m value
			raise ValueError('Ensure your matrices are of the correct size')
		for i in range( len(matrix1)): # cycles through rows of 1st matrix
			for j in range( len(matrix1[0])): # cycles through items of matrix1 rows
				for k in range(len(matrix2[j])): # fails because it only performs 1 row operation?
					print(str(matrix1[i][j]), str(matrix2[j][k]))
					matrix3[i][j] = matrix1[i][j] * matrix2[j][k] # this line isn't quite right, methinks
		return matrix3



m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
m2 = Matrix([[1, 4, 6, 7], [4, 6, 2, 6]])

m3 = Matrix([[1, 2]])
m4 = Matrix([[3], [4]])

m5 = Matrix([[1, 2], [3, 4]])
m6 = Matrix([[5], [6]])
## TODO:
## If you're a masochist, get back to the row reducer
## Oh god, use a triple for loop to get multiplication
## Github repo?
