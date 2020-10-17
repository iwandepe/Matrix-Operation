from autoOBE import *
from manualOBE import *

np.set_printoptions(suppress=True)

print("PROGRAM MENCARI INVERS MATRIX DENGAN OBE\n")

print("Matrix 3x3\n")

# Deklarasi isi matrix dengan hardcode
matrix = np.mat([[29.,25.,-16.],[25.,75.,-15.],[-16.,-15.,73.]])
I = np.eye(3)
size = 3

# Gabungkan matrix dengan matrix identitas
matrix = np.hstack([matrix,I])  

# Cetak soal
print(matrix, end="\n\n")

print("PILIHAN:")
print("1. Manual")
print("2. Auto", end='\n\n')
print("Masukkan pilihan: ", end='')

option = int(input().strip())

if option == 1:
    manualInvers(matrix)
else:
    autoInvers(matrix, size)
