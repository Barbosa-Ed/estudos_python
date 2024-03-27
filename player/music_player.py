import os

import pygame

pygame.init()
print('desafio 21: ')
print('tocar MP3')

pasta = './audios' #aqui você pode substituir pelo diretório de qualquer pasta desejada
arquivos = os.listdir(pasta)
print(f'Os arquivos em {pasta} são: \n', '\033[33m', *arquivos, '\033[m', sep = '\n', end = '\n\n')#mostra o nome das faixas de áudio destacadas
resposta = input('tocar audio? (s ou n)')
while resposta == 's':
    nome = input('digite o nome do audio: ')
    nome = '-'.join(nome.split()) #garante que o usuário possa digitar o nome do áudio utilizando apenas espaços
    pygame.mixer.music.load(f'audios\{nome}.mp3')
    input("aperte ENTER para tocar.") #pede confirmação do usuário
    pygame.mixer.music.play()
    #input()
    print('toma')
    pygame.event.wait()
    resposta = input('tocar audio de novo? (s ou n)')

print('bye!')