#main.py - Gestor de turnos del taller CarUPS.

from pila import Pila, probar as probar_pila
from cola import Cola, probar as probar_cola
from lista import ListaEnlazada, probar as probar_lista


class GestorTurnos:
    def __init__(self):
        self.historial = Pila()          # R1
        self.turnos = Cola()             # R2
        self.clientes = ListaEnlazada()  # R3

    def registrar_turno(self, dni, nombre):
        existente = self.clientes.buscar_por_dni(dni)
        nuevo = existente is None
        if nuevo:
            self.clientes.agregar(dni, nombre)
            cliente = (dni, nombre)
        else:
            cliente = existente          # se conserva el nombre ya registrado
        self.turnos.enqueue(cliente)
        self.historial.push({"accion": "registrar", "cliente": cliente, "nuevo": nuevo})
        return cliente

    def atender(self):
        cliente = self.turnos.dequeue()
        self.historial.push({"accion": "atender", "cliente": cliente})
        return cliente

    def deshacer(self):
        accion = self.historial.pop()    # LIFO: se revierte la acción más reciente
        if accion["accion"] == "registrar":
            self.turnos.quitar_ultimo()
            if accion["nuevo"]:
                self.clientes.eliminar_por_dni(accion["cliente"][0])
        else:  # atender
            self.turnos.encolar_al_frente(accion["cliente"])
        return accion


def probar_integracion():
    g = GestorTurnos()
    g.registrar_turno("111", "Ana")
    g.registrar_turno("222", "Luis")
    assert g.atender() == ("111", "Ana")          # FIFO
    g.deshacer()                                   # revierte el atender
    assert g.turnos.recorrer() == [("111", "Ana"), ("222", "Luis")]
    g.deshacer()                                   # revierte registrar Luis
    assert g.turnos.recorrer() == [("111", "Ana")]
    assert g.clientes.buscar_por_dni("222") is None
    print("[OK] Integración: registrar, atender y deshacer")


def ejecutar_pruebas():
    probar_pila()
    probar_cola()
    probar_lista()
    probar_integracion()


def mostrar_menu():
    print("\n=== CarUPS - Gestor de turnos ===")
    print("1. Registrar turno")
    print("2. Atender siguiente")
    print("3. Deshacer última acción")
    print("4. Ver cola de turnos")
    print("5. Buscar cliente por nombre")
    print("6. Ver clientes registrados")
    print("7. Ejecutar pruebas")
    print("0. Salir")


def main():
    gestor = GestorTurnos()
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        try:
            if opcion == "1":
                dni = input("DNI: ").strip()
                nombre = input("Nombre: ").strip()
                if not dni.isdigit() or not nombre:
                    print("DNI (solo números) y nombre son obligatorios.")
                    continue
                c = gestor.registrar_turno(dni, nombre)
                print(f"Turno registrado: {c[1]} (DNI {c[0]}). En cola: {gestor.turnos.tamano}")
            elif opcion == "2":
                c = gestor.atender()
                print(f"Atendiendo a: {c[1]} (DNI {c[0]})")
            elif opcion == "3":
                a = gestor.deshacer()
                print(f"Se deshizo: {a['accion']} de {a['cliente'][1]}")
            elif opcion == "4":
                cola = gestor.turnos.recorrer()
                if not cola:
                    print("No hay turnos en espera.")
                for i, (dni, nombre) in enumerate(cola, 1):
                    print(f"{i}. {nombre} (DNI {dni})")
            elif opcion == "5":
                c = gestor.clientes.buscar_por_nombre(input("Nombre: "))
                print(f"Encontrado: {c[1]} (DNI {c[0]})" if c else "Cliente no encontrado.")
            elif opcion == "6":
                todos = gestor.clientes.mostrar()
                if not todos:
                    print("No hay clientes registrados.")
                for dni, nombre in todos:
                    print(f"- {nombre} (DNI {dni})")
            elif opcion == "7":
                ejecutar_pruebas()
            elif opcion == "0":
                print("Hasta pronto.")
                break
            else:
                print("Opción no válida.")
        except IndexError as e:
            # cola o pila vacías: mensaje claro en lugar de un error
            print(f"No se puede realizar la operación: {e}.")


if __name__ == "__main__":
    main()
