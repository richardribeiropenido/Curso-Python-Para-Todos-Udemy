import sys


class Exemplo_01(object):
    def __init__(self):
        self.contador = 0
        print("Limite recursividade:", sys.getrecursionlimit())
        sys.setrecursionlimit(10)
        print("Limite de recursividade", sys.getrecursionlimit())

    def funcao_recursiva(self):
        self.contador += 1
        print("Contador: ", self.contador)
        if self.contador < sys.getrecursionlimit():
            self.funcao_recursiva()


e = Exemplo_01()
e.funcao_recursiva()
