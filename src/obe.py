import numpy as np

# Operasi tukar baris
def swapLines(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row1, row2]]

# Operasi Baris OBE
def rowOperation(matrix, dest, src, nTimes):
    matrix[dest] = matrix[dest]-nTimes*matrix[src]

# Operasi mengali semua elemen pada baris dengan N    
def timesN(matrix, row, nTimes):
    matrix[row] = nTimes*matrix[row]
