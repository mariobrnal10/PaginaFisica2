def calcular_luz_transmitida():
    I0 = float(input("Introduce la intensidad de la luz incidente (I0): "))
    R = float(input("Introduce el coeficiente de reflexión (R): "))
    It = I0 * (1 - R)
    print("La intensidad de la luz transmitida (It) es:", It)
    return It

calcular_luz_transmitida()