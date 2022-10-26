## EXERCICIO 1

"""
Recebe uma String e devolve uma String
Devolve a String que corresponde à cadeia de caractéres limpa (remove os caracteres brancos)

"""
def limpa_texto(cadeia):
    return " ".join(cadeia.split()) #Dá split na cadeia de caracteres e depois volta a juntar com o join deixando um " " entre cada palavra

"""
Recebe uma string e um inteiro e devolve um tuplo

O inteiro representa o número de caracteres da coluna. Devolve um tuplo onde na primeira posição
a String com as palavras completas desde o inicio da cadeia original chegar ao limite da coluna 
(inteiro fornecido) e na segunda posição a String que corresponde ao resto da String inicial

"""
def corta_texto(cadeia, value):  
    if not (type(value) == int and value>=0):
        raise ValueError("O número colocado não é um inteiro")
    if (len(cadeia) == value): #Caso o tamanaho da coluna seja igual ao comprimento do texto
        return (cadeia,"")
    value =value-1
    if (value >= len(cadeia)): #Quando o valor do value é maior do que a len da cadeia de caracteres dada
        return (cadeia,"")
    elif cadeia[value] == " ":  #Quando o valor do value calha num espaço
        return (cadeia[:value].strip(), cadeia[value+1:].strip())
    elif ( cadeia[value] != " " and cadeia[value +1] == " " ): #Quando o valor do value calha no final de uma palavra
        return (cadeia[:value +1].strip(),cadeia[value+2:].strip())
    else:                               #Quando o valor calha a meio de uma palavra
        i= value
        while (cadeia[i] != " " and i >0): # ciclo que vai ver onde começa essa palavra que iria ser cortada
            i=i-1
        return (cadeia[:i].strip(),cadeia[i:].strip()) #utilizamos o .strip() para garantir que não há espaços no inicio nem no final


"""
Recebe uma String e um inteiro e devolve uma String

Caso a String seja composta apenas por uma palavra devolve a String que tem essa palavra.
Caso a String seja composta por duas ou mais palavras, pega na String dada e adiciona espaços
até que o número de caracteres da String seja igual ao inteiro fornecido.
"""

def insere_espacos(cadeia,value):
    if (len(cadeia.split()) == 1):
        while len(cadeia) <value:
            cadeia= cadeia + " "
        return cadeia
    conta_espacos =0
    for i in cadeia:
        if i== " ":
            conta_espacos= conta_espacos +1
    while len(cadeia) < value:
        j=0
        tamanho =len(cadeia)
        while j < tamanho + conta_espacos:
            if len(cadeia) == value:
                return cadeia
            if cadeia[j] == " " and cadeia[j+1] != " ":
                cadeia = cadeia[:j] + " " + cadeia[j:]
                j=j+2
            else:
                j=j+1
    return cadeia # Se o valor do len(cadeia) for igual ao tamanho da coluna
"""
Recebe uma String não vazia e um inteiro e devolve um tuplo de cadeias de caracteres

A função gera um ValueError caso os argumentos sejam inválidos
Pega na String e devolve um tuplo, onde cada uma das entradas do tuplo são Strings de comprimento igual à
largura da coluna com espaços entre palavras até chegar ao limite de caracteres da String que é o valor
do inteiro dado
"""
   
def justifica_texto (cadeia, value):
    if (type(cadeia) != str or len(cadeia) == 0 or type(value) != int or value < 1): #valida os argumentos
        raise ValueError ('justifica_texto: argumentos invalidos')
    else:
        texto= limpa_texto(cadeia)
        res= corta_texto(texto,value)
        if (len(res[0]) == 0):
            raise ValueError('justifica_texto: argumentos invalidos')
        lista=(insere_espacos(res[0],value),)
        if len(res[1]) == 0: #Caso apenas haja uma linha e seja logo no inicio
            aux= res[0]
            while len(aux) <value:
                aux= aux + " "
            lista_caso_especial= (aux,)
            return lista_caso_especial
        while len(res[1]) != 0: # no final, quando o texto acabar o res vai ser do tipo ("......", "").Logo quando len(res[1]) for igual a 0 sabemos que o texto a justificar terminou
            res= corta_texto(res[1],value) #atualiza o res
            if (len(res[0]) == 0):
                raise ValueError('justifica_texto: argumentos invalidos')
            if len(res[1]) != 0:
                lista= lista + (insere_espacos(res[0],value),) #insere os espaços e adiciona no resultado final
            else: #caso da ultima linha 
                aux1= res[0]
                while len(aux1) <value:
                    aux1= aux1 + " "
                lista= lista + (aux1,)         
    return lista
    
