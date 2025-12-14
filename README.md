# 🚗**Proyecto Urban Routes - Automatización de Pruebas**

## 🚙**Descripción del Proyecto**
Este proyecto contiene pruebas automatizadas para la aplicación web Urban Routes, que simula el flujo completo de un usuario solicitando un taxi. Las pruebas cubren desde la configuración de la ruta hasta la confirmación final de la reservacion, incluyendo la selección de tarifa, métodos de pago, y opciones adicionales.

## 🚌**Funcionalidades Probadas**
- Configuración de ruta (dirección de origen y destino)
- Selección de modalidad Flash
- Pedir taxi
- Selección de tarifa Comfort
- Ingreso de número de teléfono y verificación SMS
- Configuración de método de pago (tarjeta de crédito)
- Agregar mensaje para el conductor
- Solicitar manta y pañuelos
- Pedir helado
- Presionar boton de reservación
- Modal de temporizador "Buscar automovil"
- Confirmación final de la reserva en modal "El conductor llegara en "X" min"

## 🏍**Tecnologías Usadas**
- Python 3.x: Lenguaje de programación principal
- Selenium WebDriver: Automatización del navegador web
- PyTest: Framework de pruebas
- Chrome WebDriver: Driver para navegador Chrome

## 🏎**Técnicas de Testing Utilizadas**
- Page Object Model (POM): Patrón de diseño para organizar el código
- Localizadores múltiples: ID, Class Name, XPath, CSS Selectors
- Esperas explícitas: WebDriverWait y Expected Conditions
- Assertions: Verificación de resultados esperados
- Modularización: Separación de métodos, localizadores y datos de prueba

## 🚲**Estructura del Proyecto**

qa-project-Urban-Routes-es/   
├── Home/                    # Configuración de ruta   
├── Flash/                   # Selección de tarifa  
├── Comfort/                 # Tarifa Comfort  
├── Phone/                   # Ingreso de teléfono  
├── SMS/                     # Verificación SMS  
├── Card/                    # Método de pago  
├── Pay_Method/              # Configuración de pago  
├── Card_CVV/                # Verificación CVV  
├── Message/                 # Mensaje al conductor  
├── Blanket_Tissues/         # Opciones adicionales  
├── Reservation/             # Flujo completo de reserva  
├── data.py                  # Datos de prueba  
└── README.md                # Este archivo
