#!/usr/bin/env python3

from .checkColumna import checkColumna
from .checkFila import checkFila
from .checkCuadratica import checkCuadratica
from .checkNum import checkNum
from .checkNumerosRango import checkNumerosRango
from casosTest.casosTestSudoku import *

def checkSudoku(sudoku):

    return (checkCuadratica(sudoku)
            and checkNum(sudoku)
            and checkNumerosRango(sudoku)
            and checkFila(sudoku)
            and checkColumna(sudoku))


if __name__ == "__main__":
    
   #-----------------------------------Sudoku---------------------------------------------
   
    

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