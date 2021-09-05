#Primeiro programa: login e senha

login = input("Login: ")
senha = input("Senha: ")

print("O usuario informado foi: %s, e a senha digitada foi: %s" %(login,senha))

#Segundo programa:calculo

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

divisao = num1 / num2
resto = num1 % num2
print()
print(num1, "divido por", num2, "é igual a: ", divisao)
print("O resto da divisão entre", num1, "e" , num2, "é igual a: ", resto)