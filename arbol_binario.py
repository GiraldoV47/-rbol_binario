class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)

    def inorder(self, nodo):
        if nodo:
            self.inorder(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorder(nodo.derecha)

    def preorder(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self.preorder(nodo.izquierda)
            self.preorder(nodo.derecha)

    def postorder(self, nodo):
        if nodo:
            self.postorder(nodo.izquierda)
            self.postorder(nodo.derecha)
            print(nodo.valor, end=" ")

# Ejecución
if __name__ == "__main__":
    arbol = ArbolBinario()
    datos = [50, 30, 20, 40, 70, 60, 80]
    for d in datos:
        arbol.insertar(d)

    print("--- Resultados del Arbol Binario ---")
    print("Inorder (Ordenado):")
    arbol.inorder(arbol.raiz)
    print("\n\nPreorder (Raiz-Izq-Der):")
    arbol.preorder(arbol.raiz)
    print("\n\nPostorder (Izq-Der-Raiz):")
    arbol.postorder(arbol.raiz)