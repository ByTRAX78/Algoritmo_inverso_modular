def inverso_modular(a, m):
    """ Calcula el inverso modular de a módulo m usando el Algoritmo Extendido de Euclides """
    m0, x0, x1 = m, 0, 1
    
    if m == 1:
        return None  # No existe el inverso modular si m es 1

    while a > 1:
        # q es el cociente
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    # Asegurar que x1 sea positivo
    if x1 < 0:
        x1 += m0

    return x1

# Solicitar al usuario los valores de a y m
a = int(input("Introduce el número para calcular su inverso modular: "))
m = int(input("Introduce el módulo (campo finito): "))

resultado = inverso_modular(a, m)

if resultado:
    print(f"El inverso modular de {a} mod {m} es: {resultado}")
else:
    print(f"No existe inverso modular de {a} mod {m}")
