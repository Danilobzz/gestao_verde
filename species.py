import math


class Especie:
    def __init__(self, nome, tipo_folhagem, fruto, tipo_planta, raio_max, idade_mean):

        if not nome or not isinstance(nome, str):
            raise ValueError('O nome da espécie nao pode ser vazio. ')

        if tipo_folhagem not in ['persistente', 'caduca', 'semicaduca']:
            raise ValueError(' o tipo de folhagem tem que ser: persistente, caduca ou semicaduca. ')

        if raio_max <= 0 or not isinstance(raio_max, (int, float)):
            raise ValueError("O raio deve ser um valor decimal positivo. ")

        if idade_mean <= 0 or not isinstance(idade_mean, int):
            raise ValueError("A idade tem que ser um valor positivo inteiro.")

        self.nome = nome
        self.__tipo_folhagem = tipo_folhagem
        self.__fruto = fruto
        self.__tipo_planta = tipo_planta
        self.__raio_max = raio_max
        self.__idade_mean = idade_mean

    @property
    def obter_nome(self):
        return self.nome

    def obter_folhagem(self):
        return self.__tipo_folhagem

    def obter_fruto(self):
        return self.__fruto

    def obter_tipo(self):
        return self.__tipo_planta

    def obter_raio_max(self):
        return self.__raio_max

    def obter_idade_mean(self):
        return self.__idade_mean

    def obter_area_ocupada(self):
        return round(math.pi * (self.__raio_max ** 2))

    def __str__(self):
        return f'Especie(nome={self.nome}, folhagem={self.__tipo_folhagem}, produz fruto={self.__fruto}, ' \
               f'tipo={self.__tipo_planta}, raio={self.__raio_max}, idade media ={self.__idade_mean}'

    def __eq__(self, other):
        if not isinstance(other, Especie):
            return False
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)


# Testes T1
if __name__ == "__main__":
    especie1 = Especie("Carvalho", "caduca", True, "árvore", 5.0, 50)
    especie2 = Especie("Pinheiro", "persistente", False, "árvore", 3.0, 80)

    if especie1 == especie2:
        print(" As espécies são iguais. ")
    else:
        print(" As espécies são diferentes. ")

    print(especie1)
    print(especie2)

    print(especie1.obter_area_ocupada())
