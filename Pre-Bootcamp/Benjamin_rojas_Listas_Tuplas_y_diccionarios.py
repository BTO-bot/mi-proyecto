
ventas = [
    {"fecha": "2025-05-01", "producto": "Camiseta", "cantidad": 5, "precio": 20.99},
    {"fecha": "2025-05-01", "producto": "Pantalón", "cantidad": 2, "precio": 30.00},
    {"fecha": "2025-05-02", "producto": "Camiseta", "cantidad": 3, "precio": 13.59},
    {"fecha": "2025-05-02", "producto": "Zapatos", "cantidad": 1, "precio": 47.99},
    {"fecha": "2025-05-03", "producto": "Pantalón", "cantidad": 4, "precio": 25.99},
    {"fecha": "2025-05-03", "producto": "Camiseta", "cantidad": 2, "precio": 15.00},
    {"fecha": "2025-05-03", "producto": "Sombrero", "cantidad": 3, "precio": 9.99}
]

#--------------------------------------------------------------------------------------------------------


ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print(f"\nIngresos totales: ${ingresos_totales}")


#--------------------------------------------------------------------------------------------------------


ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += venta["cantidad"]
    else:
        ventas_por_producto[producto] = venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

print(f"\nProducto mas vendido: {producto_mas_vendido}")


#--------------------------------------------------------------------------------------------------------


precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    if producto in precios_por_producto:
        precios_por_producto[producto][0] += cantidad * precio
        precios_por_producto[producto][1] += cantidad
    else:
        precios_por_producto[producto] = [cantidad * precio, cantidad]

precio_promedio = {producto: round(total[0]/total[1], 2) for producto, total in precios_por_producto.items()}

print("\nPrecio Promedio por producto:")
for producto, precio in precio_promedio.items():
    print(f"- {producto}: ${precio}")


#--------------------------------------------------------------------------------------------------------


ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print("\nIngresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${ingreso:.2f}")


#--------------------------------------------------------------------------------------------------------

resumen_ventas = {}
for producto in ventas_por_producto:
    resumen_ventas[producto] = {
        "cantidad_total": ventas_por_producto[producto],
        "ingresos_totales": precios_por_producto[producto][0],
        "precio_promedio": precios_por_producto[producto][0]/precios_por_producto[producto][1]
    }

print("\nResumen de Ventas por Producto")
for producto, datos in resumen_ventas.items():
    print(f"\nProducto: {producto}")
    print(f" - Cantidad total: {datos['cantidad_total']}")
    print(f" - Ingresos totales: ${datos['ingresos_totales']:.2f}")
    print(f" - Precio promedio: ${datos['precio_promedio']:.2f}")