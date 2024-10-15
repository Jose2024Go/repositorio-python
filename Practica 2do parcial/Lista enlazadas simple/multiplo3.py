from nodo import Nodo  # Importamos la clase Nodo

class ListaSimple:
    def __init__(self):
        self.p = None
    
    def esta_vacia(self):
        return self.p is None
    
    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.p = nuevo_nodo
        else:
            actual = self.p
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.p
        self.p = nuevo_nodo
    
    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.valor, end=" --> ")
            actual = actual.siguiente  
        print("None")  # Indica el final de la lista

    def eliminar_final(self):
        if self.esta_vacia():
            print("La lista no tiene nodos")
            return None
        elif self.p.siguiente is None:
            nodo_eliminado = self.p
            self.p = None
            return nodo_eliminado
        else:
            actual = self.p
            anterior = None
            while actual.siguiente:
                anterior = actual
                actual = actual.siguiente
            nodo_eliminado = actual
            anterior.siguiente = None
            return nodo_eliminado

    def contar_nodos(self):
        actual = self.p
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador 
    
    def eliminar_inicio(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return None
        else:
            nodo_eliminado = self.p
            self.p = self.p.siguiente
            return nodo_eliminado

    def eliminar_multiplos_de_2(self):
        actual = self.p
        anterior = None
        while actual:
            if actual.valor % 2 == 0:  # Si es múltiplo de 2
                if anterior is None:
                    self.p = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente

    def mostrar_multiplos_de_3(self):
        actual = self.p
        while actual:
            if actual.valor % 3 == 0:
                print(actual.valor, end=" --> ")
            actual = actual.siguiente
        print("None")
    
lista = ListaSimple()

lista.agregar_final(6)
lista.agregar_final(9)
lista.agregar_final(12)
lista.agregar_final(15)

print("Lista original:")
lista.mostrar_lista()

# Eliminar múltiplos de 2
lista.eliminar_multiplos_de_2()

print("\nLista después de eliminar múltiplos de 2:")
lista.mostrar_lista()

# Mostrar solo múltiplos de 3
print("\nMúltiplos de 3 en la lista:")
lista.mostrar_multiplos_de_3()