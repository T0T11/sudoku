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


if __name__ == "__main__":

    assert checkColumnas([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]]) is True

    assert checkColumnas([[1, 2, 3],
                          [2, 3, 1],
                          [2, 1, 3]]) is False
