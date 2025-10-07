#  Sistema de Notificaciones — Patrón Observer + Factory Method

##  Descripción General

Este proyecto implementa un **Sistema de Notificaciones** en Python que combina los patrones de diseño **Observer** y **Factory Method**, aplicando además los **principios SOLID** para asegurar un código modular, extensible y mantenible.

El sistema simula el envío de notificaciones (correo electrónico, SMS o push) a múltiples usuarios registrados, permitiendo agregar o eliminar observadores dinámicamente.

---



---

##  Ejecución

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Enriquesoto300/2daUnidad.git
   cd 2daUnidad
   ```

2. Ejecuta el programa principal:

   ```bash
   python observer.py
   ```

3. Modifica el tipo de notificación en `observer.py` para probar diferentes canales:

   ```python
   tipo = "sms"   # También puede ser "email" o "push"
   ```

---

##  Patrones Implementados

###  **Observer**

Permite que múltiples usuarios (observadores) reciban actualizaciones automáticas desde el sujeto (la clase `Notificacion`).

* **Ventaja:** Se desacopla el emisor de los receptores.
* **Ejemplo:** Cuando se genera un mensaje, todos los usuarios registrados reciben una notificación al instante.

###  **Factory Method**

Permite crear objetos de notificación sin especificar la clase concreta.

* **Ventaja:** Facilita la extensión del sistema (por ejemplo, agregar `WhatsAppNotificacion` sin modificar el código existente).
* **Ejemplo:** `NotificacionFactory` decide dinámicamente si crear un correo, SMS o notificación push.

---

##  Principios SOLID Aplicados

* **S (Single Responsibility):**
  Cada clase tiene una única responsabilidad (por ejemplo, `Usuario` solo maneja la recepción de notificaciones).

* **O (Open/Closed):**
  El sistema puede extenderse (nuevos tipos de notificación) sin modificar las clases existentes.

* **L (Liskov Substitution):**
  Las subclases (`EmailNotificacion`, `SMSNotificacion`, etc.) pueden sustituir a su clase base `INotificacion` sin alterar el comportamiento.

* **I (Interface Segregation):**
  Se usan interfaces separadas (`IObservador`, `INotificacion`) para evitar dependencias innecesarias.

* **D (Dependency Inversion):**
  `observer.py` depende de las abstracciones (`INotificacion` y `IObservador`), no de implementaciones concretas.

---

##  Ejemplo de Salida

```
📧 Enviando correo electrónico: Nueva actualización disponible 
[Notificación para Ana]: Nueva actualización disponible 
[Notificación para Carlos]: Nueva actualización disponible 
```

---

##  Autor

**Enrique Soto**
Proyecto académico — Aplicación de patrones de diseño y principios SOLID en Python.
Repositorio: [https://github.com/Enriquesoto300/2daUnidad](https://github.com/Enriquesoto300/2daUnidad)
