import pygame

pygame.mixer.init()

pygame.mixer.music.load('bolt.mp3')

pygame.mixer.music.play()
input()
pygame.event.wait()