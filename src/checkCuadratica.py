def checkCuadratica(matrix):
    for fila in matrix:
        if len(fila) != len(matrix):
            return False
    return True
