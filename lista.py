#lista.py - Lista simplemente enlazada de clientes registrados

class NodoLista:
    #Nodo con los datos del cliente y la unión al siguiente nodo
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        # valida que la lista esté vacía: O(1)
        return self.cabeza is None

    def agregar(self, dni, nombre):
        # agrega el dato del cliente al final de la lista: O(n) -> recorre hasta el final
        nuevo = NodoLista(dni, nombre)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamano += 1

    def buscar_por_nombre(self, nombre):
        # buscar_por_nombre: O(n) -> se revisan todos los nodos hasta encontrar el nombre o el primero si está duplicado
        buscado = nombre.strip().lower()
        actual = self.cabeza
        while actual is not None:
            if actual.nombre.lower() == buscado:
                return (actual.dni, actual.nombre)
            actual = actual.siguiente
        return None

    def buscar_por_dni(self, dni):
        # buscar_por_dni: O(n) -> evita registrar clientes duplicados
        actual = self.cabeza
        while actual is not None:
            if actual.dni == dni:
                return (actual.dni, actual.nombre)
            actual = actual.siguiente
        return None

    def eliminar_por_dni(self, dni):
        # eliminar_por_dni: O(n) -> se necesita el nodo anterior para reenlazar
        anterior = None
        actual = self.cabeza
        while actual is not None:
            if actual.dni == dni:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self.tamano -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar(self):
        # mostrar: O(n) -> recorre desde la cabeza hasta el final
        clientes = []
        actual = self.cabeza
        while actual is not None:
            clientes.append((actual.dni, actual.nombre))
            actual = actual.siguiente
        return clientes


def probar():
   #Ejemplo de uso de la lista enlazada
    lista = ListaEnlazada()
    assert lista.esta_vacia() and lista.mostrar() == []
    lista.agregar("111", "Ana Pérez")
    lista.agregar("222", "Luis Mora")
    lista.agregar("333", "Marta Ruiz")
    assert lista.mostrar() == [("111", "Ana Pérez"), ("222", "Luis Mora"), ("333", "Marta Ruiz")]
    assert lista.buscar_por_nombre("luis mora") == ("222", "Luis Mora")
    assert lista.buscar_por_nombre("Nadie") is None
    assert lista.buscar_por_dni("333") == ("333", "Marta Ruiz")
    assert lista.eliminar_por_dni("222") is True
    assert lista.eliminar_por_dni("999") is False
    assert lista.tamano == 2
    print("[OK] Lista enlazada: agregar, buscar, eliminar y mostrar")


if __name__ == "__main__":
    probar()
