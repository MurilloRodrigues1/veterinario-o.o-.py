Lista_presenca = {}
# Unico Def Necessário
def menu():
    import time
    import os
    while True:
        print("-----------------------------")
        print("Cadastrar um Cachorro [1]")
        print("Cadastrar um Gato [2]")
        print("Visualizar os animais cadastrados [3]")
        print("Sair [4]")
        print("-----------------------------")
        lugar = int(input("-> "))
        os.system("pause")
        os.system("cls")

        if lugar == 1:
            print("Bem-vindo à área de cadastro do seu cachorro.")
            print("Aqui você pode colocar as informações do seu cachorro.")

            # Classe do cachorro iniciada
            class Cachorro:
                def __init__(self, nome, raca, idade, dono):
                    self.nome = nome
                    self.raca = raca
                    self.idade = idade
                    self.dono = dono
                
                def exibir(self):
                    print(f"Cachorro: {self.nome}\nRaça: {self.raca} \nIdade: {self.idade}\nDono: {self.dono}")

            # Colocar informação dos animais
            nome = input("Coloque o nome do cachorro aqui -> ")
            raca = input("Coloque a raça do seu cachorro -> ")
            idade = int(input("Coloque a idade do seu cachorro -> "))
            dono = input("Coloque o seu nome completo aqui -> ")
            os.system('pause')
            os.system('cls')
            
            cachorro = Cachorro(nome, raca, idade, dono)
            Lista_presenca[dono] = cachorro

        elif lugar == 2:
            print("Bem-vindo à área de cadastro do seu gato.")
            print("Aqui você pode colocar as informações do seu gato.")

            # Classe do gato iniciada
            class Gato:
                def __init__(self, nome, raca, idade, dono):
                    self.nome = nome
                    self.raca = raca
                    self.idade = idade
                    self.dono = dono
                
                def exibir(self):
                    print(f"Gato: {self.nome} \nRaça: {self.raca} \nIdade: {self.idade} \nDono: {self.dono}")

            # Colocar informação dos animais
            nome = input("Coloque o nome do gato aqui -> ")
            raca = input("Coloque a raça do seu gato -> ")
            idade = int(input("Coloque a idade do seu gato -> "))
            dono = input("Coloque o seu nome completo aqui -> ")
            
            gato = Gato(nome, raca, idade, dono)
            Lista_presenca[dono] = gato

        elif lugar == 4:
            print("Saindo do sistema...")
            time.sleep(1.5)
            break

        elif lugar == 3:
            print("Aqui você pode ver os animais cadastrados em seu nome")
            for dono, animal in Lista_presenca.items():
                animal.exibir()

        else:
            print("Opção inválida. Tente novamente.")

menu()



    

