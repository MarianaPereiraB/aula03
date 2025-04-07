tipo = input(" digite G para gasolina ou digite E para etanol: ")
litros = float(input("quantos litros você quer abastecer? "))

gasolina = 5.80 * litros
etanol = 4.90 * litros


if tipo == "G" or tipo == "g":
    print(f"{gasolina} é o valor a ser pago da gasolina")
elif tipo == "E" or tipo == "e":
        print(f"{etanol} é o valor a ser pago")
else:
    print("letra inválida")