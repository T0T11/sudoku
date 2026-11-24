#!/usr/bin/env python3

def checkNum(matrix):
    assert isinstance(matrix, list)

#presuponiedo que la matriz es cuadratica
    digitoMaximo = len(matrix)
    for fila in matrix:
        for num in fila:
            if  isinstance(num, int) and (num > 0 and num < digitoMaximo):
                return True
    return False

if __name__ == "__main__":

    assert checkNum([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) is True
    assert checkNum([['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]) is False 