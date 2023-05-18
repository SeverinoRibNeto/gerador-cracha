from .estudante import Estudante
from PIL import Image, ImageDraw, ImageFont
import qrcode


class Cracha:

    imagem_padrao = Image.open("src/res/sem_imagem.jpeg")
    modelo_padrao = Image.open("src/res/modelo.png")

    def __init__(self, estudante: Estudante, modelo: Image = modelo_padrao,
                 imagem_estudante: Image = imagem_padrao,
                 caminho_salvar: str = 'saida/') -> None:
        # Função para inicializar a classe.
        # Necessário um estudante e modelo, já disponível;
        # Caminho_salvar é o caminho padrão para salvar as imagens
        self.estudante = estudante
        self.imagem_estudante = imagem_estudante
        self.modelo = modelo
        self.caminho_salvar = caminho_salvar

    def gerarCracha(self) -> None:
        # Cria as informações de texto, imagem e código qr
        self._criar_texto_estudante('nome', 300, 1870)
        self._criar_texto_estudante('fator_rh', 280, 2100)
        self._criar_texto_estudante('curso', 700, 2320)
        self._criar_texto_estudante('data_nascimento', 700, 2580)
        self._criar_texto_vertical('SUS:', 150, 30)
        self._criar_texto_vertical_estudante('sus_numero', 350, 30)
        self._organiza_imagem_estudante(538, 626)
        self._organiza_imagem_qr(153, 2260)
        return

    def _criar_texto_estudante(self, attrib: str,
                               pos_x: int, pos_y: int) -> None:
        # Escreve as informações da classe estudante;
        # Necessário passar o atributo por texto, como 'nome'
        draw = ImageDraw.Draw(self.modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        texto = getattr(self.estudante, attrib)
        draw.text((pos_x, pos_y), texto, font=font_name, fill='black')

    def _criar_texto_vertical_estudante(self, attrib: str,
                                        pos_x: int, pos_y: int) -> None:
        # Vira a imagem em -90 graus para escrever informações do estudante;
        # Dessa forma, as informações ficam de forma vertical
        self.modelo = self.modelo.rotate(-90, expand=1)
        draw = ImageDraw.Draw(self.modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        texto = getattr(self.estudante, attrib)
        draw.text((pos_x, pos_y), texto, font=font_name,
                  fill='black')
        self.modelo = self.modelo.rotate(90, expand=1)

    def _criar_texto_vertical(self, texto: str,
                              pos_x: int, pos_y: int) -> None:
        # Cria um texto na forma vertical, sem a necessidade de
        # atributos. Somente texto
        self.modelo = self.modelo.rotate(-90, expand=1)
        draw = ImageDraw.Draw(self.modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        draw.text((pos_x, pos_y), texto, font=font_name,
                  fill='black')
        self.modelo = self.modelo.rotate(90, expand=1)

    def _organiza_imagem_estudante(self, pos_x: int, pos_y: int) -> None:
        # Redefine tamanho da imagem e coloca no cracha, chamado de modelo
        self.imagem_estudante = self.imagem_estudante.resize((840, 1120))
        self.modelo.paste(self.imagem_estudante, (pos_x, pos_y))

    def _organiza_imagem_qr(self, pos_x: int, pos_y: int) -> None:
        # Pega o codigo qr criado na função codigo_qr, modifica o tamanho e
        # coloca no crachá chamado de modelo
        qr_code = self._codigo_qr()
        qr_code = qr_code.resize((417, 422))
        self.modelo.paste(qr_code, (pos_x, pos_y))

    def _codigo_qr(self) -> Image:
        # Cria o código qr com auxilio da classe qrcode
        codigo_qr = qrcode.QRCode()
        codigo_qr.add_data(self.estudante.matricula)
        codigo_qr.make(fit=True)
        return codigo_qr.make_image(fill="black", back_color=(211, 211, 211))

    def run(self) -> None:
        # Metodo para gerar um cracha de acordo com as informações passadas;
        # Necessário informar o ca
        self.gerarCracha()
        self.modelo.save(self.caminho_salvar+"teste.png")
        pass
