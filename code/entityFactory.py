from code.background import Background
from code.const import W_WIDTH


class EntityFactory: #factor nao tem init
    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range (5):
                    list_bg.append(Background(f'level1bg{i}', position))
                    list_bg.append(Background(f'level1bg{i}', position=(W_WIDTH,0)))
                return list_bg