#cad = "Computers are incredibly \n\tfast, \n\t\taccurate \n\t\t\tand stupid. \n Human beings are incredibly slow inaccurate, and brilliant. \n Together they are powerful beyond imagination."
#print(justifica_texto(cad, 60))
#for l in justifica_texto(cad, 60): print(l)
#print(corta_texto("Fundamentos da Programação",10))

## EXERCICIO 2

"""
Recebe um dicionário e um inteiro e devolve um dicionário

O dicionário contem os votos de cada partido. Devolve um dicionário onde para cada chave (partido) está
associado uma lista de comprimento igual ao inteiro fornecido com os quocientes calculados com o método de
Hondt ordenados por ordem decrescente. Altera o dicionário que é dado inicialmente
"""
def calcula_quocientes (dic, deputados):
    res={}
    for key in dic:
        lista=[] #lista onde vamos meter os quocientes de cada partido
        i=1 #começa a 1 porque não é preciso devidir por 0
        while i <= deputados:
             lista = lista + [dic[key] / i]
             i=i+1
        res [key] = lista #adiciona ao novo dicionário onde a chave é o nome do partido e a lista tem os valores dos quocientes
    return res

"""
Recebe um dicionário e um inteiro e devolve uma lista

O dicionário contem os votos de cada partido e o inteiro representa o número de deputados.
Vai percorrer o dicionário e consoante os quocientes do método de Hondt vai atribuir os mandatos, colocando-o
a chave do partido na lista. Na primeira posição da lista corresponde ao nome do partido que teve o primeiro
deputado e assim sucessivamente...Caso existam dois partidos com o mesmo quociente o mandato deve ser atribuído
a quem tem menos votos.
"""
def atribui_mandatos (dic,deputados):
    tabela = calcula_quocientes(dic,deputados) #vai fazer os quocientes 
    res= []
    while len(res) < deputados: #temos que eleger mandatos até ao valor de deputados que nos é dado
        max=0
        index=0
        chave=""
        for key in tabela: #percorre os valores dos quocientes todos e vai buscar o maior deles guardando o index e a chave para no final apagar da lista, para na próxima contagem não ser contabilizado
            for i in range(len(tabela[key])):
                if tabela[key][i] > max: #se for maior damos update no valor máximo, no index e na key
                    max = tabela[key][i]
                    index =i
                    chave = key
                if tabela[key][i] == max: #no caso de haver empate escolhemos aquele que teve menos votos
                    if dic[key] < dic[chave]: #vê qual deles tem menos fotos e escolhe o que tem menos
                        max= tabela[key][i]
                        index =i
                        chave = key
        res = res + [chave]
        del (tabela[chave][index]) # Elimina o valor máximo que foi colocado no res 
    return res

"""
Recebe um dicionário e devolve uma lista

Percorre o as chaves do dicionário e devolve uma lista com as chaves de cada partido
"""
def obtem_partidos (dic):
    res=[]
    for key in dic:
        for key2 in dic[key]["votos"]:
            if key2 not in res: #garante que não há repetições 
                res= res + [key2]
    return sorted(res)
"""
Recebe um dicionário e devolve um dicionário

Cria um dicionário com as chaves de cada um dos partidos e com os valores inicializados a 0
"""
# Função auxiliar que cria um dicionário com as chaves de cada um dos partidos com o valor inicial de 0
def dicionario_partidos (dic):
    dicionario ={}
    partidos= obtem_partidos(dic)
    for i in partidos:
        dicionario[i]=0
    return dicionario

