"""

    Laboratório 1

    Escrever um programa que solicite ao usuário:
    => O nome de um funcionário;
    => Seu salário.

    Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10%.
    No final, apresentar:
    => O nome do funcionário;
    => O salário bruto;
    => O valor do desconto;
    => O salário líquido.

"""


# nome = input("Digite seu nome: ")
# salario = salarioLiquido = float(input("Digite o Seu Salário: "))

# desconto = 0

# if(salario > 5000): desconto = salario * 0.1

# salarioLiquido -= desconto
   
# print(f'Nome: {nome}')
# print(f'Salario: {salario}')
# print(f'Valor Desconto: {desconto}')
# print(f'Salario Liquido: {salarioLiquido}')



"""

    Laboratório 1

    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:

    => Até 17 anos - R$ 50,00;
    => Entre 18 e 59 anos - R$ 60,00;
    =. A partir de 60 anos - R$ 20,00.

    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.

"""

nome = input("Nome do Associado: ")
idade = int(input("Idade do Associado: "))

if idade < 18:  valor = 50
elif idade < 60: valor = 60
else: valor = 20

print("\n===== Valores pagos =====")
print(f"Nome do Associado : {nome}")
print(f"Idade : {idade} anos")
print(f"valor do ingresso : $ {valor}")
