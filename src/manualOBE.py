from obe import *

def manualInvers(matrix):
    print("Option:")
    print("tb\t: Tukar Baris\nob\t: Operasi Baris\nkali\t: Kali dengan N\n")
    
    while True:
        option = input().strip()
        
        if option == "out":
            break
        elif option == "tb":
            print("Masukkan 2 baris yang akan ditukar")
            print("input: ", end='')
            row1, row2 = map(int, input().split())
            swapLines(matrix, row1-1, row2-1)
            
        elif option == "ob":
            print("Masukkan baris tujuan, baris awal, dan N kali")
            print("input: ", end='')
            dest, src, nTimes = input().split()
            rowOperation(matrix, int(dest)-1, int(src)-1, eval(nTimes))
            
        elif option == "kali":
            print("Masukkan baris dan N kali")
            print("input: ", end='')
            row, nTimes = input().split()
            timesN(matrix, int(row)-1, eval(nTimes))
            
        else:
            print("Masukan tidak valid, ulangi")
            
        matrix = np.round(matrix, 4)
        print(matrix, end="\n\n")
