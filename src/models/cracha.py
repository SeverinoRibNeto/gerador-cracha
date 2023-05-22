from .estudante import Estudante
from PIL import Image, ImageDraw, ImageFont
import qrcode


class Cracha:

    imagem_padrao = Image.open("src/res/sem_imagem.jpeg")
    modelo = Image.open("src/res/modelo.png")

    def __init__(self, estudante: Estudante,
                 imagem_estudante: Image = imagem_padrao,
                 caminho_salvar: str = 'saida/') -> None:
        # Função para inicializar a classe.
        # Necessário um estudante e modelo, já disponível;
        # Caminho_salvar é o caminho padrão para salvar as imagens
        self.estudante = estudante
        self.imagem_estudante = imagem_estudante
        self.caminho_salvar = caminho_salvar

    def gerar_cracha(self) -> None:
        modelo = self.modelo.copy()
        # Cria as informações de texto, imagem e código qr
        self.__criar_texto_estudante(modelo, 'nome', 300, 1870)
        self.__criar_texto_estudante(modelo, 'fator_rh', 280, 2100)
        self.__criar_texto_estudante(modelo, 'curso', 700, 2320)
        self.__criar_texto_estudante(modelo, 'data_nascimento', 700, 2580)
        modelo = self.__criar_texto_vertical(modelo, 'SUS:', 150, 30)
        modelo = self.__criar_texto_vertical_estudante(
            modelo, 'sus_numero', 350, 30)
        self.__organiza_imagem_estudante(modelo, 538, 626)
        self.__organiza_imagem_qr(modelo, 153, 2260)
        modelo.save(f"{self.caminho_salvar}\\{self.estudante.matricula}.png")

    def __criar_texto_estudante(self, modelo: Image, attrib: str,
                                pos_x: int, pos_y: int) -> None:
        # Escreve as informações da classe estudante;
        # Necessário passar o atributo por texto, como 'nome'
        draw = ImageDraw.Draw(modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        texto = getattr(self.estudante, attrib)
        draw.text((pos_x, pos_y), texto, font=font_name, fill='black')

    def __criar_texto_vertical_estudante(self, modelo: Image, attrib: str,
                                         pos_x: int, pos_y: int) -> Image:
        # Vira a imagem em -90 graus para escrever informações do estudante;
        # Dessa forma, as informações ficam de forma vertical
        modelo = modelo.rotate(-90, expand=1)
        draw = ImageDraw.Draw(modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        texto = getattr(self.estudante, attrib)
        draw.text((pos_x, pos_y), texto, font=font_name,
                  fill='black')
        modelo = modelo.rotate(90, expand=1)
        return modelo

    def __criar_texto_vertical(self, modelo: Image, texto: str,
                               pos_x: int, pos_y: int) -> Image:
        # Cria um texto na forma vertical, sem a necessidade de
        # atributos. Somente texto
        modelo = modelo.rotate(-90, expand=1)
        draw = ImageDraw.Draw(modelo)
        font_name = ImageFont.truetype("arial.ttf", 80)
        draw.text((pos_x, pos_y), texto, font=font_name,
                  fill='black')
        modelo = modelo.rotate(90, expand=1)
        return modelo

    def __organiza_imagem_estudante(self,
                                    modelo: Image,
                                    pos_x: int,
                                    pos_y: int) -> None:
        # Redefine tamanho da imagem e coloca no cracha, chamado de modelo
        self.imagem_estudante = self.imagem_estudante.resize((840, 1120))
        modelo.paste(self.imagem_estudante, (pos_x, pos_y))

    def __organiza_imagem_qr(self, modelo: Image,
                             pos_x: int, pos_y: int) -> None:
        # Pega o codigo qr criado na função codigo_qr, modifica o tamanho e
        # coloca no crachá chamado de modelo
        qr_code = self.__codigo_qr()
        qr_code = qr_code.resize((417, 422))
        modelo.paste(qr_code, (pos_x, pos_y))

    def __codigo_qr(self) -> Image:
        # Cria o código qr com auxilio da classe qrcode
        codigo_qr = qrcode.QRCode()
        codigo_qr.add_data(self.estudante.matricula)
        codigo_qr.make(fit=True)
        return codigo_qr.make_image(fill="black", back_color=(211, 211, 211))
