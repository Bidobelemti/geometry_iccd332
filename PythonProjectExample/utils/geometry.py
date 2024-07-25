import math

def perimetro_cuadrilatero(lado1:float,
                           lado2:float,
                           lado3:float,
                           lado4:float):
    return lado1+lado2+lado3+lado4

def area_cuadrilatero(lado1:float, lado2:float):
    return lado1*lado2

def perimetro_circulo(radio):
    return 2*math.pi*radio

def area_circulo(radio):
    return math.pi*radio**2

def perimetro_triangulo(lado1,lado2,lado3):
    return lado1+lado2+lado3

def area_triangulo(a,b,c):
    s = (a + b + c) / 2
    
    # Calcular el área usando la fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

def print_resultado(nombre_figura, perimetro, area):
    print(f"el perimetro de {nombre_figura} es {perimetro:.2f}")
    print(f"el area de {nombre_figura} es {area:.2f}")
