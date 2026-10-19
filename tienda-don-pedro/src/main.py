from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

total_productos = 0
valor_inventario = 0

for linea in lineas[2:]:
    print("-", linea)
    

    partes = linea.split(",") 
    
    if len(partes) >= 3:
        precio = int(partes[1].strip())
        cantidad = int(partes[2].strip())
        
        total_productos += cantidad  
        valor_inventario += (precio * cantidad)

print()
print(f"Total de productos: {total_productos}")
print(f"Valor del inventario: ${valor_inventario}")
