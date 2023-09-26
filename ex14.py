peso_peixes = float(input("Digite o peso dos peixes em quilos: "))

limite = 50

if peso_peixes > limite:
    excesso = peso_peixes - limite
    multa = excesso * 4.00
else:
    excesso = 0
    multa = 0

if excesso > 0:
    print(f"Peso de peixes excedeu o limite em {excesso:.2f} quilos.")
    print(f"Valor da multa a ser pago: R$ {multa:.2f}")
else:
    print("Peso de peixes dentro do limite. Nenhuma multa é devida.")
