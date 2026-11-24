#!/usr/bin/env python3

def checkNum(matrix):
    assert isinstance(matrix, list)

#presuponiedo que la matriz es cuadratica
    digitoMaximo = len(matrix)
    for fila in matrix:
        for num in fila:
            if num > 0 and num < digitoMaximo and isinstance(num, int):
                return True
    return False

def checkFila(matriz):
    assert isinstance(matriz, list)                                  # Precondicion: Check if the given fila (queue) is valid.
                                                                  
    for fila in matriz:
        for number in fila:         
                if fila.count(number) > 1:
                    return False
    return True

def checkNumerosRango(sudoku):

    assert isinstance(sudoku, list)

    numeroMaximo = len(sudoku)

    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int):
                return False

            if numero < 1 or numero > numeroMaximo:
                return False

    return True

def checkSudoku(sudoku):

    return checkCuadratica(sudoku) and checkNumerosRango(sudoku) and checkFila(sudoku) and checkColumnas(sudoku) and checkNum(sudoku)


if __name__ == "__main__":
    
    #-----------------------------------Fila---------------------------------------------  
    assert checkFila([[1, 0, 1],
                    [0, 1, 0]]) is False
    
    assert checkFila([[1, 0,],
                    [2, 3]]) is True
    #-----------------------------------Numeros en Rango---------------------------------------------
    
    assert checkNumerosRango([[1, 2, 3],
                                   [2, 3, 1],
                                   [3, 1, 2]]) is True
   
    assert checkNumerosRango([[1, 2, 4],
                                   [2, 3, 1],
                                   [3, 1, 2]]) is False
   
    assert checkNumerosRango([[1, 1.5],
                                   [2, 1]]) is False
   
    assert checkNumerosRango([[1, 0],
                                   [2, 1]]) is False
   #-----------------------------------Sudoku---------------------------------------------
   
    correct = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

    incorrect = [[1, 2, 3, 4],
                [2, 3, 1, 3],
                [3, 1, 2, 3],
                [4, 4, 4, 2]]

    incorrect1 = [[1, 2, 3],
                [2, 3, 1],
                [2, 3, 1]]

    incorrect2 = [[1, 2, 3, 4],
                [2, 3, 1, 2],
                [4, 1, 2, 3],
                [2, 3, 1, 4]]

    incorrect3 = [[1, 2, 3, 4, 5],
                [2, 3, 1, 5, 6],
                [4, 5, 2, 1, 3],
                [3, 4, 5, 2, 1],
                [5, 6, 4, 3, 2]]

    incorrect4 = [['a', 'b', 'c'],
                ['b', 'c', 'a'],
                ['c', 'a', 'b']]

    incorrect5 = [[1, 1.5],
                [1.5, 1]]

    irregular = [[1, 2, 3],
                [2, 3, 1]]

    irregular2 = [[1, 2, 3],
                [2, 3, 1],
                [3, 1]]
    nuevo = [[]]

    assert checkSudoku(correct) is True

    assert checkSudoku(incorrect) is False    
    assert checkSudoku(incorrect1) is False   
    assert checkSudoku(incorrect2) is False   

    assert checkSudoku(incorrect3) is False   
    assert checkSudoku(incorrect4) is False   
    assert checkSudoku(incorrect5) is False   

    assert checkSudoku(irregular) is False    
    assert checkSudoku(irregular2) is False   
    assert checkSudoku(nuevo) is False        