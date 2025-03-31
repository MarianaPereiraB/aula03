nota01 =  float(input("digite a primeira nota"))
nota02 = float(input("digite a segunda nota"))
nota03 = float(input("digite a terceira nota"))

media_aluno= (nota01+nota02+nota03) /3
if media_aluno >= 7:
    print("aprovado")
else:
    print("reprovado")