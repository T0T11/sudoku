#!/usr/bin/env python3

def checkCuadratica(matrix):
    assert isinstance(matrix, list)
    for fila in matrix:
        if len(fila) != len(matrix):
            return False
    return True

def checkNum(matrix):
    assert isinstance(matrix, list)

#presuponiedo que la matriz es cuadratica
    digitoMaximo = len(matrix)
    for fila in matrix:
        for num in fila:
            if num > 0 and num < digitoMaximo and isinstance(num, int):
                return True
    return False

if __name__ == "__main__":
    matrix =  [[1,0,1],
           [0,1,0],
           [0,1,0]]

    assert checkCuadratica(matrix) is True

    matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]

    assert checkCuadratica(matrix1) is True

    matrix2 = [[1,0,0],
           [0,1,0],
          [0,0,0]]

    assert checkCuadratica(matrix2) is True

  
    matrix5 = [[1,0,0,0,0,0,0,0,0]]
    assert checkCuadratica(matrix5) is False  
    print(checkCuadratica(matrix5))