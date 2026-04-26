class Cão:
    def __init__(self, nome):
        self.nome = nome

    def urinar(self):
        print(f'{self.nome} está a urinar...')

nikita = Cão('Nikita')
print(nikita.nome)
nikita.urinar()

bobby = Cão('bobby')
print(bobby.nome)
bobby.urinar()
