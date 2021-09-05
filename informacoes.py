# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Seja bem-vindo ao PyCharm!")

print ("Aprendendo como utilizar comentarios")
print ("segunda linha")
print("terceira linha")

# declarar variavel usar o python console,popis no terminal nao mostrará o resultado

a = 10
b = 20
a + b

#declarar variavel, qdo colocamos print usar terminal
texto = "todo texto é uma string"
print(texto)

#descobrir qual e o tipo da variavel , rodar no python console

type(texto)
type(a)
type(1.4)

#contatenar valores-dados/colocar a virgula como ex abaixo
#variavel

num_int=5
num_dec=7.3
val_str="qualquer valor"

print("O valor é:",num_int)

#converter variavel, numero inteiro
print("O valor é: %i" %num_int)

#converter variavel interia para string, somar
print("O valor é: " + str(num_int))

#concatenando decimal
print("Contatenando decimal:", num_dec)

#decimal com numeros
print("Concatendo decimal: %f" %num_dec)

#decimal com a qtdade q deseja
print("Concatendo decimal: %.10f" %num_dec)

#não é possivel converter texto p numero, neste caso tem q converter para string
print("Concatendo decimal: " + str(num_dec))

#concatendo string
print("Concatendo strings" , val_str)
print("Concatendo strings %s" % val_str)
print("Concatendo strings " + val_str)

#Operações matemáticas

print(10-10)
print(10+10)
print(10/6)
print(10//6)
print(10+(50+510))

#qdo colocado // o resultado sera sem numeros decimais
#para saber o tipo da variavel
type(10/6)
type(10//6)


#Tomada de decisão, condicao IF , ELSE , ELIF

a=10
if(a==10):
    print("O valor de a é igual a 10")



#atribuição multipla

x,y,z = 2,4,8
x,y,z = x*2, x+y+z, x*y*z

#atribuicao composta operacao
x=9
y=3

x+=y
x-=y
x*=y
x/=y
x%=y

#atribuicao condicional - se x for igual a 10 ira imprimir SIM, senao irá imprimir não

x=10
texto= "sim" if x==10 else "nao"
texto

x=9
texto= "sim" if x==10 else "nao"
texto

#atribuicao condicional - se x for igual a 10 ira imprimir SIM, senao irá imprimir não

x=10
texto= "sim" if x==10 else "nao"
texto

#Laços de repeticao - looping - laços condicionais - iteração
x=0
while(x<=10): #enquanto q X for menor igual a 10 faça
    print(x) #imprima
    x+=1 #acrescentar uma unidade a x toda vez q passar nessa linha, irá imprimir 11 linhas na tela

#no caso abaixo se a instrucao nao for verdadeira imprimir else
x=0
print("while")
while(x<=10):
    print(x)
    x=x+1;
else:
    print("else")
print("fim")

#função range - inicio,fim,intervalo
list(range(0,10,2)) #ira imprimir numeros de 0 a 10 com interlalo de 2 numero (inicio, fim e intervalo)
[0, 2, 4, 6, 8]

list(range(10))#imprimi fim
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(1,15))#imprimi inicio e fim
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

list(range(100,0,-3)) #imprimi de 100 a 0 num intervalor de 3 numeros(subtração)
[100, 97, 94, 91, 88, 85, 82, 79, 76, 73, 70, 67, 64, 61, 58, 55, 52, 49, 46, 43, 40, 37, 34, 31, 28, 25, 22, 19, 16, 13, 10, 7, 4, 1]


#funcao for e a funcao range()
for i in range(-10,0,1):
    print(i)


#setimo usando a instrução BREAK
print("Antes de entrar no laço")
for item in range(10):
    print(item)
    if(item==6): #ira imprimir numero de 0 a 6
        print("A condiçção estabelecida retornou true")
        break
print("Depois de ter entrado no laço")


#funcao continue

print()
print("Inicio")
i=0
while(i<10):
    i += 1
    if(i%2==0):
        continue
    print(i)
else:
    print("else")
print("fim")
print() #imprimi linha em branco

#Estrutura de dados LISTA

lista=[1,2,5,8,15] #nome da variavel lista
lista #imprimi a lista

lista[0] #ira imprimir o valor q contem no campo 0, lembrando q sempre começamos a contar do numero 0
#o resultado será 1

lista[2] #o resultado sera 5

lista[1]+lista[2]# para somar o valor contido na lista, o resultado sera 7

lista=['a',3] #na lista posso ter uma variavel inteira e string
lista

lista=[['a','b','c'],[5,8,2],[]] #pode conter uma lista dentro da lista [[]]
lista

#dicionario é considerado sempre que estiver entre chaves {}

tel = {}
tel = {}
tel = {
    998835555: "Mel",
    999581341: "Cleber",
    956249645: "Heloisa"
    }
print(tel)

del(tel[998835589]) #para deletar
print(tel)

tel.keys() #irá imprimir a lista de chaves

tel.values() #ira imprimir a lista de valores

tel.get(numero da chave) #ira retornar o valor que esta associado a chave informada

tel.popitem() #remove o ultimo valor do dicionario

998835589 in tel #este valor esta contido dentro da variavel tel (true ou falso)

tel2={99999999: "teste1", 555555555: "teste2"}
tel.update(tel2) #todos os valores da variavel tel2 add a variavel tel

#setimo programa Função com parametros

def soma (x,y):
    total=x+y
    print("O total da soma de x+y é: ", total)
soma(10,50)
