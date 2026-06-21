from code.background import Background
from code.const import W_WIDTH, W_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory: #factor nao tem init
    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range (5):
                    list_bg.append(Background(f'level1bg{i}', position))
                    list_bg.append(Background(f'level1bg{i}', (W_WIDTH,0)))
                return list_bg
            case 'player':
                return Player('player', (0,290))
            case 'enemy1':
                return Enemy('enemy1', (position[0], position[1]))
            case 'enemy2':
                return Enemy('enemy2', (position[0], position[1]))
