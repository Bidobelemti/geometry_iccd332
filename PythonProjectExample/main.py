import argparse
from utils import *
def main(figura):
    print("=====Programa Geometría=====")
    print("=Autor: Bryan Morales=")

    perimetro = 0
    area = 0
        
    if figura=="cuadrado":
        lado = input("Ingrese el valor del lado: ")
        lado = float(lado)
        perimetro = perimetro_cuadrilatero(lado1=lado,
                                           lado2=lado,
                                           lado3=lado,
                                           lado4=lado)
        area = area_cuadrilatero(lado1=lado, lado2=lado)
        
    elif figura=="circulo":
        radio = int(input('Ingrese el valor del radio: '))
        perimetro = perimetro_circulo(radio=radio)
        area = area_circulo(radio)
    elif figura == 'triangulo':
        lado1=int(input('Ingrese el valor del primer lado: '))
        lado2=int(input('Ingrese el valor del segundo lado: '))
        lado3=int(input('Ingrese el valor del tercer lado: '))
        perimetro = perimetro_triangulo(lado1,lado2,lado3)
        area = area_triangulo(lado1,lado2,lado3)
        
    else:
        print("Ingrese una figura geometrica escribiendo  python main.py --fig <nombre de la figura>")

    print_resultado(nombre_figura=figura,
                    perimetro=perimetro,
                    area=area)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Figuras Geometricas")
    print('FIGURAS\ncuadrado\ncirculo\ntriangulo')
    figure = input('ingrese una figura: ')
    parser.add_argument("--fig", default=figure, help="Se declara la figura geométrica sobre la que se realiza operaciones e.g.cuadrado, circulo, rectangulo")
    args = parser.parse_args()
    main(figura=args.fig)
