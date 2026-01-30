### `/api/auth/login/`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas                             |
| ------ | ----- | ---------- | ------- | ------- | --------------------------------- |
| POST   | ✅     | ✅          | ✅       | ✅       | Devuelve `access` y `refresh` JWT |

--- 

### `/api/auth/token/refresh/`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas                     |
| ------ | ----- | ---------- | ------- | ------- | ------------------------- |
| POST   | ✅     | ✅          | ✅       | ✅       | Renueva el `access token` |

---

### `/api/users/`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas |
|------|------|-----------|--------|--------|------|
| GET | ✅ | ❌ | ❌ | ❌ | Lista todos los usuarios |
| POST | ✅ | ✅ | ✅ | ✅ | Solo admin setea `is_club_owner` |

---

### `/api/users/:id/`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas |
|------|------|-----------|--------|--------|------|
| GET | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Consulta por ID |
| PATCH | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Edición parcial |
| DELETE | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Eliminación |

---

### `/api/courts/`

| Método | Admin | Club Owner | Jugador | Descripción |
|------|------|------------|---------|-------------|
| GET  | ✅ | ✅ (solo propias) | ❌ | Lista de canchas |
| POST | ✅ | ✅ (propias) | ❌ | Crear cancha |

---

### `/api/courts/:id/`

| Método      | Admin | Club Owner       | Jugador | Descripción     |
| ----------- | ----- | ---------------- | ------- | --------------- |
| GET         | ✅     | ✅ (solo propias) | ❌       | Obtener cancha  |
| PATCH       | ✅     | ✅ (solo propias) | ❌       | Editar cancha   |
| DELETE      | ✅     | ✅ (solo propias) | ❌       | Eliminar cancha |

---

### `/api/matches/`

| Método | Admin | Club Owner                     | Jugador | Anónimo | Notas             |
| ------ | ----- | ------------------------------ | ------- | ------- | ----------------- |
| GET    | ✅     | ✅ (solo matches de sus courts) | ✅       | ❌       | Lista de partidos |
| POST   | ✅     | ✅ (solo courts propios)        | ❌       | ❌       | Crear partido     |

---

### `/api/matches/:id/`

| Método | Admin | Club Owner                     | Jugador | Anónimo | Notas            |
| ------ | ----- | ------------------------------ | ------- | ------- | ---------------- |
| GET    | ✅     | ✅                              | ✅       | ❌       | Obtener partido  |
| PATCH  | ✅     | ✅ (solo si es dueño del court) | ❌       | ❌       | Editar partido   |
| DELETE | ✅     | ✅ (solo si es dueño del court) | ❌       | ❌       | Eliminar partido |

---

### `/api/match-players/`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas                  |
| ------ | ----- | ---------- | ------- | ------- | ---------------------- |
| GET    | ✅     | ❌          | ✅       | ❌       | Lista de inscripciones |

---

### `/api/match-players/:id/`

| Método | Admin | Club Owner | Jugador           | Anónimo | Notas             |
| ------ | ----- | ---------- | ----------------- | ------- | ----------------- |
| GET    | ✅     | ❌          | ✅                 | ❌       | Ver inscripción   |
| DELETE | ✅     | ❌          | ⚠️ solo la propia | ❌       | Abandonar partido |

---

### `/api/match-players/create/`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas               |
| ------ | ----- | ---------- | ------- | ------- | ------------------- |
| POST   | ✅     | ❌          | ✅       | ❌       | Unirse a un partido |
