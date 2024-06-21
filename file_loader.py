from t1 import Especie


def carregar_ficheiro(nome_do_ficheiro):
    especies = []

    with open(nome_do_ficheiro, 'r') as ficheiro:
        linhas = ficheiro.readlines()

        for linha in linhas:
            # Dividir a linha em campos usando a vírgula como delimitador
            campos = linha.strip().split(',')

            nome, tipo_folhagem, fruto, tipo_planta, raio_max, idade_mean = (
                campos[0],
                campos[1],
                campos[2].lower() == 'True',
                campos[3],
                float(campos[4]),
                int(campos[5])
            )

            especie = Especie(nome, tipo_folhagem, fruto, tipo_planta, raio_max, idade_mean)

            especies.append(especie)

    return especies


# Exemplo de utilização

if __name__ == "__main__":
    arquivo_especies = "ficheiro_especies.txt"
    lista_especies = carregar_ficheiro(arquivo_especies)

    # Imprima detalhes de cada espécie na lista
    for especie in lista_especies:
        print(especie)
        print(f"Área ocupada: {especie.obter_area_ocupada()}m²")
        print("------")