#Outra função auxiliar que vai percorrer a lista incial dada e criar dois dicionários diferentes.
#Um com os deputados eleitos por cada partido e outro com o número total de votos
"""
Recebe um dicionário e devolve um tuplo de dicionários

O tuplo de dicionários na primeira posição tem um dicionário as chaves são cada um dos partidos
e o valor de cada chave é a soma dos votos de cada partido em todas as regiões.
Na segunda posição do tuplo tem um dicionário onde novamente tem como chaves o nome de cada um dos partidos
que participou e o valor de cada chave é o número de mandatos que cada partido tem direito.

"""
def lista_deputados_votos_aux(dic):
    deputados=dicionario_partidos(dic) #Vai pegar os dicionários vazios com a função anterior tanto para o número de votos como para os deputados eleitos
    votos=dicionario_partidos(dic)
    for key in dic:
        mandatos = atribui_mandatos(dic[key]["votos"], dic[key]["deputados"]) #calcula os mandatos por cada região
        for i in mandatos:
                 deputados[i]= deputados[i] +1 #Conforme aparecem vai alterando os dados do dicionário
        for key2 in dic[key]["votos"]: #ciclo que percorre o dicionário com os votos e vai alterando o dicionário dos votos inicial, para no final ter os votos totais de cada partido
             votos[key2] = votos[key2] + dic[key]["votos"][key2]
    return (deputados,votos) #devolve um tuplo onde na posição 0 tem um dicionário com os deputados eleitos de cada partido e na posição 1 um dicionário com os votos totais de cada partido

"""
Recebe um dicionário e devolve uma lista

Utiliza as outras funções auxiliares anteriores e devolve uma lista de tuplos. Cada tuplo é composto
por 3 entradas. Na primeira o nome do partido, no segundo o número de mandatos do partido e por fim
o número de votos. Os tuplos devem ser apresentados por ordem decrescente de número de mandatos. Caso
haja empate deve aparecer primeiro aquele que tem menor numero de votos.

Verifica a validade dos argumentos
"""

def obtem_resultado_eleicoes(dic):
    if (type(dic) != dict or len(dic) == 0):
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    for key in dic: 
        if ( type(dic[key]) != dict or "deputados" not in dic[key] or "votos" not in dic[key] or len(dic[key]["votos"])==0 or type(dic[key]["votos"])!= dict):
            raise ValueError('obtem_resultado_eleicoes: argumento invalido')
        for key2 in dic[key]["votos"]:
            if  ( type(dic[key]["deputados"]) != int or dic[key]["deputados"] <= 0 or type(key2) != str or key2 == "" or type(dic[key]["votos"][key2]) != int or dic[key]["votos"][key2] <=0): #confirma os argumentos
                raise ValueError ('obtem_resultado_eleicoes: argumento invalido')
    deputados= lista_deputados_votos_aux(dic)[0] #Vai buscar os dicionários da função anterior já com os dados
    votos = lista_deputados_votos_aux(dic)[1]
    vistos=[] # uma lista onde vamos adicionando os partidos que já foram colocados no resultado para não haver repetições
    res=[]
    while len(vistos) < len(obtem_partidos(dic)): #Enquanto o comprimento da lista dos partidos já colocados no resultado for menor que o comprimento dos partidos que participaram na eleição significa que ainda não foram colocados todos os partidos
        max=-1
        chave=""
        for key in deputados: #um ciclo que vai achar qual o partido que teve mais deputados para serem apresentados por ordem decrescente
            if deputados[key] > max and key not in vistos:
                max= deputados[key]
                chave=key
            if deputados[key] == max and key not in vistos: #no caso de haver um empate entre nos mandatos vamos ver o que tem maior número de votos
                if votos[key] > votos[chave]:
                    max= deputados[key]
                    chave= key        
        vistos= vistos + [chave]
        res= res +[(chave,deputados[chave],votos[chave])]
    return res

# info = {"Endor": {"deputados": 7,"votos": {"A":12000, "B":7500, "C":5250, "D":3000}},"Hoth": {"deputados": 6,"votos": {"B":11500, "A":9000, "E":5000, "D":1500}},"Tatooine": {"deputados": 3,"votos": {"A":3000, "B":1900}}}
# print(lista_deputados_votos_aux(info))

##EXERCICIO 3

"""
Recebe 2 tuplos com a mesma dimensão e devolve um real 

Faz o produto interno entre os dois tuplos com a mesma dimensão e devolve o real que resulta desse produto
"""

