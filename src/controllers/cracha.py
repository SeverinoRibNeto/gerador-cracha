import time
import threading
from models.estudante import Estudante
from models.cracha import Cracha
from views.gui import GUI
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

    def __init__(self):
        # self.config = config
        self.app = wx.App()
        self.gui = GUI(None)

        # cria comunicação com a view
        pub.subscribe(self.salvar, "SALVAR_SOLICITADO")
        pub.subscribe(self.carregar, "CARREGAR_SOLICITADO")
        pub.subscribe(self.gerar, "GERAR_SOLICITADO")
        pub.subscribe(self._criar_csv_exemplo, "DOWNLOAD_SOLICITADO")

    def _criar_csv_exemplo(self):
        # cria o arquivo csv exemplo e abre com o notepad
        with open('template.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(self.cabecalho_csv)
        try:
            subprocess.run(['notepad.exe', 'template.csv'])
        except FileNotFoundError:
            print("Editor de texto não encontrado")

    def salvar(self, caminho_info, caminho_imagens, pasta_saida):
        pass

    def carregar(self):
        pass

    def gerar(self):
        pass

    def run(self):
        self.gui.Show()
        self.app.MainLoop()


if __name__ == '__main__':
    cracha = CrachaController()
    cracha.run()
