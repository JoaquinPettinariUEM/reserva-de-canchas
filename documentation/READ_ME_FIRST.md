# Backend – Sistema de Reservas de Canchas Deportivas

Este backend implementa un **sistema básico de reservas de canchas deportivas**, desarrollado con **Django + Django REST Framework**, con control de permisos por rol y una estructura pensada para reflejar el funcionamiento real de una aplicación de este tipo.

---

## 🎯 Scope del sistema

### 👉 Objetivo del backend

El sistema permite:

- Gestionar **usuarios con distintos roles**
- Administrar **canchas deportivas**
- Crear y administrar **partidos**
- Permitir que jugadores se unan a partidos
- Aplicar **reglas de negocio y permisos** según el rol del usuario

Deportes soportados:
- Fútbol
- Tenis
- Pádel

[Endpoints del proyecto](https://github.com/JoaquinPettinariUEM/reserva-de-canchas/blob/main/documentation/ENDPOINTS.md)

---

### 👉 Lo que **NO** está incluido

Este backend **no implementa**:

- Pagos reales
- Geolocalización
- Calendarios avanzados tipo Google Calendar
- Notificaciones push o email
- Algoritmos de armado de equipos balanceados

> El foco está en **modelado de dominio**, **roles**, **permisos** y **flujos reales de uso**.

---

## 🧑‍🤝‍🧑 Roles del sistema

### 👑 Admin

Usuario con control total del sistema.

- Puede crear usuarios con cualquier rol
- Puede crear, editar y borrar canchas de cualquier club
- Puede eliminar partidos
- Puede eliminar usuarios
- No tiene restricciones de acceso

---

### 🏟️ Club / Organización

Representa a un club o entidad dueña de canchas.

- Posee canchas propias
- Administra sus canchas
- Puede crear partidos en sus canchas
- Puede cancelar partidos en sus canchas
- **No puede** borrar usuarios
- **No puede** administrar canchas de otros clubes

---

### 🧍 Jugador

Usuario final del sistema.

- Se registra
- Visualiza canchas y partidos disponibles
- Se anota a partidos
- Puede abandonar partidos
- Puede modificar su perfil
- No puede crear canchas ni partidos

---

## 🧱 Arquitectura general

El backend está organizado en **módulos independientes** (apps). Observar el [modelo entidad relación](https://github.com/JoaquinPettinariUEM/reserva-de-canchas/blob/main/documentation/Reserva%20canchas.pdf)

- `users`: usuarios y roles
- `courts`: canchas deportivas
- `matches`: partidos
- `match_players`: relación jugadores ↔ partidos

Cada módulo contiene:
- Modelos
- Serializers
- Vistas
- Permisos específicos

---

## 🔐 Seguridad y permisos

El sistema utiliza:

- Autenticación basada en usuario
- Control de acceso por rol
- Validaciones a nivel:
  - Vista
  - Serializer
  - Modelo (cuando aplica)

Esto evita:
- Accesos indebidos
- Modificaciones no autorizadas
- Inconsistencias de datos

---

## 👑 Historias de Usuario – Admin

### Gestión de usuarios

- Como **admin**, quiero crear usuarios con cualquier rol para administrar el sistema.
- Como **admin**, quiero listar todos los usuarios para tener control general.
- Como **admin**, quiero editar los datos de cualquier usuario.
- Como **admin**, quiero eliminar usuarios que incumplen reglas.

### Gestión de canchas

- Como **admin**, quiero crear canchas para cualquier club.
- Como **admin**, quiero editar cualquier cancha del sistema.
- Como **admin**, quiero eliminar canchas existentes.
- Como **admin**, quiero ver todas las canchas sin restricciones.

### Gestión de partidos

- Como **admin**, quiero crear partidos en cualquier cancha.
- Como **admin**, quiero cancelar cualquier partido.
- Como **admin**, quiero ver todos los partidos del sistema.
- Como **admin**, quiero eliminar partidos con conflictos.

### Control general

- Como **admin**, quiero poder acceder a toda la información sin limitaciones.
- Como **admin**, quiero mantener la integridad del sistema.

---

## 🏟️ Historias de Usuario – Club / Organización

### Gestión de canchas propias

- Como **club**, quiero crear canchas propias.
- Como **club**, quiero editar la información de mis canchas.
- Como **club**, quiero definir duración máxima de partidos.
- Como **club**, quiero establecer precios por hora.
- Como **club**, quiero eliminar canchas que ya no uso.

### Gestión de partidos

- Como **club**, quiero crear partidos en mis canchas.
- Como **club**, quiero ver todos los partidos de mis canchas.
- Como **club**, quiero cancelar partidos en mis canchas.

### Restricciones

- Como **club**, no quiero poder modificar canchas de otros clubes.
- Como **club**, no quiero poder borrar usuarios.
- Como **club**, quiero que el sistema valide que soy dueño de la cancha.

---

## 🧍 Historias de Usuario – Jugador

### Registro y perfil

- Como **jugador**, quiero registrarme en el sistema.
- Como **jugador**, quiero editar mis datos personales.
- Como **jugador**, quiero ver mi información de perfil.

### Visualización

- Como **jugador**, quiero ver todas las canchas disponibles.
- Como **jugador**, quiero ver partidos abiertos.
- Como **jugador**, quiero ver detalles de un partido.
- Como **jugador**, quiero saber cuántos jugadores faltan para un partido.

### Participación en partidos

- Como **jugador**, quiero unirme a un partido.
- Como **jugador**, quiero abandonar un partido.
- Como **jugador**, quiero evitar anotarme dos veces al mismo partido.
- Como **jugador**, quiero que el sistema valide el cupo máximo.
- Como **jugador**, quiero ver los partidos en los que estoy anotado.

### Restricciones

- Como **jugador**, no quiero poder crear canchas.
- Como **jugador**, no quiero poder cancelar partidos ajenos.
- Como **jugador**, no quiero poder ver información sensible de otros usuarios.

---

## ℹ️ Base de datos

Se adopta una base de datos MqSql desde un inicio por lo que no es necesaria una migración desde SQLite a MySql

---

## 🚧 Limitaciones y Posibles Mejoras

### 🧑‍🤝‍🧑 Gestión de Usuarios

**Sin recuperación de contraseña**:
No existe flujo de:
  - Forgot password
  - Reset password
  - Verificación por email

### 🏟️ Gestión de Canchas y Partidos

**Disponibilidad simplificada**:  
El sistema no valida:
  - Superposición de horarios
  - Bloqueos por mantenimiento
  - Horarios no laborables

- **Sin manejo de estados avanzados**:
  - Un partido solo existe o se cancela
  - No hay estados como:
    - Programado
    - Confirmado
    - Cancelado
    - Finalizado

### 📦 Base de Datos

**Sin manejo de concurrencia**:
  - No se manejan locks para evitar:
    - Overbooking
    - Anotaciones simultáneas al mismo partido

### 📡 Manejo de Errores

- **Errores genéricos**:
  Al usar algunos serializers de DJANGO se pierde un poco el control de la descripción de errores.

  Mejoras posibles:
  - Estandarizar errores (códigos + mensajes)
  - Manejo global de excepciones
  - Mensajes orientados al frontend

---

## 📝 Conclusiones y Observaciones

La separación entre:

- Modelos
- Serializers
- Vistas

permite comprender fácilmente el dominio y escalar el sistema sin generar mucha investigación previa.

El uso de **Docker** simplifica el setup del entorno, evitando problemas de dependencias, y el uso de **variables de entorno** permite mantener las credenciales fuera del código fuente.

Este backend sienta una base sobre la cual se podría implementar funcionalidades más avanzadas como:
- Pagos
- Notificaciones
- Disponibilidad compleja
- Reportes
- Métricas

Para una primera interacción básica el sistema cumple, permitiendo escalabilidad a futuro en el caso que se continuara el proyecto.

---

## ⚙️ Comandos útiles

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cd config
python manage.py makemigrations
python manage.py migrate

python manage.py runserver

Comandos personales:
// Inicializa el proyecto
django-admin startproject config

// Crear módulo
python manage.py startapp users

// Crear superusuario
python manage.py createsuperuser

// Correr los seeds
python manage.py seed_all

```
