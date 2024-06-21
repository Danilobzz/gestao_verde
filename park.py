from t2 import Planta
from t4 import Especie
import matplotlib.pyplot as plt


class Park:
    def __init__(self, nome_parque, area):
        if not nome_parque or not isinstance(nome_parque, str):
            raise ValueError("O nome do parque deve ser uma string nao vazia. ")

        if area <= 0 or not isinstance(area, (int, float)):
            raise ValueError("A area deve ser um valor decimal positivo. ")

        self.nome_parque = nome_parque
        self.area = area
        self.lst_plantas = []

    def adicionar_planta(self, planta):
        if not isinstance(planta, Planta):
            raise ValueError("A planta deve ser valida em Planta. ")

        if self.planta_em_localizacao(planta.obter_localizacao()):
            raise ValueError("Localizacao ja esta ocupada. ")

        if not self.espaco_para_planta(planta):
            raise ValueError("Nao ha espaco para a planta neste parque. ")

        self.lst_plantas.append(planta)

    def apagar_planta(self, localizacao):
        planta_para_apagar = None
        for planta in self.lst_plantas:
            if planta.obter_localizacao() == localizacao:
                planta_para_apagar = planta
                break

        if planta_para_apagar:
            self.lst_plantas.remove(planta_para_apagar)
        else:
            raise ValueError("Não existe planta na localizão fornecida. ")

    def planta_em_localizacao(self, localizacao):
        for planta in self.lst_plantas:
            if planta.obter_localizacao() == localizacao:
                return True
        return False

    def area_total_ocupada(self):
        return sum(planta.obter_area_ocupada() for planta in self.lst_plantas)

    def area_disponivel(self):
        return self.area - self.area_total_ocupada()

    def espaco_para_planta(self, planta):
        return self.area_disponivel() >= planta.obter_area_ocupada()

    def idade_media_das_plantas(self):
        total_idade = sum(planta.obter_idade(2023) for planta in self.lst_plantas)
        return total_idade / len(self.lst_plantas) if len(self.lst_plantas) > 0 else 0

    def numero_especies_diferentes(self):
        especies_unicas = set(self.lst_plantas)
        total_diferentes = len(especies_unicas)
        return total_diferentes

    def especies_no_parque(self):
        especies = set()
        for planta in self.lst_plantas:
            especies.add(planta.especie.obter_nome)
        return list(especies)

    def mostrar_plantas_por_especie(self):
        sorted_plantas = sorted(self.lst_plantas, key=lambda planta: planta.especie.obter_nome)
        for planta in sorted_plantas:
            print(planta.especie.obter_nome)

    def mostrar_plantas_por_ano_plantacao(self):
        sorted_plantas = sorted(self.lst_plantas, key=lambda planta: planta.obter_ano_plantacao)
        for planta in sorted_plantas:
            print("Nome: ", planta.especie.obter_nome, "idade: ", planta.obter_idade(2023))

    def plantas_com_idade_superior_a_media(self, ano_atual):
        idade_media = self.idade_media_das_plantas()
        return [planta.especie.obter_nome for planta in self.lst_plantas if
                planta.obter_idade(ano_atual) >= idade_media]

    def guardar_para_ficheiro(self, nome_ficheiro):
        with open(nome_ficheiro, 'w') as f:
            f.write(f'{self.nome_parque}, {self.area}\n')
            for planta in self.lst_plantas:
                f.write(f'{planta.especie.obter_nome}, {planta.localizacao}, {planta.ano_plantacao}\n')
        print('-' * 50)
        print('Parque guardado. ')
        print('-' * 50)

    def menu(self):
        while True:

            print('1. Adicionar planta. ')
            print('2. Remover planta. ')
            print('3. Listar plantas existentes no parque. ')
            print('4. Mostrar área ocupada. ')
            print('5. Mostrar a área disponível para plantação. ')
            print('6. Estatísticas e informações. ')
            print('7. Guardar o parque no ficheiro. ')
            print('8. Sair. ')
            x = input('Oque deseja? ')

            if x == '1':
                print('-' * 50)
                self.adicionar_planta_menu()
                print('-' * 50)
            if x == '2':
                print('-' * 50)
                self.remover_planta_menu()
                print('-' * 50)
            if x == '3':
                print('-' * 50)
                print("Plantas no parque: ")
                print(self.mostrar_plantas_por_especie())
                print('-' * 50)
            if x == '4':
                print('-' * 50)
                print("Está ocupado ", self.area_total_ocupada(), " metros quadrados")
                print('-' * 50)
            if x == '5':
                print('-' * 50)
                print("Está disponível ", self.area_disponivel(), " metros quadrados")
                print('-' * 50)
            if x == '6':
                print('-' * 50)
                while True:
                    print("\nEstatísticas e Informações:")
                    print("1. Mostrar a média de idades das plantas do parque")
                    print("2. Mostrar o número de espécies diferentes")
                    print("3. Listar as espécies existentes no parque")
                    print("4. Listar todas as plantas organizadas por espécie")
                    print("5. Listar todas as plantas organizadas por ano de plantação")
                    print("6. Listar as plantas que excederam o tempo médio de vida da sua espécie")
                    print("7. Histograma por idade")
                    print("8. Histograma por espécie")
                    print("9. Voltar ao menu anterior")
                    print('-' * 50)

                    opcao = int(input("Escolha uma opção (1-9): "))

                    if opcao == 1:
                        print('-' * 50)
                        print("A média das idades é: ", self.idade_media_das_plantas(), "anos. ")
                        print('-' * 50)
                    elif opcao == 2:
                        print('-' * 50)
                        print("Existem", self.numero_especies_diferentes(), "espécies diferentes no parque. ")
                        print('-' * 50)
                    elif opcao == 3:
                        print('-' * 50)
                        print('Lista das espécies: ')
                        print(self.especies_no_parque())
                        print('-' * 50)
                    elif opcao == 4:
                        print('-' * 50)
                        print('Lista das plantas por espécie: ')
                        print(self.mostrar_plantas_por_especie())
                        print('-' * 50)
                    elif opcao == 5:
                        print('-' * 50)
                        print('Lista das plantas por ano de plantação: ')
                        print(self.mostrar_plantas_por_ano_plantacao())
                        print('-' * 50)
                    elif opcao == 6:
                        print('-' * 50)
                        print('Plantas com idade superior a média: ')
                        print(self.plantas_com_idade_superior_a_media(2023))
                        print('-' * 50)
                    elif opcao == 7:
                        print('-' * 50)
                        self.histograma_idades()
                        print('-' * 50)
                    elif opcao == 8:
                        print('-' * 50)
                        self.histograma_especies()
                        print('-' * 50)
                    elif opcao == 9:
                        print('-' * 50)
                        break
                    else:
                        print('Opção inválida')

            if x == '7':
                print('-' * 50)
                self.guardar_para_ficheiro('parque_dados.txt')
                print('-' * 50)
            if x == '8':
                print('-' * 50)
                break

    def adicionar_planta_menu(self):
        print('\nAdicionar Planta: ')
        try:
            nome_especie = input('Insira o nome da espécie -')
            tipo_folhagem = input('Insira o tipo de folhagem[caduca, persistente, semicaduca] -')
            fruto = input('produz fruto?[True/False] -')
            tipo_planta = input('Qual o tipo? [árvore/arbusto] -')
            raio_max = float(input('Qual o seu raio máximo? -'))
            idade_mean = int(input('Qual é a média da idade? -'))

            especie = Especie(nome_especie, tipo_folhagem, fruto, tipo_planta, raio_max, idade_mean)

            latitude = float(input('Insira a latitude da localizacao: '))
            longitude = float(input('Insira a longitude da localizacao: '))
            localizacao = (latitude, longitude)

            ano_plantacao = int(input('Insira o ano de plantacao da planta: '))

            planta = Planta(especie, localizacao, ano_plantacao)

            self.adicionar_planta(planta)
            print('Planta adicionada. ')
        except ValueError as e:
            print(f'erro ao adicionar a planta {e}')

    def remover_planta_menu(self):
        print('\nRemover planta: ')
        try:
            latitude = float(input('Insira a latitude da localizcao: '))
            longitude = float(input('Insira a longitude da localizacao: '))
            localizcao = (latitude, longitude)

            planta_remover = None
            for planta in self.lst_plantas:
                if planta.obter_localizacao() == localizcao:
                    planta_remover = planta
                    break

            if planta_remover:
                self.lst_plantas.remove(planta_remover)
                print('Planta removida. ')
            else:
                print('Planta não encontrada. ')
        except ValueError as e:
            print(f'Erro a remover a planta {e}')

    def histograma_idades(self):
        idades = [planta.obter_idade(2023) for planta in self.lst_plantas]
        plt.hist(idades, bins=20, color='blue', edgecolor='black')
        plt.title('histograma por idade')
        plt.xlabel('idade')
        plt.ylabel('Numero plantas ')
        plt.show()

    def histograma_especies(self):
        especies = [planta.especie.obter_nome for planta in self.lst_plantas]
        plt.hist(especies, bins=20, color='blue', edgecolor='black')
        plt.title('histograma por especies')
        plt.xlabel('especies')
        plt.ylabel('Numero de plantas ')
        plt.xticks(rotation=45, ha='right')
        plt.show()

# testes estão no 'tester.py'
