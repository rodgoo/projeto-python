import pygame
pygame.init()
pygame.mixer.music.load('audio-para-py-teste.mp3')

pygame.mixer.music.play()
input('Press Enter to stop the music...')
pygame.event.wait()