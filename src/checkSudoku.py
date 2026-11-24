#!/usr/bin/env python3

def checkSudoku(sudoku):

    return checkCuadratica(sudoku) and checkNumerosRango(sudoku) and checkFila(sudoku) and checkColumnas(sudoku) and checkNum(sudoku)


if __name__ == "__main__":

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