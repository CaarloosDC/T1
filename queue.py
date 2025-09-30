class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento):
        # Agrega un elemento al final de la cola
        self.items.append(elemento)

    def dequeue(self):
        # Elimina el primer elemento
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        # Muestra el primer elemento sin sacarlo
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Verifica si la cola está vacía
        return len(self.items) == 0

    def size(self):
        # Devuelve el número de elementos
        return len(self.items)