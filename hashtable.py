class HashTable:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)]  # Lista de listas

    def _hash(self, clave):
        # Función hash (usa la función de hash interna de Python)
        return hash(clave) % self.capacidad

    def agregar(self, clave, valor):
        # Inserta un valor con una clave
        indice = self._hash(clave)
        cubeta = self.tabla[indice]

        for i, (k, v) in enumerate(cubeta):
            if k == clave:
                cubeta[i] = (clave, valor)  # actualiza
                return

        cubeta.append((clave, valor))  # agrega nuevo

    def obtener(self, clave):
        # Devuelve el valor según la clave
        indice = self._hash(clave)
        cubeta = self.tabla[indice]

        for k, v in cubeta:
            if k == clave:
                return v

        return None  # no existe

    def eliminar(self, clave):
        # Elimina la clave y su valor
        indice = self._hash(clave)
        cubeta = self.tabla[indice]

        for i, (k, v) in enumerate(cubeta):
            if k == clave:
                del cubeta[i]
                return

    def claves(self):
        # Devuelve todas las claves
        claves = []
        for cubeta in self.tabla:
            for k, v in cubeta:
                claves.append(k)
        return claves

    def valores(self):
        # Devuelve todos los valores
        valores = []
        for cubeta in self.tabla:
            for k, v in cubeta:
                valores.append(v)
        return valores