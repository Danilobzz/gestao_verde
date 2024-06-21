from t4 import Especie
from t2 import Planta
from t3 import Park


if __name__ == "__main__":
    parque = Park("Parque Exemplo", 1000)

    especie1 = Especie("Carvalho", "caduca", True, "árvore", 5.0, 50)
    planta1 = Planta(especie1, (40.7128, -74.0060), 1990)

    especie2 = Especie("Pinheiro", "persistente", False, "árvore", 3.0, 80)
    planta2 = Planta(especie2, (40.7128, -74.0055), 1995)

    parque.adicionar_planta(planta1)
    parque.adicionar_planta(planta2)

    # print( parque.mostrar_plantas_por_ano_plantacao())
    # print("Espécies no parque:", parque.especies_no_parque())
    # print("plantas por especie: ", parque.mostrar_plantas_por_especie())
    # print("Área total ocupada:", parque.area_total_ocupada(), "metros quadrados")
    # print("Área disponível:", parque.area_disponivel(), "metros quadrados")
    # print("Idade média das plantas: ", parque.idade_media_das_plantas(), "anos")
    # print("Número de espécies diferentes:", parque.numero_especies_diferentes())
    # print("Espécies no parque:", parque.especies_no_parque())
    # print(parque.planta_em_localizacao((40.7128, -74.0055)))  # ha plana na localizacao x?
    # print(parque.espaco_para_planta(planta1))  # espaco para planta x
    # print(parque.plantas_com_idade_superior_a_media(2023))  # idade superior a media
    # print("plantas por especie: ", parque.mostrar_plantas_por_especie())

    print(parque.menu())
