with open("Nomes.txt","a") as arquivo:

    texto=input("digite seu nome: ")
    arquivo.write(f'{texto}\n')


