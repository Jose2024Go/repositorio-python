class ColaSimple: 
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None] * (self.max + 1)
        self.front = 0
        self.back = 0

    def es_llena(self):
        return (self.back + 1) % (self.max + 1) == self.front

    def es_vacia(self):
        return self.front == self.back

    def enqueue(self, dato):
        if not self.es_llena():
            self.cola[self.back] = dato
            self.back = (self.back + 1) % (self.max + 1)
        else:
            print("La cola está llena")

    def dequeue(self):
        if not self.es_vacia():
            dato = self.cola[self.front]
            self.cola[self.front] = None
            self.front = (self.front + 1) % (self.max + 1)
            return dato
        else:
            print("La cola está vacía")
            return None

    def size(self):
        if self.back >= self.front:
            return self.back - self.front
        else:
            return self.max + 1 - self.front + self.back

    def mostrar(self):
        if self.es_vacia():
            print("La cola está vacía")
        else:
            print("Elementos en la cola:", end=" ")
            i = self.front
            while i != self.back:
                print(self.cola[i], end=" ")
                i = (i + 1) % (self.max + 1)
            print()

    def numero_mayor(self):
        if self.es_vacia():
            return None
        mayor = self.cola[self.front]
        i = (self.front + 1) % (self.max + 1)
        while i != self.back:
            if self.cola[i] > mayor:
                mayor = self.cola[i]
            i = (i + 1) % (self.max + 1)
        return mayor

    def numeros_pares(self):
        pares = []
        if self.es_vacia():
            return pares
        i = self.front
        while i != self.back:
            if self.cola[i] % 2 == 0:
                pares.append(self.cola[i])
            i = (i + 1) % (self.max + 1)
        return pares
    
def main():
    max_size = int(input("Ingrese el tamaño máximo de la cola: "))
    cola = ColaSimple(max_size)

    for _ in range(max_size):
        dato = int(input("Ingrese el dato a agregar: "))
        cola.enqueue(dato)
        cola.mostrar()
        print("Tamaño de la cola:", cola.size())
        if cola.es_llena():
            print("La cola está llena")
            break

    while True:
        print("\nOpciones:")
        print("1. Enqueue (Agregar elemento)")
        print("2. Dequeue (Eliminar elemento)")
        print("3. Mostrar cola")
        print("4. Mostrar el número mayor")
        print("5. Mostrar números pares")
        print("6. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            dato = int(input("Ingrese el dato a agregar: "))
            cola.enqueue(dato)
            cola.mostrar()
            print("Tamaño de la cola:", cola.size())
        elif opcion == 2:
            dato = cola.dequeue()
            if dato is not None:
                print(f"Elemento eliminado: {dato}")
            cola.mostrar()
            print("Tamaño de la cola:", cola.size())
        elif opcion == 3:
            if cola.es_llena():
                print("La cola está llena")
            elif cola.es_vacia():
                print("La cola está vacía")
            cola.mostrar()
            print("Tamaño de la cola:", cola.size())
        elif opcion == 4:
            mayor = cola.numero_mayor()
            if mayor is not None:
                print(f"El número mayor en la cola es: {mayor}")
            else:
                print("La cola está vacía")
        elif opcion == 5:
            pares = cola.numeros_pares()
            if pares:
                print("Números pares en la cola:", pares)
            else:
                print("No hay números pares en la cola o la cola está vacía")
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
