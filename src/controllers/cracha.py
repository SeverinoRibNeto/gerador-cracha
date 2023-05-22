import os
import threading
from typing import List
from models.estudante import Estudante
from models.cracha import Cracha
from views.gui import GUI
from PIL import Image
from pubsub import pub
import csv
import subprocess
import wx
import wx.xrc


class ProcessaCrachaThreading(threading.Thread):
    def __init__(self,):
        pass


class CrachaController:
    cabecalho_csv = ['matricula', 'nome', 'fator_rh',
                     'curso', 'data_nascimento', 'sus_numero']
    exemplo_dados = [111, "Nome Teste", "A+", "Curso",
                     "01/01/2001", 123456789]
    formato_imagens = [".jpg", ".jpeg", ".png"]
    app = wx.App()
    gui = GUI(None)
    error_message = wx.MessageDialog(gui,
                                     'Mensagem Erro',
                                     style=wx.OK | wx.CENTRE,
                                     pos=wx.DefaultPosition)

    def __init__(self):
        self.gui.contador_lbl.Hide()

        if (not os.path.exists('config.txt')):
            # Cria arquivo vazio com a configuração do programa
            self.criar_arquivo_config('', '', '')

        # cria comunicação com a view
        pub.subscribe(self.salvar, "SALVAR_SOLICITADO")
        pub.subscribe(self.carregar, "CARREGAR_SOLICITADO")
        pub.subscribe(self.gerar, "GERAR_SOLICITADO")
        pub.subscribe(self.__criar_csv_exemplo, "DOWNLOAD_SOLICITADO")

    def __criar_csv_exemplo(self):
        # cria o arquivo csv exemplo e abre com o notepad
        with open('template.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(self.cabecalho_csv)
            writer.writerow(self.exemplo_dados)
        try:
            subprocess.run(['notepad.exe', 'template.csv'])
        except FileNotFoundError:
            print("Editor de texto não encontrado")

    def salvar(self, caminho_info: str,
               caminho_imagens: str, pasta_saida: str) -> bool:
        self.criar_arquivo_config(caminho_info, caminho_imagens, pasta_saida)
        return True

    def carregar(self) -> None:
        try:
            config = self.retorna_variaveis_config()
            if config:
                self.gui.m_filePicker2.SetPath(config[1])
                self.gui.m_dirPicker1.SetPath(config[0])
                self.gui.m_dirPicker2.SetPath(config[2])
            return
        except Exception as e:
            self.error_message.SetMessage(
                'Error ao carregar as configurações'+'\n'+str(e))
            self.error_message.ShowModal()
            return

    def gerar(self, caminho_info, caminho_imagens, pasta_saida):
        # Separar informações do csv para lista e fazer contagem total -ok
        # criar estudante com as informações do csv- ok
        # Criar lista de arquivos em caminh_imagens- ok
        # verificar se existe foto do estudante na lista de imagens
        # criar o cracha e preencher as informações
        # salvar na pasta de saidas
        # adicionar ao contador -ok
        if not pasta_saida:
            self.error_message.SetMessage(
                "É necessário informar a pasta para saida!")
            self.error_message.ShowModal()
            return
        lista_imagens = self.lista_imagens(caminho_imagens)
        estudantes = self.cria_lista_estudantes_info(caminho_info)
        texto = f"Gerando ... (1 de {len(estudantes)})"
        self.gui.contador_lbl.Show()
        for contador in range(len(estudantes)):
            imagem_estudante = self.verifica_estudante_imagens(
                estudantes[contador],
                lista_imagens)
            if imagem_estudante:
                imagem = Image.open(imagem_estudante)
                cracha = Cracha(estudantes[contador], imagem_estudante=imagem,
                                caminho_salvar=pasta_saida)
            else:
                cracha = Cracha(estudantes[contador],
                                caminho_salvar=pasta_saida)
            cracha.gerar_cracha()
            cracha = ''
            self.gui.contador_lbl.SetLabel(
                texto.replace("(1", "("+str(contador+1)))

    def cria_lista_estudantes_info(self, caminho_csv: str) -> List[Estudante]:
        try:
            with open(caminho_csv, 'r') as file:
                lista_estudantes = list(csv.reader(file, delimiter=','))
            return self.transf_lista_estudante(lista_estudantes)
        except Exception as e:
            self.error_message.SetMessage(
                'Error ao carregar as Informações'+'\n'+str(e))
            self.error_message.ShowModal()
            return []

    def transf_lista_estudante(self,
                               lista_e: List[Estudante]) -> List[Estudante]:
        # Recebe uma lista de estudantes e transforma em estudantes(Objeto)
        return [Estudante(estudante[0],
                          estudante[1],
                          estudante[2],
                          estudante[3],
                          estudante[4],
                          estudante[5])
                for estudante in lista_e
                if estudante[0] not in self.cabecalho_csv]

    def lista_imagens(self, imagens_dir: str) -> List[str]:
        # Percorre o diretório e imagens_dir, percore os arquivos,
        # filtrando eles pelo formato desejado. Os formatos aceitos
        # são '.jpeg', '.jpg' e '.png'
        return [os.path.join(diretorio, arquivo)
                for diretorio, subpastas, arquivos in os.walk(imagens_dir)
                for arquivo in arquivos
                if any(formato in arquivo for formato in self.formato_imagens)]

    def verifica_estudante_imagens(self, estudante: Estudante,
                                   lista_imagens: List[str]) -> str:
        # Procura imagens com o numero do sus do estudante, caso encontre,
        # retorna a primera imagem encontrada, caso contrario, retorna ''
        imagens = [imagem for imagem in lista_imagens
                   if estudante.sus_numero in imagem]

        if len(imagens):
            return imagens[0]
        return ''

    def criar_arquivo_config(self, caminho_info: str,
                             caminho_imagens: str, pasta_saida: str) -> bool:
        # Salva as configurações em um arquivo txt de nome config.txt
        try:
            with open('config.txt', "w") as f:
                f.write(f'caminho_imagens={caminho_imagens}')
                f.write(';')
                f.write(f'caminho_info={caminho_info}')
                f.write(';')
                f.write(f'pasta_saida={pasta_saida}')
                return True
        except Exception as e:
            print(e)
            return False

    def retorna_variaveis_config(self) -> List[str]:
        try:
            with open('config.txt', 'r') as f:
                config_crua = f.readline()
        except Exception as e:
            raise e
        # Separa as informações que estão com ';' e cria a lista para as
        # config_crua
        config_lista = [config for config in config_crua.split(";")]
        # Faz o retorno de c que é o slipt de config, item da lista
        # config_crua Valores sem o '\\' são descartados
        return [c for config in config_lista
                for c in config.split('=') if '\\' in c]

    def run(self):
        self.gui.Show()
        self.app.MainLoop()


if __name__ == '__main__':
    cracha = CrachaController()
    cracha.run()
