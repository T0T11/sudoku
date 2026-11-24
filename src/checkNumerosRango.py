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

if __name__ == "__main__":
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