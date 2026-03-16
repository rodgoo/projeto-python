import pygame
pygame.init()
pygame.mixer.music.load('audio-para-py-teste.mp3')

input('Pressione ENTER para iniciar a música')
pygame.mixer.music.play()

input('Press ENTER para parar a música')
pygame.event.wait()