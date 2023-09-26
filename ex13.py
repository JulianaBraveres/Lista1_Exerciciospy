altura = float(input("Digite a altura: "))

sexo = input("Digite o sexo: (M para masculino, F para feminino): ")

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    genero = "masculino"
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    genero = "feminino"
else:
    print("Não reconhecido. Digite M para masculino ou F para feminino.")
    exit()

print(f"O peso ideal para uma pessoa do sexo {genero} com altura {altura} é de {peso_ideal:.2f} kg")
