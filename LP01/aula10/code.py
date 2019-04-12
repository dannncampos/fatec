import numpy as np

class Cliente:
    codigo = 0

    def __init__(self, nome, idade, id=0):
        ###  inicializa os atributos ###
        if id <= 0:
            Cliente.codigo = Cliente.codigo + 1
            self.id = Cliente.codigo
        else:
            # atualiza o código
            if id >= Cliente.codigo:
                Cliente.codigo = id
            self.id = id
        self.nome = nome
        self.idade = idade

    def toString(self):
        ### retorna o valor dos atributos no formato de texto ###
        return self.nome + ";" + str(self.idade) + ";" + str(self.id)

    def toArray(self):
        ### retorna o valor dos atributos no formato de texto ###
        return [self.nome,str(self.idade),str(self.id)]


class Cadastro:
    lista = []

    def add(self, cliente):
        ### adiciona um objeto do tipo Cliente na lista ###
        self.lista.append(cliente)

    def print(self):
        ### imprime na tela os elementos da lista ###
        for item in self.lista:
            print(item.toString())

    def salvar(self,caminho):
        ### salva no arquivo os elementos da lista ###
        # carrega num array de 2 dimensões
        temp = []
        for item in self.lista:
            temp.append(item.toArray())
        #temp = np.array(temp) # converte para array Numpy
        # escreve no arquivo
        np.savetxt(caminho, temp, delimiter=';', newline='\n', encoding='utf-8', fmt='%s')

    def ler(self,caminho):
        ### ler o conteúdo do arquivo e carrega na lista ###
        dados = np.loadtxt(caminho, delimiter=';', dtype=np.str, encoding='utf-8')
        for linha in dados:
            if linha.size == 3:
                # cada linha é formada por: nome idade id
                nome = linha[0]
                idade = int(linha[1])
                id = int(linha[2])
                # adiciona na lista
                self.lista.append(Cliente(nome, idade, id))
