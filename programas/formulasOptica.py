import math

#primer formula
def ley_snell(n1, theta1, n2):
    # Convertir los ángulos a radianes
    theta1_rad = math.radians(theta1)
    
    # Calcular el ángulo de refracción en radianes usando la ley de Snell
    sin_theta2 = (n1 / n2) * math.sin(theta1_rad)
    
    # Calcular el ángulo de refracción en grados
    theta2_rad = math.asin(sin_theta2)
    theta2 = math.degrees(theta2_rad)
    
    return theta2

# Solicitar al usuario que ingrese los valores
n1 = float(input("Ingresa el índice de refracción del primer medio (n1): "))
theta1 = float(input("Ingresa el ángulo de incidencia en grados (θ1): "))
n2 = float(input("Ingresa el índice de refracción del segundo medio (n2): "))

# Calcular el ángulo de refracción usando la función ley_snell
theta2 = ley_snell(n1, theta1, n2)
print(f"El ángulo de refracción es: {theta2} grados")

#segunda formula y sus subformulas
def calcular_luz_transmitida():
    I0 = float(input("Introduce la intensidad de la luz incidente (I0): "))
    R = float(input("Introduce el coeficiente de reflexión (R): "))
    It = I0 * (1 - R)
    print("La intensidad de la luz transmitida (It) es:", It)
    return It

calcular_luz_transmitida()

#subformula 1
def calcular_luz_incidente():
    It = float(input("Introduce la intensidad de la luz transmitida (It): "))
    R = float(input("Introduce el coeficiente de reflexión (R): "))
    I0 = It / (1 - R)
    print("La intensidad de la luz incidente (I0) es:", I0)
    return I0

calcular_luz_incidente()

#subformula 2

def calcular_coeficiente_reflexion():
    I0 = float(input("Introduce la intensidad de la luz incidente (I0): "))
    It = float(input("Introduce la intensidad de la luz transmitida (It): "))
    R = 1 - (It / I0)
    print("El coeficiente de reflexión (R) es:", R)
    return R

calcular_coeficiente_reflexion()

#subformula 3

def calcular_luz_incidente():
    It = float(input("Introduce la intensidad de la luz transmitida (It): "))
    R = float(input("Introduce el coeficiente de reflexión (R): "))
    I0 = It / (1 - R)
    print("La intensidad de la luz incidente (I0) es:", I0)
    return I0

calcular_luz_incidente()

#tercer formula y sus subformulas
def calcular_distancia_focal():
    do = float(input("Introduce la distancia del objeto (do): "))
    di = float(input("Introduce la distancia de la imagen (di): "))
    f = (do * di) / (do + di)
    print("La distancia focal (f) es:", f)
    return f

calcular_distancia_focal()

#subformula 1
def calcular_distancia_objeto():
    f = float(input("Introduce la distancia focal (f): "))
    di = float(input("Introduce la distancia de la imagen (di): "))
    do = (f * di) / (f - di)
    print("La distancia del objeto (do) es:", do)
    return do

calcular_distancia_objeto()

#subformula 2
def calcular_distancia_imagen():
    f = float(input("Introduce la distancia focal (f): "))
    do = float(input("Introduce la distancia del objeto (do): "))
    di = (f * do) / (f + do)
    print("La distancia de la imagen (di) es:", di)
    return di

calcular_distancia_imagen()

#subformual 3
def calcular_distancia_imagen():
    f = float(input("Introduce la distancia focal (f): "))
    do = float(input("Introduce la distancia del objeto (do): "))
    di = (f * do) / (f + do)
    print("La distancia de la imagen (di) es:", di)
    return di

calcular_distancia_imagen()

#cuarta formula y sus subformulas
def calcular_angulo_brewster():
    n1 = float(input("Introduce el índice de refracción del primer medio (n1): "))
    n2 = float(input("Introduce el índice de refracción del segundo medio (n2): "))
    theta_B = n2 / n1
    print("El ángulo de Brewster (theta_B) es:", math.degrees(theta_B), "grados")
    return theta_B

calcular_angulo_brewster()

#subformula 1
def calcular_indice_refraccion_1():
    theta_B = float(input("Introduce el ángulo de Brewster (theta_B) en grados: "))
    n2 = float(input("Introduce el índice de refracción del segundo medio (n2): "))
    n1 = n2 / math.tan(theta_B * math.pi / 180)
    print("El índice de refracción del primer medio (n1) es:", n1)
    return n1

calcular_indice_refraccion_1()

#subformula 2
def calcular_indice_refraccion_2():
    theta_B = float(input("Introduce el ángulo de Brewster (theta_B) en grados: "))
    n1 = float(input("Introduce el índice de refracción del primer medio (n1): "))
    n2 = n1 * math.tan(theta_B * math.pi / 180)
    print("El índice de refracción del segundo medio (n2) es:", n2)
    return n2

calcular_indice_refraccion_2()

#formula 5
def calcular_angulo_difraccion():
    lam = float(input("Introduce la longitud de onda (lambda): "))
    Q = float(input("Introduce el orden de difracción (Q): "))
    theta = (lam / Q) ** 0.5
    print("El ángulo de difracción (theta) es:", theta)
    return theta

calcular_angulo_difraccion()

#subformula 1
def calcular_longitud_onda():
    theta = float(input("Introduce el ángulo de difracción (theta) en grados: "))
    Q = float(input("Introduce el orden de difracción (Q): "))
    lam = Q * math.sin(theta * math.pi / 180)
    print("La longitud de onda (lambda) es:", lam)
    return lam

calcular_longitud_onda()

#subformula 2
def calcular_orden_difraccion():
    theta = float(input("Introduce el ángulo de difracción (theta) en grados: "))
    lam = float(input("Introduce la longitud de onda (lambda): "))
    Q = lam / (theta * math.pi / 180)
    print("El orden de difracción (Q) es:", Q)
    return Q

calcular_orden_difraccion()