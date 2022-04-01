class Collide:
    """
    this class handles collisions between lasers and the ships using an overlap function.
    the laser overlaps the picture where there is an empty area on the png file and hits the
    actual ship.
    """
    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