def produto_interno (t1,t2):
    res=0
    for i in range(len(t1)):
        res = res + t1[i]*t2[i]
    return float(res)

"""
Recebe 3 tuplos de igual dimensão e um valor real positivo e devolve um booleano

Um dos tuplos é um conjunto de tuplos onde cada tuplo representa uma linha da matriz quadrada e outros dois tuplos
um com os valores das constantes e a solução atual. O valor real é a precisão.
A função deverá retornar True caso o valor absoluto do erro de todas as equações seja inferior à
precisão, e False caso contrário
"""

def verifica_convergencia (A,c,x,e):
    for i in range(len(A)):
        if abs(produto_interno(A[i],x) - c[i]) > e:
            return False
    return True

"""
Recebe dois tuplos e devolve um tuplo

Um dos tuplos representa a matriz de entrada e o outro tuplo representa o vetor das constantes.
A função devolve a matriz sem zeros na diagonal. Para isso troca as linhas até que a matriz fique sem zeros
na diagonal. As alterações feitas na matriz também são aplicadas no vetor das constantes.

"""
def retira_zeros_diagonal (matriz, c):
    res_matriz=[]
    res_c=[]
    for i in matriz:
        res_matriz = res_matriz +[i]
    for i in c:    
        res_c= res_c + [i]
    for i in range(len(matriz)):
            if res_matriz[i][i] == 0:
                bol=False
                j=0
                while bol ==False and j< len(matriz):
                    if res_matriz[j][i] !=0 and res_matriz[i][j] !=0:
                        aux=res_matriz[i]
                        res_matriz [i] = res_matriz[j]
                        res_matriz [j] = aux
                        aux1= res_c[i]
                        res_c [i] = res_c[j]
                        res_c [j] =aux1
                        bol=True
                    j=j+1
    return (tuple(res_matriz),tuple(res_c))

"""
Recebe um tuplo e devolve um booleano

O tuplo representa uma matriz quadrada onde cada linha da matriz é um tuplo. A função devolve True caso a 
matriz seja diagonal dominante e False caso contrário

"""

def eh_diagonal_dominante (matriz):
    for i in range(len(matriz)):
        res=0
        for j in range(len(matriz[0])):
            if i != j:
                res= res + abs(matriz[i][j])
        if abs(matriz[i][i]) < res:
            return False
    return True

"""
Recebe dois tuplos um valor real e devolve um tuplo

A função recebe um tuplo que representa uma matriz quadrada e o outro tuplo representa o vetor das constantes.
O valor real representa a precosão do resultado que queremos.
A função confirma a validade dos erros e se a matriz é diagonal dominante. Caso não seja devolve um ValueError.

No final devolve um tuplo que é o resultado de aplicar o método de Jacobi.
"""

def resolve_sistema(matriz,c,e): #começamos com um valor de x =(0,0,0)
    if (type(matriz) != tuple or type(c) != tuple or len(matriz) == 0 or not isinstance(e,(int, float)) or e <= 0):
        raise ValueError('resolve_sistema: argumentos invalidos')
    for i in range(len(matriz)):
        if (type(matriz[i]) != tuple or len(matriz[i]) != len(matriz[0]) or len(matriz) != len(matriz[0]) or len(matriz[0]) != len(c)):
            raise ValueError('resolve_sistema: argumentos invalidos')
        for j in range (len(matriz[0])):
            if (not isinstance(matriz[i][j],(int, float)) or not isinstance(c[i],(int,float))):
                raise ValueError ('resolve_sistema: argumentos invalidos')
    if eh_diagonal_dominante(matriz) == False:
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    x = tuple ([0] * len(matriz[0]))
    matriz= retira_zeros_diagonal (matriz, c)[0]
    c= retira_zeros_diagonal (matriz, c)[1]
    for l in range(len(matriz)):
        if matriz[l][l] == 0:
            raise ValueError('resolve_sistema: argumentos invalidos')
    while verifica_convergencia(matriz,c, x, e) == False:
        nova_lista_x = []
        for k in range(len(matriz)): # vai atualizar o valor do resultado x
            novo_valor_x = x[k] + (c[k] - produto_interno(matriz[k],x))/matriz[k][k]
            nova_lista_x.insert(k, novo_valor_x)
        x= tuple (nova_lista_x)
    return x
