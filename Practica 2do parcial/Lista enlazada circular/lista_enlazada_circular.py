from nodo import Nodo  # Importamos la clase Nod
class ListaCircular():
    def __init__(self): 
        self.p = None  # Referencia al primer nodo

    def es_vacia(self):
        return self.p is None

    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.es_vacia():
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.p

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.es_vacia():
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            nuevo_nodo.siguiente = self.p
            self.p = nuevo_nodo
            actual.siguiente = self.p  # El último nodo apunta al nuevo inicio

    def eliminar_inicio(self):
        if self.es_vacia():
            print("La lista está vacía. No hay nada que eliminar.")
            return
        elif self.p.siguiente == self.p:  # Caso especial: solo un nodo
            self.p = None
        else:
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            self.p = self.p.siguiente
            actual.siguiente = self.p  # El último nodo apunta al nuevo inicio

    def eliminar_final(self):
        if self.es_vacia():
            print("La lista está vacía. No hay nada que eliminar.")
            return
        elif self.p.siguiente == self.p:  # Caso especial: solo un nodo
            self.p = None
        else:
            actual = self.p
            anterior = None
            while actual.siguiente != self.p:
                anterior = actual
                actual = actual.siguiente
            anterior.siguiente = self.p  # El penúltimo nodo apunta al inicio

    def mostrar(self):
        if self.es_vacia():
            print("La lista está vacía.")
        else:
            actual = self.p
            while True:
                print(actual.valor, end='-->')
                actual = actual.siguiente
                if actual == self.p:  # Volvemos al inicio
                    break
            print("Vuelve a inicio")

lista_circular = ListaCircular()

# Agregar al final
lista_circular.agregar_final("Ana")
lista_circular.agregar_final("Carlos")
lista_circular.agregar_final("Pedro")
lista_circular.mostrar()

# Agregar al inicio
lista_circular.agregar_inicio("Inicio")
lista_circular.mostrar()

# Eliminar el inicio
lista_circular.eliminar_inicio()
lista_circular.mostrar()

# Eliminar el final
lista_circular.eliminar_final()
lista_circular.mostrar()