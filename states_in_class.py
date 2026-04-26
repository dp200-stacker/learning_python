class Carro:
    def __init__(self, nome, acelerando=False):
        self.nome = nome
        self.acelerando = acelerando

    def acelerar(self):
        if self.acelerando:
            print(f'O {self.nome} já está acelerar..')
            return

        print(f'O {self.nome} está acelerar..')
        self.acelerando=True

    def acelera_trava(self):
        if not self.acelerando:
            print(f'O {self.nome} não está acelerar mais..')
            return
        
        print(f'O {self.nome} está parar de acelerar..')
        self.acelerando = False

    def travar(self):
        if self.acelerando:
            print(f'O {self.nome} não pode travar enquanto acelera..')
            return
        
        print(f'O {self.nome} já está a travar..')


c1 = Carro('BMW')
c2 = Carro('Mercedez')

c1.acelerar()
c1.acelerar()
c1.travar()
c1.acelera_trava()
c1.travar()
