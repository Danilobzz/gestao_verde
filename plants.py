import math
from t1 import Especie


class Planta:
    def __init__(self, especie, localizacao, ano_plantacao):
        if not isinstance(especie, Especie):
            raise ValueError("A planta deve ter uma Espécie válida. ")

        if not isinstance(localizacao, tuple) or len(localizacao) != 2 \
                or not all(isinstance(coord, (int, float))for coord in localizacao):
            raise ValueError("A localizacao deve ser uma tupla de dois valores decimais.")

        if not isinstance(ano_plantacao, int) or ano_plantacao <= 0:
            raise ValueError("O ano de plantacao deve ser inteiro e positivo. ")

        self.especie = especie
        self.localizacao = localizacao
        self.ano_plantacao = ano_plantacao

    @property
    def obter_especie(self):
        return self.especie

    @property
    def obter_ano_plantacao(self):
        return self.ano_plantacao

    def obter_localizacao(self):
        return self.localizacao

    def obter_area_ocupada(self):
        return self.especie.obter_area_ocupada()

    def obter_idade(self, ano_atual):
        return ano_atual - self.ano_plantacao

    def verificar_localizacao(self, localizacao_verificar):
        distancia = math.sqrt((self.localizacao[0] - localizacao_verificar[0])**2 +
                              (self.localizacao[1] - localizacao_verificar[1])**2)
        return distancia <= self.especie.obter_raio_max()

    def __str__(self):
        return f'Planta(especie={str(self.especie)}, localização={self.localizacao}, ano Plantação={self.ano_plantacao}'


# testes T2
if __name__ == "__main__":
    especie1 = Especie("Carvalho", "caduca", True, "árvore", 5.0, 50)
    planta1 = Planta(especie1, (40.7128, -74.0060), 1990)

    print(planta1)
    print(planta1.obter_area_ocupada(), 'metros quadrados. ')
    print(planta1.obter_idade(2023))

    localizacao_ver = (40.7128, -74.0055)
    if planta1.verificar_localizacao(localizacao_ver):
        print('Já esta ocupado')
    else:
        print('nao pertence a area ocupada pela planta. ')
