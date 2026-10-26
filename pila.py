#pila.py - Pila (stack) implementada con nodos enlazados.

class NodoPila:
    """Nodo de la pila: guarda un dato y la referencia al nodo inferior."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    #Pila con referencia únicamente al tope.

    def __init__(self):
        self.tope = None
        self.tamano = 0

    def esta_vacia(self):
        # esta_vacia: O(1)
        return self.tope is None

    def push(self, dato):
        # push: O(1) -> se inserta siempre en el tope, sin recorrer nada
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamano += 1

    def pop(self):
        # pop: O(1) -> se retira siempre el tope
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamano -= 1
        return dato

    def peek(self):
        # peek: O(1) -> consulta el tope sin retirarlo
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.tope.dato

    def recorrer(self):
        # recorrer: O(n) -> visita cada nodo desde el tope hacia abajo
        elementos = []
        actual = self.tope
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos


def probar():
    """Caso de prueba de la pila (comportamiento LIFO)."""
    pila = Pila()
    assert pila.esta_vacia()
    pila.push("registrar 111")
    pila.push("registrar 222")
    pila.push("atender 111")
    assert pila.peek() == "atender 111"
    assert pila.pop() == "atender 111"   # sale el último que entró
    assert pila.pop() == "registrar 222"
    assert pila.pop() == "registrar 111"
    assert pila.esta_vacia()
    try:
        pila.pop()
        raise AssertionError("pop en pila vacía debía fallar")
    except IndexError:
        pass
    print("[OK] Pila: LIFO, peek y pila vacía")


if __name__ == "__main__":
    probar()
