import numpy as np

def tukarBaris(matrix, baris1, baris2):
    matrix[[baris1, baris2]] = matrix[[baris2, baris1]]
    
def tukarKolom(matrix, kolom1, kolom2):
    matrix[:, [kolom1, kolom2]] = matrix[:, [kolom2, kolom1]]

def operasiBaris(matrix, barisTujuan, barisAwal, nKali):
    matrix[barisTujuan] = matrix[barisTujuan]-nKali*matrix[barisAwal]
    
def kaliN(matrix, baris, nKali):
    matrix[baris] = nKali*matrix[baris]
