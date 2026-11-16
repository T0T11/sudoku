
from src.checkCuadratica import checkCuadratica



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
assert checkCuadratica(matrix5) is True