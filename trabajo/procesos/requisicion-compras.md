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

## Esto explica la bentonita
"Bentonita Playa del Carmen" dice "Esperando Orden de Compra del Dpto de...".
Muy probablemente ese departamento es **Compras** y la persona es **Adriana Ortega**.
CONFIRMAR con el usuario antes de darlo por hecho.

## Los dos caminos de compra, ahora más claros
| | Flujo interno (filtros MADISA) | Requisición a Compras (baterías, bentonita) |
|---|---|---|
| Quién hace la OC | Ellos mismos | Adriana Ortega, de Compras |
| Qué dispara el siguiente paso | Generar factura y OC | El correo de Adriana avisando |
| Paso final | Flujo de pago la semana siguiente | Proceso de entrega |

Falta saber QUÉ determina que una compra vaya por un camino o por el otro.

## Requisiciones abiertas del 2026-11-17 (mismo proceso, distintas obras)
- PD18
- PD23 Playa del Carmen
- PD 22 Morelia
- PD26 Cancún
- Pilas de litio (requi aparte)
