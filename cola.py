#cola.py - Cola (queue) implementada sobre lista enlazada con head y tail.
class NodoCola:
    # Nodo de la cola: guarda el cliente (dni, nombre) y el siguiente nodo.

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamano = 0

    def esta_vacia(self):
        # esta_vacia: O(1)
        return self.head is None

    def enqueue(self, dato):
        # enqueue: O(1)
        nuevo = NodoCola(dato)
        if self.tail is None:# cola vacía
            self.head = nuevo
            self.tail = nuevo
        else:
            self.tail.siguiente = nuevo
            self.tail = nuevo
        self.tamano += 1

    def dequeue(self):
        # dequeue: O(1)
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        dato = self.head.dato
        self.head = self.head.siguiente
        if self.head is None:# la cola quedó vacía
            self.tail = None
        self.tamano -= 1
        return dato

    def frente(self):
        # frente: O(1)
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.head.dato

    # ----- Operaciones de apoyo para poder reversar acciones ------

    def encolar_al_frente(self, dato):
        # encolar_al_frente: O(1) -> deshace un "atender" (devuelve al cliente al frente)
        nuevo = NodoCola(dato)
        nuevo.siguiente = self.head
        self.head = nuevo
        if self.tail is None:
            self.tail = nuevo
        self.tamano += 1

    def quitar_ultimo(self):
        """ quitar_ultimo: O(n) -> deshace un "registrar". En una lista simplemente
        enlazada hay que recorrer hasta el penúltimo nodo para actualizar tail"""
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        if self.head is self.tail:
            return self.dequeue()
        actual = self.head
        while actual.siguiente is not self.tail:
            actual = actual.siguiente
        dato = self.tail.dato
        actual.siguiente = None
        self.tail = actual
        self.tamano -= 1
        return dato

    def recorrer(self):
        # recorrer: O(n) -> de head a tail
        elementos = []
        actual = self.head
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos


def probar():
    """Caso de prueba de la cola (comportamiento FIFO y punteros head/tail)."""
    cola = Cola()
    assert cola.esta_vacia()
    cola.enqueue(("111", "Ana"))
    cola.enqueue(("222", "Luis"))
    cola.enqueue(("333", "Marta"))
    assert cola.frente() == ("111", "Ana")
    assert cola.dequeue() == ("111", "Ana")      # sale el primero que llegó
    assert cola.dequeue() == ("222", "Luis")
    assert cola.tamano == 1
    assert cola.head is cola.tail                # un solo nodo
    assert cola.dequeue() == ("333", "Marta")
    assert cola.esta_vacia() and cola.tail is None
    # Operaciones de apoyo para deshacer
    cola.enqueue(("1", "A"))
    cola.enqueue(("2", "B"))
    assert cola.quitar_ultimo() == ("2", "B")
    cola.encolar_al_frente(("0", "Z"))
    assert cola.recorrer() == [("0", "Z"), ("1", "A")]
    try:
        Cola().dequeue()
        raise AssertionError("dequeue en cola vacía debía fallar")
    except IndexError:
        pass
    print("[OK] Cola: FIFO, head/tail y operaciones de deshacer")


if __name__ == "__main__":
    probar()
