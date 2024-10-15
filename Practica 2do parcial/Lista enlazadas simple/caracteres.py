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
    
    def mostrar_lista(self):
        actual = self.p
        while actual:
            print(actual.valor, end=" --> ")
            actual = actual.siguiente  
        print("None")  # Indica el final de la lista
    
    def mayor_caracter(self):
        if self.esta_vacia():
            return None
        mayor = self.p.valor
        actual = self.p
        while actual:
            if actual.valor > mayor:
                mayor = actual.valor
            actual = actual.siguiente
        return mayor
    
    # Unir dos listas y devolver una nueva lista
    def unir_listas(self, otra_lista):
        nueva_lista = ListaSimple()
        # Agregar elementos de la primera lista
        actual = self.p
        while actual:
            nueva_lista.agregar_final(actual.valor)
            actual = actual.siguiente
        # Agregar elementos de la segunda lista
        actual = otra_lista.p
        while actual:
            nueva_lista.agregar_final(actual.valor)
            actual = actual.siguiente
        return nueva_lista

    def ordenar_alfabeticamente(self):
        lista_python = []
        actual = self.p
        while actual:
            lista_python.append(actual.valor)
            actual = actual.siguiente
        
        # Ordenar la lista
        lista_python.sort()

        # Crear una nueva lista enlazada con los valores ordenados
        lista_ordenada = ListaSimple()
        for valor in lista_python:
            lista_ordenada.agregar_final(valor)
            return lista_ordenada
        
# Crear dos listas de caracteres
lista1 = ListaSimple()
lista2 = ListaSimple()

lista1.agregar_final('a')
lista1.agregar_final('z')
lista1.agregar_final('m')

lista2.agregar_final('b')
lista2.agregar_final('y')
lista2.agregar_final('n')

print("Mayor carácter en lista1:", lista1.mayor_caracter())
print("Mayor carácter en lista2:", lista2.mayor_caracter())

# Unir las dos listas y mostrar
lista_unida = lista1.unir_listas(lista2)
print("\nLista unida:")
lista_unida.mostrar_lista()

# Ordenar la lista unida alfabéticamente y mostrar
lista_ordenada = lista_unida.ordenar_alfabeticamente()
print("\nLista unida ordenada alfabéticamente:")
lista_ordenada.mostrar_lista()