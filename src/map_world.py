import os
from src.config import (
    logging,
    DEFAULT_FILE_NAME
)




class City:
    """ Can be destroyed, has a name and links """

    def __init__(self, name):
        self.name = name
        self.links = {}

    def get_directions(self):
        """ Available links - remember these can be blown away! """
        return self.links

    def remove_city_from_directions(self, citySearch):
        self.links = {k: v for k, v in self.links.items() if not citySearch == v}

    def destroy(self):
        self.links = {}

    def is_destroyed(self):
        return len(self.links) == 0

def load_map():
    """ You should create a program that reads in the world map """
    map_world_list = []
    """ Assumptions:
        o Always use the = sign to split
        o Data is formatted as in world_map_small
        o No control/newline characters peppered through lines
    """
    INPUT_FILE_NAME=  os.getenv('FILE_NAME', DEFAULT_FILE_NAME)
    with open(INPUT_FILE_NAME) as mapFile:
        for entry in mapFile:
            tmpCity = City(entry.split(' ', 1)[0])

            # Extract the location links and wire them up for our city
            locations = entry.split(' ', 1)[1]
            for direction in locations.split(" "):
                # What a line - this creates our hashmap of direction to city
                tmpCity.links[direction.split("=")[0].lower()] = \
                    direction.split("=")[1].strip()
            map_world_list.append(tmpCity)

    logging.debug(f"Created {len(map_world_list)} city entries")
    return map_world_list

def display_map(map_list):
    for city in map_list:
        if city.is_destroyed():
            continue

        result = city.name + " "
        # The order should match that of the input
        # Exceptions are cheaper than tests in Python so use that
        try:
            location = city.get_directions()["north"]
            result = result + "north=" + location + " "
        except KeyError:
            pass
        try:
            location = city.get_directions()["south"]
            result = result + "south=" + location + " "
        except KeyError:
            pass
        try:
            location = city.get_directions()["east"]
            result = result + "east=" + location + " "
        except KeyError:
            pass
        try:
            location = city.get_directions()["west"]
            result = result + "west=" + location + " "
        except KeyError:
            pass
        print(result)