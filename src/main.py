# Assumption: As monsters randomly moving in cities ,may some cases different monsters can destroys the same cities
# As am using random move
# ALso can optimise this code further ,also make it faster using threading or multiprocessing

import os
import sys
import argparse

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.driver import  run

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--number_of_monsters", help="Please enter the number of monsters",type=int)
    parser.add_argument("-f", "--file_name", help="Please enter file name")
    arguments = parser.parse_args()
    if arguments.file_name:
        os.environ['FILE_NAME'] = arguments.file_name

    run(arguments.number_of_monsters)