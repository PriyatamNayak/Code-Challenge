import os
import logging

BASE_DIR=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
INPUT_FEEDS_DIR = os.path.join(BASE_DIR,"src","input_files")
INPUT_FILE_NAME=  os.path.join(INPUT_FEEDS_DIR, "world_map_small.txt")
LOG_DIR =  os.path.join(BASE_DIR,"log")
LOG_FILE_NAME = "monster_move_fight.log"

logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE_NAME), level=logging.DEBUG)

MONSTER_MOVE = 10000
