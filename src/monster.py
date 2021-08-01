import random
from src.util import   monster_id_generator
from src.config import (
    MONSTER_MOVE,
    logging
)


class Monster:
    """
      This is the monster class
      we are defining all the properties and functionality monster can do
    """

    monster_id_generator = monster_id_generator().__next__

    def __init__(self, location):
        """
        :param location: location
        """
        self.location = location
        self.id = Monster.monster_id_generator()
        self.__move_left = MONSTER_MOVE
        self.__is_alive = True


    def wander(self, map_list):
        """
        this method will help monster to move
        :param map_list: contains all the locations
        :return:
        """

        if self.has_moves() and self.is_alive:
            if len(self.location.get_directions().values()) > 0:
                new_destination = random.choice([*self.location.get_directions().values()])
                logging.debug(f"Monster-{self.id}  will move to {new_destination}")
                #logging.debug(f"the type of map is {type(map_list)}")
                for dst in map_list:
                    if dst.name == new_destination:
                        self.location = dst
            else:
                # If he stuck ,then  set count to 1
                logging.debug("He got stuck!")
                self.__move_left = 1
            self.__move_left = self.__move_left - 1
            logging.debug(f" Monster-{self.id} moved to {self.location.name}")



    def get_location(self):
        """
        it is a getter method
        :return: location
        """
        return self.location

    def kill(self):
        """
        This a setter type method which will re initialize the monster  move and kill the monster
        :return:
        """
        self.__move_left = 0
        self.__is_alive = False

    def has_moves(self):
        """
        :return:  True or False
        """
        return self.__move_left > 0

    def is_alive(self):
        """
        :return:  True or False
        """
        return self.__is_alive

def monsters_have_moves(monsters):
    moving_monsters = False
    for monster in monsters:
        if monster.has_moves():
            moving_monsters = True
    return moving_monsters

def get_monster_map(monster_counts, map_list):
    """
    :param monster_counts: number of monsters
    :param map_list:  all locations list on map
    :return:
    """

    monsters = []
    for _ in range(monster_counts):
        # Pick a random city to put him in
        chosenCity = random.choice(map_list)
        monsters.append(Monster(chosenCity))

    logging.debug(f"Created {len(monsters)} Monsters")
    return monsters


def monsters_alive(monsters):
    alive_monsters = False
    for monster in monsters:
        if monster.is_alive():
            alive_monsters = True
    return alive_monsters

