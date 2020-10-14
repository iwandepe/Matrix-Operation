from obe import *
from os import system, name
from time import sleep

print("PROGRAM OPERASI MATRIX DENGAN OBE\n")

print("Matrix 3x3\n")
# mengganti isi matrix dengan hardcode
matrix=np.mat([[3,1,2],[0,1,-5.],[1,1,-1]])
while True:
    print(matrix, end="\n\n")
    opsi = input().strip()
    
    if opsi == "out":
        break
    elif opsi == "tb":
        print("Masukkan 2 baris yang akan ditukar")
        print("input: ", end='')
        baris1, baris2 = map(int, input().split())
        tukarBaris(matrix, baris1, baris2)
    elif opsi == "tk":
        print("Masukkan 2 kolom yang akan ditukar")
        print("masukan: ", end='')
        kolom1, kolom2 = map(int, input().split())
        tukarKolom(matrix, kolom1, kolom2)
    elif opsi == "ob":
        print("Masukkan baris tujuan, baris awal, dan N kali")
        print("input: ", end='')
        barisTujuan, barisAwal, nKali = input().split()
        operasiBaris(matrix, int(barisTujuan), int(barisAwal), eval(nKali))
    elif opsi == "kali":
        print("Masukkan baris dan N kali")
        print("input: ", end='')
        baris, nKali = input().split()
        kaliN(matrix, int(baris), eval(nKali))
    else:
        print("Masukan tidak valid, ulangi")
