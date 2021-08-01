from src.monster import (
    get_monster_map,
    monsters_alive,
    monsters_have_moves
)

from src.map_world import (
    load_map,
    display_map
)

def run(number_of_monsters):
    """
    The program should run until all the monster have been
    destroyed, or each monster has moved at least 10,000 times. When two Monsters
    fight, logging.info out a message like:

    Bar has been destroyed by monster 10 and monster 34!
    """
    print("****************The Program is Started*******\n")
    world = load_map()
    monster_list = get_monster_map(number_of_monsters, world)

    # This is our main loop
    while monsters_alive(monster_list) and monsters_have_moves(monster_list):
        # Wander all Monsters
        for monster in monster_list:
            monster.wander(world)

        # Check for collided Monsters - if they're on the same spot. They fight
        # and they kill all involved and the city (as 1+ Monsters can occupy)
        collisions = {}
        for monster in monster_list:
            check = collisions.get(monster.location)
            if check:
                print(f"{monster.location.name} has been destroyed by monster {check.id} and monster {monster.id}")

                # Kill the involved Monsters and mark the city as destroyed
                monster.location.destroy()
                monster.kill()
                check.kill()
                for loc in world:
                    loc.remove_city_from_directions(monster.location.name)
            else:
                collisions[monster.location] = monster

        # Update our kill stats so we don't iterate over dead Monsters
        monster_list = [x for x in monster_list if x.is_alive()]
    print("*******************************************************************************************\n")
    print("Monsters are all dead or out of moves!")
    print("The Final map after destruction of city is:")
    print("*******************************************************************************************\n")
    # printing the Results
    display_map(world)
    print("*************************************Completed*****************************************************\n")

