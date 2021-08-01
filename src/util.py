def monster_id_generator(firstval=0, step=1):
    x = firstval
    while 1:
        yield x
        x += step