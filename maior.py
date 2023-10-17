# Exercício Python 13: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

print("Descubra qual o maior número entre 3 números")
num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
num3 = float(input("Digite o 3° número: "))

if (num1 > num2 and num1 > num3):
    print(f"O número {num1} é o maior entre os 3.")
    if num2 < num3:
        print(f"O número {num2} é o menor número entre os 3")
    else:
        print(f"O número {num3} é o menor número entre os 3")
elif (num2 > num1 and num2 > num3):
    print(f"O número {num2} é o maior entre os 3.")
    if num1 < num3:
        print(f"O número {num1} é o menor número entre os 3")
    else:
        print(f"O número {num3} é o menor número entre os 3")
elif (num3 > num1 and num3 > num2):
    print(f"O número {num3} é o maior entre os 3.")
    if num1 < num2:
        print(f"O número {num1} é o número entre os 3")
    else:
        print(f"O número {num2} é o número entre os 3")