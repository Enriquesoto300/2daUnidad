"""
Sistema de Notificaciones - versión funcional en un solo archivo.

Este script combina una implementación simple y funcional de:
- Patrón Observer: Subject (Notificacion) y Observer (Usuario / IObservador)
- Patrón Factory Method: NotificacionFactory que crea INotificacion concretas
- Principios SOLID: breves comentarios donde aplican (SRP, DIP, O/C, L, I)

Ejecuta:
    python SistemaNotificaciones_funcional.py

Salida esperada (ejemplo):
    📧 [Email] Enviando correo electrónico: Nueva actualización disponible (EMAIL)
    [Notificación para Ana]: Nueva actualización disponible (EMAIL)
    [Notificación para Carlos]: Nueva actualización disponible (EMAIL)
    ...
"""

from abc import ABC, abstractmethod
from typing import List


# ==============================
# Observer: interfaz y clases
# ==============================
class IObservador(ABC):
    """Interfaz del Observador (I of SOLID: Interface Segregation)."""

    @abstractmethod
    def actualizar(self, mensaje: str) -> None:
        """Recibe la actualización desde el sujeto."""
        pass


class Usuario(IObservador):
    """
    Implementación concreta de un observador.
    SRP: esta clase sólo representa/gestiona la recepción de mensajes para un usuario.
    """

    def __init__(self, nombre: str, email: str, telefono: str):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def actualizar(self, mensaje: str) -> None:
        """Acción al recibir una notificación (simulación)."""
        print(f"[Notificación para {self.nombre}]: {mensaje}")


class Notificacion:
    """
    Sujeto del patrón Observer.
    Mantiene la lista de observadores y los notifica.
    DIP: depende de la abstracción IObservador (no de clases concretas).
    """

    def __init__(self):
        self._observadores: List[IObservador] = []

    def agregar_observador(self, observador: IObservador) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: IObservador) -> None:
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, mensaje: str) -> None:
        # Iteramos sobre una copia en caso de que un observador se elimine durante la notificación
        for obs in list(self._observadores):
            obs.actualizar(mensaje)


# ==============================
# Factory: interfaz y clases
# ==============================
class INotificacion(ABC):
    """Interfaz para canales de notificación (DIP e I: interfaces específicas)."""

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass


class EmailNotificacion(INotificacion):
    """Simula el envío por correo electrónico."""

    def enviar(self, mensaje: str) -> None:
        # Aquí se podría integrar SMTP; por ahora, sólo imprimimos simulando envío.
        print(f"📧 [Email] Enviando correo electrónico: {mensaje}")


class SMSNotificacion(INotificacion):
    """Simula el envío por SMS."""

    def enviar(self, mensaje: str) -> None:
        # Integración real con proveedor SMS (Twilio, etc.) en implementación real.
        print(f"📱 [SMS] Enviando SMS: {mensaje}")


class PushNotificacion(INotificacion):
    """Simula el envío por notificación push."""

    def enviar(self, mensaje: str) -> None:
        # Integración real con Firebase/Apple push en implementación real.
        print(f"🔔 [Push] Enviando notificación push: {mensaje}")


class NotificacionFactory:
    """
    Factory Method: crea objetos INotificacion sin exponer clases concretas.
    Open/Closed: para agregar un nuevo canal, crear una clase que implemente INotificacion
    y añadirla aquí (o mejor: usar un registro dinámico para evitar modificar la fábrica).
    """

    @staticmethod
    def crear_notificacion(tipo: str) -> INotificacion:
        tipo_norm = (tipo or "").strip().lower()
        if tipo_norm == "email":
            return EmailNotificacion()
        elif tipo_norm == "sms":
            return SMSNotificacion()
        elif tipo_norm == "push":
            return PushNotificacion()
        else:
            raise ValueError(f"Tipo de notificación no válido: {tipo}")


# ==============================
# Demo / Uso
# ==============================
def main() -> None:
    # Crear usuarios (observadores)
    usuario1 = Usuario("Ana", "ana@example.com", "+52-55-1111")
    usuario2 = Usuario("Carlos", "carlos@example.com", "+52-55-2222")
    usuario3 = Usuario("Bea", "bea@example.com", "+52-55-3333")

    # Crear sujeto (gestor de suscripciones / notificaciones)
    sistema = Notificacion()
    sistema.agregar_observador(usuario1)
    sistema.agregar_observador(usuario2)
    sistema.agregar_observador(usuario3)

    # Enviar notificaciones por distintos canales usando la fábrica
    for tipo in ("email", "sms", "push"):
        print("\n=== Canal:", tipo.upper(), "===")
        notificador = NotificacionFactory.crear_notificacion(tipo)
        mensaje = f"Nueva actualización disponible ({tipo.upper()})"
        # 1) el canal realiza su envío (simulado)
        notificador.enviar(mensaje)
        # 2) el sujeto notifica a todos los observadores (simulación de entrega interna)
        sistema.notificar_observadores(mensaje)

    # Ejemplo: un usuario se da de baja
    sistema.eliminar_observador(usuario2)
    print("\n--- Carlos se dio de baja ---\n")
    notificador = NotificacionFactory.crear_notificacion("email")
    mensaje_final = "Actualización crítica: mantenimiento programado"
    notificador.enviar(mensaje_final)
    sistema.notificar_observadores(mensaje_final)


if __name__ == "__main__":
    main()


