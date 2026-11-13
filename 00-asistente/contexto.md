# Contexto del asistente (handoff entre sesiones)
Última actualización: 2026-11-13

Lee esto y `CLAUDE.md` al empezar. Es el resumen de todo lo acordado hasta hoy.

## Quién es el usuario
Sebastian. Trabaja en **operaciones / logística**. Su departamento **no tiene jefe**: nadie valida ni da seguimiento,
así que el asistente lleva ese hilo. Las tareas le llegan por **correo del trabajo**, que NO se puede conectar
(la empresa bloquea los conectores). Antes llevaba todo de memoria.

- Horario (UTC-6, America/Mexico_City): entra 9:00, come ~14:00-15:00, sale 18:00. Trabaja **un sábado sí y otro no** (sin programar).
- Mayor fuga de pendientes: **esperar respuesta de otros**. Cuando no le responden, **insiste por el mismo medio**.
- Regla acordada: al terminar un paso, el asistente **crea solo la tarea siguiente** y avisa.
- Ambición: que el asistente lleve el 100% de su vida laboral, personal y proyectos. Este vault es el piloto con trabajo.

## Dónde vive todo
- **Vault (este repo):** `srios446-sketch/vault`, privado en GitHub. Procesos, diario, contactos, perfil.
- **Tablero (fuente principal de tareas):** https://claude.ai/artifact/KdqVnKdKEoxsG2Jhy4xYS2
  Código fuente en `proyectos/tablero.html`. Se lee y escribe con la herramienta ArtifactData
  (colecciones `tasks` y `contacts`). Capacidades: db, assets, downloads, sample.
- **Avisos programados** (hora de Ciudad de México, L-V), atados a la sesión original:
  8:55 resumen del día · 14:25 recordatorio · 17:30 retroalimentación con preguntas de opción múltiple.
  Pueden llegar tarde (hasta una hora).

## Conexiones
- **Gmail personal** (srios446@gmail.com): autorizado para leer y hacer borradores. NUNCA enviar sin confirmación.
  Sirve para lo personal, no para el trabajo.
- **Correo del trabajo:** imposible de conectar. Las tareas entran por chat o por el tablero.
- **Notificaciones al celular:** sin confirmar que lleguen. Remote Control no aparece en su app.
- **Calendario y Drive:** no conectados.

## Campos de una tarea en el tablero (colección `tasks`)
`title, kind ('day'|'week'), date (AAAA-MM-DD; en 'week' es el lunes), done, doneAt, waitingOn, followUp,
notes, createdAt, log[{at,text,by}], proc, procName, step, steps, group, files[{id,url,name,type}]`

## Lo que falta por aprender (preguntar cuando venga al caso)
1. ¿Qué define si una compra va por **flujo interno** (ellos generan factura y OC) o si la **OC la emite otro departamento**?
2. ¿De qué departamento espera la OC de la **bentonita de Playa del Carmen**?
3. ¿Qué área exacta autoriza las órdenes de compra y por qué medio se le pide?
4. ¿Qué es **MADISA**: proveedor, sucursal o cliente?
5. ¿La factura y la OC se generan en **Enkontrol** o en otro sistema?
6. ¿Qué se puede hacer una vez que Cristal da de alta un insumo?
7. ¿Cuál es el próximo **sábado** que trabaja?

## Cómo trabajar con él
Español, directo y breve. No pedirle que llene formatos: él escribe como le hablaría a un compañero y el asistente
lo acomoda. Guardar TODO lo que cuente; si no es claro dónde va, a `bandeja/`. Hacer commit y push en cada cambio.
