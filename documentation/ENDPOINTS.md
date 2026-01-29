## `/api/users`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas |
|------|------|-----------|--------|--------|------|
| GET | ✅ | ❌ | ❌ | ❌ | Lista todos los usuarios |
| POST | ✅ | ✅ | ✅ | ✅ | Solo admin setea `is_club_owner` |

---

## `/api/users/:id`

| Método | Admin | Club Owner | Jugador | Anónimo | Notas |
|------|------|-----------|--------|--------|------|
| GET | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Consulta por ID |
| PATCH | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Edición parcial |
| DELETE | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Eliminación |

---

### `/api/courts`

| Método | Admin | Club Owner | Jugador | Descripción |
|------|------|------------|---------|-------------|
| GET  | ✅ | ✅ (solo propias) | ❌ | Lista de canchas |
| POST | ✅ | ✅ (propias) | ❌ | Crear cancha |

---

### `api/courts/:id`

| Método      | Admin | Club Owner       | Jugador | Descripción     |
| ----------- | ----- | ---------------- | ------- | --------------- |
| GET         | ✅     | ✅ (solo propias) | ❌       | Obtener cancha  |
| PATCH       | ✅     | ✅ (solo propias) | ❌       | Editar cancha   |
| DELETE      | ✅     | ✅ (solo propias) | ❌       | Eliminar cancha |

