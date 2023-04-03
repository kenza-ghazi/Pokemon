import pygame

from dialogue import DialogBox
from map import MapManager
from players import Player
class Game:
    def __init__(self):
      self.screen = pygame.display.set_mode((660,630))
      pygame.display.set_caption("Toad")
      self.player = Player()
      self.dialog_box = DialogBox()
      sel.map_manager = MapManager(self.screen ,self.player, self.dialog_box)