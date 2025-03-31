nome = input("nome")
idade = int(input("idade"))
salario =float(input("seu salário"))
porcentagem = float(input("quantos % você quer aumentar seu salário?"))
salarioatual = (porcentagem*salario)/100
somaaumento = (salario+salarioatual)
print(f"o nome é {nome}\n a idade é {idade}\n e o salário antes do aumento {salario}\n  porcentagem que vai ser aumentada no salário atual{porcentagem}% \n e o salário com o aumento{somaaumento}")
#int 1 \ float 1.4
