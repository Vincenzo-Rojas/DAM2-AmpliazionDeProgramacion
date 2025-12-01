# DAM2-AmpliazionDeProgramacion

# Sistema de Detección de Intrusos con Webcam

## Descripción

Este proyecto implementa un **Sistema de Detección de Intrusos** utilizando **Java** y **OpenCV**. El sistema captura video en tiempo real desde una webcam, detecta movimiento o presencia de objetos no autorizados y genera alertas visuales y sonoras. Además, cuenta con una **interfaz gráfica** para monitorear el estado del sistema y registrar las detecciones.

---

## Funcionalidades

### Funcionalidades Obligatorias
- Captura de video en tiempo real desde webcam (OpenCV VideoCapture)
- Detección de movimiento mediante análisis de frames
- Alertas visuales y sonoras al detectar intrusos
- Interfaz gráfica con:
  - Video en vivo
  - Estado del sistema (activo/inactivo)
  - Registro de detecciones
  - Controles para iniciar/detener vigilancia

### Funcionalidades Adicionales (Extras)
- Configuración de sensibilidad de detección
- Grabación automática de video al detectar movimiento
- Envío de notificaciones por email o servicios en la nube
- Detección de múltiples objetos simultáneamente
- Configuración de zonas de vigilancia específicas

---

## Requisitos Técnicos

- Java 11 o superior
- OpenCV 4.x para Java
- Java Swing o JavaFX (para la GUI)
- Java Sound API (para alertas sonoras)
- Sistema operativo: Windows, macOS o Linux

