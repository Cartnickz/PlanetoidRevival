import math

import anvil
from random import choice

class World:

    @staticmethod
    def create_region(i, j):
        # Create a new region with the `EmptyRegion` class at 0, 0 (in region coords)
        region = anvil.EmptyRegion(i, j)

        # Create `Block` objects that are used to set blocks
        stone = anvil.Block('minecraft', 'stone')
        dirt = anvil.Block('minecraft', 'dirt')

        # Make a 16x16x16 cube of either stone or dirt blocks
        for y in range(16):
            for z in range(512):
                for x in range(512):
                    region.set_block(choice((stone, dirt)), i * 512 + x, y, j * 512 + z)

        # Save to a file
        filename = 'region/r.' + str(i) + '.' + str(j) + '.mca'
        region.save(filename)

    @staticmethod
    def water_floor(i, j):
        region = anvil.EmptyRegion(i, j)
        bedrock = anvil.Block('minecraft', 'bedrock')
        water = anvil.Block('minecraft', 'water')
        print(i, j)
        region.fill(bedrock, i * 512, -63, j * 512, i * 512 + 511, -63, j * 512 + 511)
        region.fill(water, i * 512, -62, j * 512, i * 512 + 511, -60, j * 512 + 511)
        filename = 'region/r.' + str(i) + '.' + str(j) + '.mca'
        region.save(filename)

    @staticmethod
    def empty(i, j):
        region = anvil.EmptyRegion(i, j)
        air = anvil.Block('minecraft', 'air')
        print(i, j)
        region.fill(air, i*512, 0, j*512, i*512+511, 0, j*512+511)
        filename = 'region/r.' + str(i) + '.' + str(j) + '.mca'
        region.save(filename)

    @staticmethod
    def sphere_test(x, y, z, size):
        region = anvil.EmptyRegion(0, 0)
        # Create `Block` objects that are used to set blocks
        stone = anvil.Block('minecraft', 'stone')
        dirt = anvil.Block('minecraft', 'dirt')
        grass = anvil.Block('minecraft', 'grass_block')
        bedrock = anvil.Block('minecraft', 'bedrock')
        water = anvil.Block('minecraft', 'water')

        top_layer_active = True
        top_layer = -65
        for b in range(size, -size, -1):
            if top_layer_active:
                top_layer = b
            for a in range(-size, size):
                for c in range(-size, size):
                    if math.sqrt((a)**2 + (b)**2 + (c)**2) < size:
                        if top_layer_active or top_layer == b:
                            region.set_block(grass, a + x, b + y, c + z)
                            top_layer = b
                            top_layer_active = False
                        else:
                            region.set_block(dirt, a + x, b + y, c + z)

        region.fill(bedrock, 0, -63, 511, 0, -63, 511)
        region.fill(water, 0, -62, 511, 0, -60, 511)

        filename = 'region/r.0.0.mca'
        region.save(filename)

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
        print("Blocks applied")
        return region




