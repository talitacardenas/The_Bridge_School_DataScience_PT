import argparse
parser = argparse.ArgumentParser()
# configuramos argumentos obligatorios
parser.add_argument("square", help="display a square of a given number",
                    type=int, default=5)
# configuramos argumentos opcionales, en este caso hay que llamar el argumento --constante o abreviado -k
parser.add_argument("-k", "--constante", default=2, help="display a square of a given number",
                    type=int)
args = parser.parse_args()
square = args.square
costante = args.constante
print(square**costante)
