# FarmaciasAPE
# Autor

Fabricio Josue Ruiz Aguilar "Michu117"

# Descripción del Problema:
Se requiere el desarrollo de un sistema de gestión para una cadena de farmacias con múltiples sucursales, cuyo principal objetivo es permitir la venta de medicamentos en una sucursal determinada. Si el producto no está disponible en la sucursal solicitada, el sistema debe permitir la venta del medicamento desde otra sucursal, con la opción de que el cliente pueda retirarlo en la sucursal de origen o recibirlo directamente en la sucursal donde realizó la compra.
El sistema se desarrollará utilizando el framework Django, permitiendo la gestión de inventarios, ventas, transferencias entre sucursales y seguimiento de pedidos.

## Características del Proyecto
**1. Gestión de Inventario:** Controlar el stock de medicamentos en cada sucursal.

**2. Venta de Medicamentos:** Permitir la venta de productos disponibles en la sucursal.

**3. Transferencias entre Sucursales:** Habilitar la compra de medicamentos desde otra sucursal en caso de falta de stock local.

**4. Opciones de Entrega:** Ofrecer la opción de retirar el medicamento en la sucursal o enviarlo a la sucursal de origen.

**5. Registro de Clientes y Pedidos:** Gestionar clientes, pedidos y seguimiento de entrega.

**6. Autenticación de Usuarios:** Roles para administrador, empleado de sucursal y cliente.

## Diagrama de Clases
![image](https://github.com/user-attachments/assets/8b06ddfc-c182-46d4-9e4d-20d3fd9876d2)

## Archivos Importantes
1. [models.py](https://github.com/Michu117/FarmaciasAPE/blob/main/FarmaciasAPE/Farmacia/models.py)

2. [admin.py](https://github.com/Michu117/FarmaciasAPE/blob/main/FarmaciasAPE/Farmacia/admin.py)

3. [forms.py](https://github.com/Michu117/FarmaciasAPE/blob/main/FarmaciasAPE/Farmacia/forms.py)

4. [views.py](https://github.com/Michu117/FarmaciasAPE/blob/main/FarmaciasAPE/Farmacia/views.py)

5. [urls.py](https://github.com/Michu117/FarmaciasAPE/blob/main/FarmaciasAPE/FarmaciasAPE/urls.py)

6. [templates](https://github.com/Michu117/FarmaciasAPE/tree/main/FarmaciasAPE/templates)

## Tecnologías Utilizadas

- **Lenguaje:** Python
- **Framework:** Django

## Capturas de la Interfaz:
- El sitio por defecto es el apartado de login.
![image](https://github.com/user-attachments/assets/5ab9edda-2d8e-4984-8632-d6cf7f9385e1)

- localhost:8000/register/
Es el apartado para registrar a un nuevo usuario como Cliente, el cual no puede acceder a admin.
![image](https://github.com/user-attachments/assets/ea1f0016-ad12-4c67-8248-2e4552543700)

- http://localhost:8000/home/
Es el Home y Menú Principal.
![image](https://github.com/user-attachments/assets/706034d4-3e5b-4910-831b-3f61148b25f1)

- http://localhost:8000/inventario/
Apartado donde se pueden visualizar los inventarios
![image](https://github.com/user-attachments/assets/e9424e76-33af-4387-a265-63ce8eb81e63)

- http://localhost:8000/inventario/nuevo/
Apartado para agregar un nuevo inventario.
![image](https://github.com/user-attachments/assets/12138ce8-348b-441f-8309-075fd3b670ed)

- http://localhost:8000/transferencias/
Apartado para visualizar las transferencias entre sucursales.
![image](https://github.com/user-attachments/assets/32aa6938-7dd7-45f4-bc01-536d7a3750f5)

- http://localhost:8000/transferencias/crear/
Apartado para crear transferencias entre sucursales.
![image](https://github.com/user-attachments/assets/f0abf8b7-428c-4b34-bf64-421058aa97c1)

- http://localhost:8000/medicamentos/
Lista de Medicamentos y Agregar más.
![image](https://github.com/user-attachments/assets/bd3396ad-878c-47e6-9f39-d3f39259d94b)

- http://localhost:8000/facturas/
Apartado para visualizar las facturas generadas.
![image](https://github.com/user-attachments/assets/bd460835-c2fb-4b7d-b354-3f2837ed2d6d)

- http://localhost:8000/factura/crear/
Apartado para crear facturas.
![image](https://github.com/user-attachments/assets/37f1d0be-c5ec-4407-b403-d9988d40ef07)

## Reflexión

El sistema FarmaciasAPE propuesto representa un enfoque integral y bien organizado para resolver un problema práctico en la gestión de la cadena de farmacias. El producto es capaz de satisfacer la necesidad de disponibilidad del producto en todas las sucursales, no solo mejorando la experiencia del cliente sino también mejorando las operaciones internas de la empresa. El uso de Django como marco de trabajo mejora la solidez técnica del proyecto, aprovechando su potencia para desarrollar funciones importantes como la gestión de inventario, las transferencias y la autenticación de usuarios con un rol específico. Además, las capturas de pantalla proporcionadas muestran una interfaz clara y fácil de usar que facilita Interacción entre clientes, empleados y administradores.


