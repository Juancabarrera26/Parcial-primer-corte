# Ejercicio 2: Validar el ID

def validar_id(id):
    if not isinstance(id, int) or id < 0:
        return False
    id_str = str(id)
    if 5 <= len(id_str) <= 10:
        return True
    return False

# Ejemplo de uso
if __name__ == '__main__':
    id_test = 12345
    print(f'ID {id_test} valido: {validar_id(id_test)}')
