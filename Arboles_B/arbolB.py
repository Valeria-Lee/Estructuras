class NodoB:
    def __init__(self, hoja=True):
        self.hoja = hoja
        self.claves = []
        self.hijos = []
        

class ArbolB:
    def __init__(self, grado, t=0):
        self.raiz = NodoB()
        self.grado = grado
        self.t = t

    def insertar(self, valor):
        if valor not in self.buscar(self.raiz, valor):
            if len(self.raiz.claves) == (2 * self.grado) - 1:
                nueva_raiz = NodoB(hoja=False)
                nueva_raiz.hijos.append(self.raiz)
                self._dividir(nueva_raiz, 0, self.raiz)
                self.raiz = nueva_raiz
            self._insertar_no_lleno(self.raiz, valor)

    def _insertar_no_lleno(self, nodo, valor):
        i = len(nodo.claves) - 1
        if nodo.hoja:
            nodo.claves.append(None)
            while i >= 0 and valor < nodo.claves[i]:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = valor
        else:
            while i >= 0 and valor < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == (2 * self.grado) - 1:
                self._dividir(nodo, i, nodo.hijos[i])
                if valor > nodo.claves[i]:
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], valor)

    def _dividir(self, padre, indice, hijo):
        nuevo_nodo = NodoB(hoja=hijo.hoja)
        padre.claves.insert(indice, hijo.claves[self.grado - 1])
        padre.hijos.insert(indice + 1, nuevo_nodo)
        nuevo_nodo.claves = hijo.claves[self.grado:]
        hijo.claves = hijo.claves[:self.grado - 1]
        if not hijo.hoja:
            nuevo_nodo.hijos = hijo.hijos[self.grado:]
            hijo.hijos = hijo.hijos[:self.grado]

    def buscar(self, nodo, valor):
        i = 0
        while i < len(nodo.claves) and valor > nodo.claves[i]:
            i += 1
        if i < len(nodo.claves) and valor == nodo.claves[i]:
            return nodo
        elif nodo.hoja:
            return []
        else:
            return self.buscar(nodo.hijos[i], valor)

    def eliminar(self, x, valor):
        t = self.t
        i = 0
        while i < len(x.claves) and valor > x.claves[i]:
            i += 1
        if x.hoja:
            if i < len(x.claves) and x.claves[i] == valor:
                x.claves.pop(i)
                return
            return

        if i < len(x.claves) and x.claves[i] == valor:
            return self.eliminar_nodo_interno(x, valor, i)
        elif len(x.hijos[i].claves) >= t:
            self.eliminar(x.hijos[i], valor)
        else:
            if i != 0 and i + 2 < len(x.hijo):
                if len(x.hijos[i - 1].claves) >= t:
                    self.eliminar_hermano(x, i, i - 1)
                elif len(x.hijos[i + 1].claves) >= t:
                    self.eliminar_hermano(x, i, i + 1)
                else:
                    self.eliminar_combinar(x, i, i + 1)
            elif i == 0:
                if len(x.hijo[i + 1].claves) >= t:
                    self.eliminar_hermano(x, i, i + 1)
                else:
                    self.eliminar_combinar(x, i, i + 1)
            elif i + 1 == len(x.hijo):
                if len(x.hijo[i - 1].claves) >= t:
                    self.eliminar_hermano(x, i, i - 1)
                else:
                    self.eliminar_combinar(x, i, i - 1)
            self.eliminar(x.hijo[i], valor)

def main():
    arbol_b = ArbolB(grado=2)

    valores_a_insertar = [3, 8, 12, 15, 20, 25, 6, 9, 14]
    for valor in valores_a_insertar:
        arbol_b.insertar(valor)
    
    arbol_b.eliminar(arbol_b.raiz,12)

    valor_buscar = int(input('¿Que valor buscar? -> '))
    nodo_encontrado = arbol_b.buscar(arbol_b.raiz, valor_buscar)
    if nodo_encontrado:
        print(f"El nodo con valor {valor_buscar} ha sido encontrado.")
    else:
        print(f"No se encontró el nodo con valor {valor_buscar} en el árbol B.")

if __name__ == "__main__":
    main()
