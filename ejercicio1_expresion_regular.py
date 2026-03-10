# Solución del ejercicio 1: Expresiones regulares

import re

# Definición de la expresión regular para buscar patrones
# Ejemplo de patrón: buscar palabras que comienzan con una letra mayúscula
patron = r'\b[A-Z][a-z]*\b'

# Texto de ejemplo
texto = "Este es un Texto de Ejemplo. Aquí hay algunas Palabras que comienzan con Mayúscula."

# Buscar todas las coincidencias en el texto
coincidencias = re.findall(patron, texto)

# Imprimir los resultados
print('Palabras que comienzan con mayúscula:')
for palabra in coincidencias:
    print(palabra)