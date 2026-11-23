# Sudoku ✅

Proyecto desarrollado por **T0T11** y **ArionVP** para comprobar la validez de un tablero de Sudoku mediante distintas funciones de verificación implementadas en Python.

## 📋 Descripción

Este proyecto permite validar un tablero de Sudoku verificando que cumpla las reglas fundamentales del juego:

- Los números pertenecen al rango permitido.
- No existen valores repetidos en una misma fila.
- No existen valores repetidos en una misma columna.
- Las subcuadrículas contienen valores válidos.
- La validación completa se realiza mediante la combinación de todas las comprobaciones anteriores.

Cada regla ha sido implementada en un módulo independiente para facilitar el mantenimiento, la reutilización del código y la creación de pruebas unitarias.

## 📂 Estructura del Proyecto

```text
sudoku/
├── .gitignore
├── checkColumnas.py
├── checkCuadratica.py
├── checkFila.py
├── checkNumerosRango.py
├── checkSudoku.py



## 🛠️ Módulos

| Archivo | Funcionalidad |
|----------|--------------|
| `checkFila.py` | Comprueba que una fila sea válida. |
| `checkColumnas.py` | Comprueba que las columnas sean válidas. |
| `checkCuadratica.py` | Verifica las subcuadrículas del tablero. |
| `checkNumerosRango.py` | Comprueba que los números estén dentro del rango permitido. |
| `checkSudoku.py` | Realiza la validación completa del Sudoku utilizando el resto de funciones. |

## 🚀 Instalación

### Clonar el repositorio

```bash
git clone https://github.com/T0T11/sudoku.git
cd sudoku
```

### Crear un entorno virtual

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

