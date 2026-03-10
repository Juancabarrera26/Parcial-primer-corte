def afd_ajedrez(movimiento):
    
    estado = 0
    tokens = movimiento.split()
    
    # Si el movimiento es simple (ej: p->k4), nos aseguramos de separar el '->'
    if "->" in movimiento and " " not in movimiento:
        tokens = movimiento.replace("->", " -> ").split()

    for t in tokens:
        if estado == 0:
            if all(c in 'pkqrbn' for c in t):
                estado = 1
            else: return "RECHAZADO"

        elif estado == 1:
            # Validar el tipo de movimiento o captura
            if t == "->" or t == "X":
                estado = 2
            else: return "RECHAZADO"

        elif estado == 2:
            if t[-2] in 'abcdefgh' and t[-1] in '12345678':
                estado = 3 # Llegamos al estado final
            else: return "RECHAZADO"

    return "ACEPTADO" if estado == 3 else "RECHAZADO"
    
print(f"p->k4: {afd_ajedrez('p->k4')}")      # Caso movimiento simple
print(f"kbp X qn: {afd_ajedrez('kbp X qn')}") # Caso captura con varias piezas
print(f"z1 -> a1: {afd_ajedrez('z1 -> a1')}") # Caso error 
