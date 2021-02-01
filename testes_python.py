z = 26
while z > 3:
    arquivo = open('library.txt', 'r', encoding ='utf-8')
    palavra = []
    for line in arquivo:
        palavra.append(line.strip())
    arquivo.close()
    input1 = input('digita a palavra, ')
    i = 0
    x = 0
    lista = list(input1)
    nao = True
    result  = []
    listaTemp = []
    while i != len(palavra):
        listpa = list(palavra[i])
        for l in lista:
            listaTemp.append(l)
        if len(lista) == len(listpa):
            while x != len(lista):
                verdadeiro = listpa[x] in listaTemp
                if verdadeiro == False:
                    nao = False
                else:
                    listaTemp.remove(listpa[x])
                x += 1
            if nao and len(listaTemp) == 0:
                result.append(palavra[i])
            nao = True
        i += 1
        x = 0
        listaTemp = []
    if len(result) == 0:
        print('nenhum resultado encontrado')
        
    print(result)
