#Terceiro Programa: Se digitar 1 sim se digitar 2 nao e se digitar qualquer outro numero o sistema informa q nao foi digitado 1 nem 2

acao = int(input("Digite '1' para sim e '2' para não: "))
if(acao==1):
    print("Você disse sim!")
else:
    if(acao==2):
        print("Você disse não!")
    else:
        print("O número digitado não é '1' e nem ' 2'!!!")