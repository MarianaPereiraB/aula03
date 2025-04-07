tipo = input(" digite G para gasolina: "
             "digite E para etanol:")
litros = float(input("quantos litros você quer abastecer?"))

gasolina = 5.80
etanol = 4.90

if gasolina == "G":
    print(f"{gasolina*litros:.2f} é o valor a ser pago")

else:
    if etanol == "E":
        print(f"{etanol*litros:.2f} é o valor a ser pago")