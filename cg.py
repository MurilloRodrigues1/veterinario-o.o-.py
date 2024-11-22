class Cachorro:
    def __init__(self, nome):
        self.nome = nome


    def comer(self):
        print(f"{self.nome} está comendo...")

    def dormir(self):
        print(f"{self.nome} está dormindo...")

nome_cachorro = input("COLOQUE O NOME DO SEU CACHORRO -> ")
cachorro = Cachorro(nome_cachorro)
cachorro.comer()
cachorro.dormir()

#--------------------------------------------------------------------I

class Gato:
    def __init__(self, nome):
        self.nome = nome

    def miar(self):
        print(f"{self.nome} está miando...")

    def brincar(self):
        print(f"{self.nome} está brincando...")

nome_gato = input("COLOQUE O NOME DO SEU GATO -> ")
gato = Gato(nome_gato)

gato.miar()
gato.brincar()




        