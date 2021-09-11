from pickle import dump, load
from random import choice

TAM_SUDOKU = 9

class Celda():
    def __init__(self, n):
        self.n = int(n)
        self.mutable = self.es_mutable()

    def es_mutable(self):
        return True if self.n == 0 else False

    def __repr__(self):
        return ("[{}]".format(self.n))

    def __eq__(self, otra):
        return self.n == otra.n

class Sudoku():
    def __init__(self):
        self.sudoku = []


def elegir_quiz(ruta):
    quizzes = []
    with open(ruta) as f:
        for linea in f:
            quizzes.append(linea.rstrip())
    return choice(quizzes)

def convertir_quiz(quiz):
    sudoku = []
    for i in range(TAM_SUDOKU):
        linea = quiz[i*TAM_SUDOKU:i*TAM_SUDOKU+TAM_SUDOKU]
        sudoku.append([Celda(n) for n in linea])
    return sudoku


def pruebas():
    tablero = convertir_quiz(elegir_quiz("quizzes.csv"))
    print("INICIANDO COMPARACIONES")
    linea = tablero[0]
    for i in range(TAM_SUDOKU):
        print("{} ** {} --> {}".format(linea[0], linea[i], linea[0] == linea[i]))
