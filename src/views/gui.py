# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from pubsub import pub

###########################################################################
# Class principalFrame
###########################################################################


class GUI (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gerador de Crachás", pos=wx.DefaultPosition, size=wx.Size(
            714, 484), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"Gerador de Crachás", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(wx.Font(
            16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer1.Add(self.m_staticText2, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticline1 = wx.StaticLine(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer1.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_staticText3 = wx.StaticText(
            self, wx.ID_ANY, u"Selecione a lista com as informações", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        wSizer1.Add(self.m_staticText3, 0, wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        wSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_filePicker2 = wx.FilePickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.csv", wx.DefaultPosition, wx.Size(450, -1), wx.FLP_DEFAULT_STYLE)
        wSizer1.Add(self.m_filePicker2, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(
            self, wx.ID_ANY, u"Selecione a pasta das imagens", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        wSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        wSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_dirPicker1 = wx.DirPickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size(450, -1), wx.DIRP_DEFAULT_STYLE)
        wSizer1.Add(self.m_dirPicker1, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(
            self, wx.ID_ANY, u"Selecione a pasta de saida", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        wSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        wSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_dirPicker2 = wx.DirPickerCtrl(
            self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size(450, -1), wx.DIRP_DEFAULT_STYLE)
        wSizer1.Add(self.m_dirPicker2, 0, wx.ALL, 5)

        bSizer1.Add(wSizer1, 1, wx.EXPAND, 5)

        gSizer1 = wx.GridSizer(0, 4, 0, 0)

        self.m_button1 = wx.Button(
            self, wx.ID_ANY, u"Salvar Config", wx.DefaultPosition, wx.Size(150, 50), 0)
        gSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(
            self, wx.ID_ANY, u"Carregar Config", wx.DefaultPosition, wx.Size(150, 50), 0)
        gSizer1.Add(self.m_button2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button3 = wx.Button(
            self, wx.ID_ANY, u"Gerar Crachas", wx.DefaultPosition, wx.Size(150, 50), 0)
        gSizer1.Add(self.m_button3, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_button4 = wx.Button(
            self, wx.ID_ANY, u"Download Template", wx.DefaultPosition, wx.Size(150, 50), 0)
        gSizer1.Add(self.m_button4, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        bSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"Instruções"), wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, u"Para gerar os crachás, escolha uma lista CSV com as informações dos estudantes; Template disponível em \"Download Template\"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        sbSizer3.Add(self.m_staticText6, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, u"Em seguida, escolha a pasta com as imagens dos estudantes, todas numeradas de acordo com o número do SUS;", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        sbSizer3.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, u"Por fim, escolha a pasta em que quer que os arquivos sejam salvos;", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        sbSizer3.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, u"Feito por: @severino_neto", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        self.m_staticText9.SetFont(wx.Font(
            8, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        sbSizer3.Add(self.m_staticText9, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_staticText10 = wx.StaticText(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, u"Github: https://github.com/SeverinoRibNeto", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        self.m_staticText10.SetFont(wx.Font(
            8, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        sbSizer3.Add(self.m_staticText10, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer1.Add(sbSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.salvar)
        self.m_button2.Bind(wx.EVT_BUTTON, self.carregar)
        self.m_button3.Bind(wx.EVT_BUTTON, self.gerar)
        self.m_button4.Bind(wx.EVT_BUTTON, self.download)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def salvar(self, event):
        self.m_filePicker2.GetPath()
        # Envia as informações de pastas para salvar em arquivo txt.
        pub.sendMessage("SALVAR_SOLICITADO",
                        caminho_info=self.m_filePicker2.GetPath(),
                        caminho_imagens=self.m_dirPicker1.GetPath(),
                        pasta_saida=self.m_dirPicker2.GetPath())
        event.Skip()

    def carregar(self, event):
        pub.sendMessage("CARREGAR_SOLICITADO")
        event.Skip()

    def gerar(self, event):
        pub.sendMessage("GERAR_SOLICITADO",
                        caminho_info=self.m_filePicker2.GetPath(),
                        caminho_imagens=self.m_dirPicker1.GetPath(),
                        pasta_saida=self.m_dirPicker2.GetPath())
        event.Skip()

    def download(self, event):
        pub.sendMessage("DOWNLOAD_SOLICITADO")
        event.Skip()
