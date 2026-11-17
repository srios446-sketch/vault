# Proceso: REQUISICIÓN -> COMPRAS -> ENTREGA
Explicado por el usuario el 2026-11-17 (caso: requisiciones de baterías de litio).
Este es el camino en el que la OC NO la emite él.

1. **Se levanta la requisición** (ej. "REQUI BATERÍAS PD26 CANCÚN")
2. **Se coloca al departamento de COMPRAS**
3. **Adriana Ortega (Compras)** realiza la compra
4. Cuando su proceso está listo, **Adriana coloca la Orden de Compra**
5. **Avisa por correo** que ya quedó la compra  <-- ESPERA: aquí es donde se atoran las cosas
6. **Comienza el proceso de entrega**

## Dependencias
- El paso 5 es una ESPERA con Adriana Ortega. Registrar "esperando a" y fecha de seguimiento.
- El paso 6 NO puede empezar hasta que llegue ese correo.
- Al llegar el aviso de Adriana, el asistente debe crear sola la tarea de seguimiento de entrega.

## Bentonita: CONFIRMADO (2026-11-17)
"Bentonita Playa del Carmen" espera la OC de **Adriana Ortega, de Compras**.
Es el mismo proceso de requisicion. Ya quedo marcada asi en el tablero.

## Los dos caminos de compra, ahora más claros
| | Flujo interno (filtros MADISA) | Requisición a Compras (baterías, bentonita) |
|---|---|---|
| Quién hace la OC | Ellos mismos | Adriana Ortega, de Compras |
| Qué dispara el siguiente paso | Generar factura y OC | El correo de Adriana avisando |
| Paso final | Flujo de pago la semana siguiente | Proceso de entrega |

## QUÉ DETERMINA EL CAMINO: EL MONTO (confirmado 2026-11-17)
Una compra va por **flujo interno** (ellos generan factura y OC) o por **requisición a Compras**
(Adriana Ortega coloca la OC) **según el monto**.
FALTA SABER: cuál es el monto límite y quién lo fija. Preguntarlo cuando aparezca una compra nueva.

Regla para el asistente: al registrar una compra, preguntar el monto si no se sabe.
Con el monto se sabe qué camino sigue y, por lo tanto, qué tarea crear después.

## Requisiciones abiertas del 2026-11-17 (mismo proceso, distintas obras)
- PD18
- PD23 Playa del Carmen
- PD 22 Morelia
- PD26 Cancún
- Pilas de litio (requi aparte)
