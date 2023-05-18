from estudante import Estudante
from PIL import Image, ImageDraw, ImageFont
import qrcode


class Cracha:

    imagem_padrao = Image.open("src/res/sem_imagem.jpeg")

    def __init__(self, estudante: Estudante, modelo: Image,
                 imagem_estudante: Image = imagem_padrao) -> None:

        self.estudante = estudante
        self.imagem_estudante = imagem_estudante
        self.modelo = modelo

    def gerarCracha(self):
        self._criar_texto_estudante('nome', 300, 1870)
        self._criar_texto_estudante('fator_rh', 280, 2100)
        self._criar_texto_estudante('curso', 700, 2320)
        self._criar_texto_estudante('data_nascimento', 700, 2580)
        self._criar_texto_vertical('SUS:', 150, 30)
        self._criar_texto_vertical_estudante('sus_numero', 350, 30)
        self._organiza_imagem_estudante(538, 626)
        self._organiza_imagem_qr(153, 2260)
        pass

    def _criar_texto_estudante(self, attrib, pos_x, pos_y):
        draw = ImageDraw.Draw(self.modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        texto = getattr(self.estudante, attrib)
        draw.text((pos_x, pos_y), texto, font=font_name, fill='black')

    def _criar_texto_vertical_estudante(self, attrib, pos_x, pos_y):
        self.modelo = self.modelo.rotate(-90, expand=1)
        draw = ImageDraw.Draw(self.modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        texto = getattr(self.estudante, attrib)
        draw.text((pos_x, pos_y), texto, font=font_name,
                  fill='black')
        self.modelo = self.modelo.rotate(90, expand=1)

    def _criar_texto_vertical(self, texto, pos_x, pos_y):
        self.modelo = self.modelo.rotate(-90, expand=1)
        draw = ImageDraw.Draw(self.modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        draw.text((pos_x, pos_y), texto, font=font_name,
                  fill='black')
        self.modelo = self.modelo.rotate(90, expand=1)

    def _organiza_imagem_estudante(self, pos_x, pos_y):
        self.imagem_estudante = self.imagem_estudante.resize((840, 1120))
        self.modelo.paste(self.imagem_estudante, (pos_x, pos_y))

    def _organiza_imagem_qr(self, pos_x, pos_y):
        qr_code = self._codigo_qr()
        qr_code = qr_code.resize((417, 422))
        self.modelo.paste(qr_code, (pos_x, pos_y))

    def _codigo_qr(self):
        codigo_qr = qrcode.QRCode()
        codigo_qr.add_data(self.estudante.matricula)
        codigo_qr.make(fit=True)
        return codigo_qr.make_image(fill="black", back_color=(211, 211, 211))

    def run(self) -> None:
        self.gerarCracha()
        self.modelo.save("teste.png")
        pass
