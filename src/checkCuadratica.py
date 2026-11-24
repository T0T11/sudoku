#!/usr/bin/env python3

def checkCuadratica(matrix):
    assert isinstance(matrix, list)
    for fila in matrix:
        if len(fila) != len(matrix):
            return False
    return True

if __name__ == "__main__":
    matrix =  [[1,0,1],
               [0,1,0],
               [0,1,0]]
        
        
    matrix1 = [[1,0,0,0],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]]
    
    
    matrix2 = [[1,0,0],
               [0,1,0],
              [0,0,0]]
    
    
      
    matrix5 = [[1,0,0,0,0,0,0,0,0]]
    
    assert checkCuadratica(matrix) is True
    assert checkCuadratica(matrix1) is True
    assert checkCuadratica(matrix2) is True
    assert checkCuadratica(matrix5) is False  