time1 = input("insira o primeiro nome de time:")
time2 = input("insira  o segundo nome de time:")
gols1 = input(f"insira o número de gols do primeiro time: ")
gols2 = input(f" insira o número de gols do segundo time: ")

if gols1 > gols2:
    print(f"campeão é o {time1}")
else:
    if gols2 > gols1:
     print(f"campeão é o {time2}")
    else:
        print("empate")


