from aula10.code import *

c = Cadastro()
c.add(Cliente("Ana Maria", 25))
c.add(Cliente("Pedro Silva", 21))
c.add(Cliente("Amanda Soares", 28))

c.print()
c.salvar("teste.txt")
