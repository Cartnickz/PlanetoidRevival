import math

import anvil
import random

class World:
    @staticmethod
    def sphere(size):
        inner = []
        outer = []
        for y in range(size, -size, -1):
            for x in range(-size, size):
                for z in range(-size, size):
                    dist = math.sqrt((x) ** 2 + (y) ** 2 + (z) ** 2)
                    if dist < size - 2:
                        inner += [(x, y, z)]
                    elif dist < size:
                        outer += [(x, y, z)]
        return inner, outer

    @staticmethod
    def plane(depth):
        list = []
        for y in range(0, depth):
            for x in range(0, 512):
                for z in range(0, 512):
                    list += [(x, y, z)]
        return list

    @staticmethod
    def apply_block(region, region_coords, list, block):
        region = region;
        for coords in list:
            region.set_block(block, region_coords[0] + coords[0],
                             region_coords[1] + coords[1], region_coords[2] + coords[2])
        return region

    @staticmethod
    def make_planets(region, inner, outer, inner_block, outer_block, rand_size, rand_coords):
        for n in range(len(rand_coords)):
            inner, outer = World.sphere(rand_size[n])
            region = World.apply_block(region, rand_coords[n], inner, inner_block)
            region = World.apply_block(region, rand_coords[n], outer, outer_block)

    @staticmethod
    def planet_array(count, region_origin):
        p_count = count
        rand_size_list = []
        rand_coords = []
        for planet in range(0, p_count):
            rand_size = random.randint(4, 20)
            rand_size_list += [rand_size]
            rand_x = random.randint(region_origin[0] + rand_size, region_origin[0] + 511 - rand_size)
            rand_y = random.randint(-35 + rand_size, 200 - rand_size)
            rand_z = random.randint(region_origin[1] + rand_size, region_origin[1] + 511 - rand_size)
            rand_coords += [(rand_x, rand_y, rand_z)]

        return rand_size_list, rand_coords


