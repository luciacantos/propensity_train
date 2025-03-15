from datetime import datetime, timedelta

def obtener_datos_usuario():
    return {
        "nombre": "Lucía Fernández",
        "nivel": "Oro",
        "puntos": 3200,
        "dinero_gastado": 1540,
        "beneficios": """
        - Descuento del 20% en todas las compras
        - Atención VIP
        - Acceso a eventos privados
        """,
        "promociones": [
            {
                "titulo": "Envío gratuito este mes",
                "descripcion": "Recibe tus pedidos sin costos adicionales.",
                "fecha_expiracion": datetime.today() + timedelta(days=10)
            },
            {
                "titulo": "Regalo sorpresa en tu siguiente pedido",
                "descripcion": "Obtén un producto especial con tu compra.",
                "fecha_expiracion": datetime.today() + timedelta(days=5)
            }
        ]
    }
