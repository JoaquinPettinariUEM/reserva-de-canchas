```
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
| PUT | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Edición |
| PATCH | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Edición parcial |
| DELETE | ✅ | ⚠️ solo él mismo | ⚠️ solo él mismo | ❌ | Eliminación |

---
```
