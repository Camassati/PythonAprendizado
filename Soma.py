var1 = int(input("Digite o primeiro valor: "))
var2 = int(input("Digite o segundo valor: "))
operacao = int(input("Oque quer fazer\n Soma[1]\n Subtração[2] \nMultiplicação[3] \nDivisão[4]"))
if operacao == 1:
    print (var1+var2)
elif operacao == 2:
    print (var1-var2)
elif operacao == 3:
    print(var1*var2)
elif operacao == 4:
    print(var1/var2)
else:
    print("Numero inválido")