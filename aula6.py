#programa q diz se o numero é par ou impar

#sexto Programa que pede ao usuario digitar um numero , o programa ira responder se aquele numero é impar ou par
#a expressao abaixo esta dizendo que todo numero q for divisivel por 2 sera par senao sera impar
# se o resto da divisao de num1 por 2 for igual a zero, entao deve receber a palavra par senao
# deve receber a palavra impar

num1 = int(input("Digite um número: "))
numero="par" if num1 %2 == 0 else "impar"
print("O número digitado é ",numero)

