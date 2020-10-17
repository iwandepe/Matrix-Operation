from obe import *

def findMainOne(matrix, size, index):
    row = index
    col = index
    
    row += 1
    while row<size:
        if matrix[[row],[col]] != 0:
            return row
    return index

def autoInvers(matrix, size):
    # Variable to counting each of step
    step = 0
    
    # LOOP membuat satu utama
    for index in range(size):
        
        # Cek apakah bisa dijadikan satu utama
        if matrix[[index],[index]] == 0:
             row = findMainOne(matrix, size, index)
             swapLines(matrix, index, row)
             step += 1
             print("Step ", step)
             print(matrix, end='\n\n')
        
        # Cek apakah elemen sudah menjadi satu utama
        if matrix[[index],[index]] != 1:
            timesN(matrix, index, 1/matrix[[index],[index]])
            matrix = np.round(matrix, 4)
            step += 1
            print("Step ", step)
            print(matrix, end='\n\n')
        
        # LOOP untuk membuat nol elemen di bawah satu utama
        for row in range(index+1, size):
            
            # Cek apakah elemen belum nol
            if matrix[[row],[index]] != 0:
                rowOperation(matrix, row, index, matrix[[row],[index]])
                matrix = np.round(matrix, 4)
                step += 1
                print("Step ", step)
                print(matrix, end='\n\n')
        
    # LOOP membuat nol elemen di atas satu utama
    for index in range(size-1,-1,-1):
        for row in range(index-1, -1, -1):
            
            # Cek apakah elemen belum nol
            if matrix[[row],[index]] != 0:
                rowOperation(matrix, row, index, matrix[[row],[index]])
                matrix = np.round(matrix, 4)
                step += 1
                print("Step ", step)
                print(matrix, end='\n\n')
    
