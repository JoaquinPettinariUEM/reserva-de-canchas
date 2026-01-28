# Scope del sistema

### 👉 Objetivo del backend

Un sistema básico de reservas de canchas deportivas donde:
- Existen 3 deportes fijos: Fútbol, Tenis, Pádel
- Hay usuarios con roles
- Se pueden crear canchas
- Se pueden crear / unirse a partidos
- Se controlan permisos por rol

### 👉 Lo que NO está incluido

- No pagos reales
- No geolocalización real
- No disponibilidad compleja tipo Google Calendar
- No notificaciones
- No equipos balanceados

# Roles (perfectos como los planteaste)

### 👑 Admin

- Control total
- Puede crear usuarios con cualquier rol
- Puede crear canchas de cualquier club
- Puede borrar lo que sea

### 🏟️ Club / Organización

- Tiene canchas propias
- Administra sus canchas
- Puede cancelar partidos en sus canchas
- *NO* puede borrar usuarios

### 🧍 Jugador

- Se registra
- Ve partidos disponibles
- Se anota a partidos
- Modifica su perfil
