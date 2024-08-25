entrada = int(input("\nDigite sua idade em dias \n"))
anos = int(0)
meses = int(0)
dias = int(0)

while entrada > 0:  
    if entrada > 365:
        entrada = entrada - 365
        anos = anos + 1
    elif entrada > 30:
        entrada = entrada - 30
        meses = meses + 1
    else:
        dias = entrada
        entrada = 0
       

print("Você tem \n{0} ano(s) \n{1} meses(s) \n{2} dia(s)".format(anos,meses,dias))
       
