import gtts
from playsound import playsound
import os

with open('texto.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase.mp3')
        playsound('frase.mp3')
        