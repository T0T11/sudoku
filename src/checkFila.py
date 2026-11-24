#!/usr/bin/env python3

def checkFila(matriz):
    assert isinstance(matriz, list)                                  # Precondicion: Check if the given fila (queue) is valid.
                                                                  
    for fila in matriz:
        for number in fila:         
                if fila.count(number) > 1:
                    return False
    return True

if __name__ == "__main__":
    assert checkFila([[1, 0, 1],
                    [0, 1, 0]]) is False
    
    assert checkFila([[1, 0,],
                    [2, 3]]) is True