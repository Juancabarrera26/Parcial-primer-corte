# Ejercicio 2: Validación de ID

def validar_id(id):
    """
    Esta función valida si un ID cumple con las siguientes condiciones:
    - Debe ser un entero positivo.
    - Debe tener entre 5 y 10 dígitos.
    """
    if not isinstance(id, int) or id < 0:
        return False
    id_str = str(id)
    if 5 <= len(id_str) <= 10:
        return True
    return False

# Ejemplo de uso
if __name__ == '__main__':
    id_test = 12345
    print(f'ID {id_test} válido: {validar_id(id_test)}')