class Stack:
    def __init__(self):
        self.items = []  # Lista para almacenar los elementos
    
    def push(self, item):
        self.items.append(item)  # Agrega un elemento al final
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Elimina y retorna el último elemento
        return None  # Retorna None si la pila está vacía
    
    def is_empty(self):
        return len(self.items) == 0  # Verifica si la pila está vacía
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # Retorna el último elemento sin eliminarlo
        return None  # Retorna None si la pila está vacía
    
    def size(self):
        return len(self.items)  # Retorna el tamaño de la pila