class ArquivoAudio:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        if not arquivo.endswith(self.ext):
            raise Exception("Formato inválido!")

class ArquivoMP3(ArquivoAudio):
    ext = "mp3"
    def tocar(self):
        print('Tocando {} como MP3'.format(self.arquivo))

class ArquivoWav(ArquivoAudio):
    ext = "wav"
    def tocar(self):
        print('Tocando {} como WAV'.format(self.arquivo))


class ArquivoOgg(ArquivoAudio):
    ext = "ogg"
    def tocar(self):
        print('Tocando {} como OGG'.format(self.arquivo))

ogg = ArquivoOgg("musica.ogg")
mp3 = ArquivoMP3("musica.mp3")
wav = ArquivoWav("musica.wav")

ogg.tocar()
mp3.tocar()
wav.tocar()

#teste_ogg = ArquivoMP3("outramusica.ogg")