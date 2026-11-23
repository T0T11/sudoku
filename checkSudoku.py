#!/usr/bin/env python3

def checkColumnas(sudoku):

    assert isinstance(sudoku, list)

    numeroFilas = len(sudoku)

    for columna in range(numeroFilas):
        numerosColumna = []

        for fila in sudoku:
            numero = fila[columna]

            if numero in numerosColumna:
                return False

            numerosColumna.append(numero)

    return True


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

    return checkCuadratica(sudoku) and checkNumerosRango(sudoku) and checkFila(sudoku) and checkColumnas(sudoku)


if __name__ == "__main__":
    
    #-----------------------------------Columnas------------------------------------
    assert checkColumnas([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) is True
    assert checkColumnas([[1, 2, 3], [2, 3, 1], [2, 1, 3]]) is False

    #-----------------------------------Cuadratica------------------------------------
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

# Caso válido (matriz cuadrada NxN con enteros del 1 al N sin repetir en filas ni columnas)
assert checkSudoku(correct) is True

# Casos inválidos por números repetidos en filas o columnas
assert checkSudoku(incorrect) is False    # Repite el 3 en la última columna y el 4 en la última fila
assert checkSudoku(incorrect1) is False   # Repite valores en las columnas
assert checkSudoku(incorrect2) is False   # Repite el 2 en la segunda fila [2, 3, 1, 2]

# Casos inválidos por tipo de dato o rango fuera de 1..N
assert checkSudoku(incorrect3) is False   # Matriz 5x5 que contiene un 6 (fuera del rango 1..5)
assert checkSudoku(incorrect4) is False   # Contiene strings ('a', 'b', 'c') en lugar de enteros
assert checkSudoku(incorrect5) is False   # Contiene flotantes (1.5) en lugar de enteros

# Casos inválidos por dimensiones o estructura irregular
assert checkSudoku(irregular) is False    # No es cuadrada (2 filas x 3 columnas)
assert checkSudoku(irregular2) is False   # Filas de distinta longitud (la última tiene solo 2 elementos)
assert checkSudoku(nuevo) is False        # Matriz vacía [[]]