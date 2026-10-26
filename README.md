# Nuñez_Alexnader_AlgEstDatos_U1
Repositorio de programas solicitados en la tarea 1
# Gestor de turnos CarUPS – Unidad 1: Estructuras de datos simples

Programa en Python que gestiona los turnos de atención del taller CarUPS integrando una pila, una cola y una lista enlazada, todas implementadas desde sus nodos (sin `list.append/pop` ni `collections.deque`). Cada cliente se identifica por DNI y nombre.

# Cómo ejecutarlo

```bash
python main.py          # menú de consola
python pila.py          # prueba de la pila
python cola.py          # prueba de la cola
python lista.py         # prueba de la lista
```

La opción 7 del menú ejecuta todas las pruebas (una por estructura y una de integración).

## Estructuras

| Archivo | Estructura | Rol en el programa |

| `pila.py` | Pila (LIFO) con nodos y referencia al tope | Historial de acciones (registrar turno, atender). `pop` permite deshacer la última acción. LIFO es adecuado porque la acción más reciente es la primera que hay que revertir. |
| `cola.py` | Cola (FIFO) sobre lista enlazada con `head` y `tail` | **R2** Turnos en orden de llegada con `enqueue` y `dequeue` en O(1). |
| `lista.py` | Lista simplemente enlazada | **R3** Clientes registrados: agregar, buscar por nombre y mostrar recorriendo desde la cabeza. |
| `main.py` | Menú de consola | Integra las tres estructuras mediante la clase `GestorTurnos`. |

**Cómo se deshace una acción:** al registrar un turno se hace `push` de `{registrar, cliente}`; al atender, `push` de `{atender, cliente}`. Con "Deshacer" se hace `pop` y se revierte: un *registrar* quita al cliente del final de la cola (y de la lista si era nuevo); un *atender* devuelve al cliente al frente de la cola.

## Tabla de complejidades

| Estructura | Operación | Complejidad | Justificación |
|---|---|---|---|
| Pila | `push` | O(1) | Inserta siempre en el tope, sin recorrer nodos. |
| Pila | `pop` | O(1) | Retira siempre el tope. |
| Pila | `peek` | O(1) | Solo lee el tope. |
| Pila | `recorrer` | O(n) | Visita cada nodo una vez. |
| Cola | `enqueue` | O(1) | `tail` apunta al último nodo; se enlaza el nuevo sin recorrer. |
| Cola | `dequeue` | O(1) | `head` apunta al primer nodo; se avanza una posición. |
| Cola | `encolar_al_frente` (deshacer atender) | O(1) | Se enlaza el nuevo nodo antes de `head`. |
| Cola | `quitar_ultimo` (deshacer registrar) | O(n) | Lista simplemente enlazada: hay que recorrer hasta el penúltimo nodo para actualizar `tail`. |
| Lista | `agregar` (al final) | O(n) | No hay referencia a la cola; se recorre hasta el último nodo. |
| Lista | `buscar_por_nombre` / `buscar_por_dni` | O(n) | En el peor caso se revisan todos los nodos. |
| Lista | `eliminar_por_dni` | O(n) | Se busca el nodo y su anterior para reenlazar. |
| Lista | `mostrar` | O(n) | Recorre desde la cabeza hasta el final. |

## Pruebas

Cada estructura incluye una función `probar()` con aserciones (LIFO en la pila, FIFO y punteros `head/tail` en la cola, agregar/buscar/eliminar en la lista). `main.py` agrega una prueba de integración.
