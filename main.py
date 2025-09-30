from stack import Stack
from queue import Queue
from hashtable import HashTable

# Pila
pila = Stack()
pila.push(1)
pila.push(2)
print("Pop de pila:", pila.pop())  # 2

# Cola
cola = Queue()
cola.enqueue("A")
cola.enqueue("B")
print("Dequeue de cola:", cola.dequeue())  # A

# Tabla hash
tabla = HashTable()
tabla.agregar("x", 100)
tabla.agregar("y", 200)
print("Valor de 'x':", tabla.obtener("x"))  # 100