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
    def apply_block(region, region_coords, coord_list, block):
        region = region;
        for coords in coord_list:
            if isinstance(block, list):
                region.set_block(random.choice(block), region_coords[0] + coords[0],
                                 region_coords[1] + coords[1], region_coords[2] + coords[2])
            else:
                region.set_block(block, region_coords[0] + coords[0],
                                 region_coords[1] + coords[1], region_coords[2] + coords[2])
        return region

    @staticmethod
    def make_planets(region, rand_size, rand_coords):
        for n in range(len(rand_coords)):

            inner, outer = World.sphere(rand_size[n])
            inner_block, outer_block, soil_planet = World.choose_planet_type()

            region = World.apply_block(region, rand_coords[n], inner, inner_block)
            region = World.apply_block(region, rand_coords[n], outer, outer_block)

        return region

    @staticmethod
    def planet_array(count, region_origin):
        p_count = count
        rand_size_list = []
        rand_coords = []
        for planet in range(0, p_count):
            rand_size = random.randint(4, 20)
            rand_size_list += [rand_size]
            rand_x = random.randint(region_origin[0] + rand_size, region_origin[0] + 511 - rand_size)
            rand_y = random.randint(-35 + rand_size, 191 - rand_size)
            rand_z = random.randint(region_origin[1] + rand_size, region_origin[1] + 511 - rand_size)
            rand_coords += [(rand_x, rand_y, rand_z)]

        return rand_size_list, rand_coords

    @staticmethod
    def choose_planet_type():
        outer_block = ""
        inner_block = ""
        choice_1 = random.random()
        soil_planet = False
        # wood chosen 30%
        if choice_1 <= .3:
            choice_2 = random.random()
            # oak planet 50%
            if choice_2 <= 0.5:
                inner_block = anvil.Block('minecraft', 'oak_log')
                outer_block = anvil.Block('minecraft', 'oak_leaves')

            # birch planet 13%
            elif 0.5 < choice_2 <= 0.63:
                inner_block = anvil.Block('minecraft', 'birch_log')
                outer_block = anvil.Block('minecraft', 'birch_leaves')

            # spruce planet 13%
            elif 0.63 < choice_2 <= 0.76:
                inner_block = anvil.Block('minecraft', 'spruce_log')
                outer_block = anvil.Block('minecraft', 'spruce_leaves')

            # acacia planet 4%
            elif 0.76 < choice_2 <= 0.80:
                inner_block = anvil.Block('minecraft', 'acacia_log')
                outer_block = anvil.Block('minecraft', 'acacia_leaves')

            # dark oak 4%
            elif 0.80 < choice_2 <= 0.84:
                inner_block = anvil.Block('minecraft', 'dark_oak_log')
                outer_block = anvil.Block('minecraft', 'dark_oak_leaves')

            # mangrove planet 4%
            elif 0.84 < choice_2 <= 0.88:
                inner_block = anvil.Block('minecraft', 'mangrove_log')
                outer_block = anvil.Block('minecraft', 'mangrove_leaves')

            # cherry planet 4%
            elif 0.88 < choice_2 <= 0.92:
                inner_block = anvil.Block('minecraft', 'cherry_log')
                outer_block = anvil.Block('minecraft', 'cherry_leaves')

            # jungle planet 4%
            elif 0.92 < choice_2 <= 0.96:
                inner_block = anvil.Block('minecraft', 'jungle_log')
                outer_block = anvil.Block('minecraft', 'jungle_leaves')

            # azalea planet
            else:
                inner_block = anvil.Block('minecraft', 'oak_log')
                outer_block = [anvil.Block('minecraft', 'azalea_leaves'),
                               anvil.Block('minecraft', 'flowering_azalea_leaves')]


        elif 0.3 < choice_1 <= 0.7:
        # soil planet 40%
            soil_planet = True
            choice_2 = random.random()
            # grass planet 50%
            if choice_2 <= 0.5:
                inner_block = anvil.Block('minecraft', 'dirt')
                outer_block = anvil.Block('minecraft', 'grass_block')

            # gravel planet 15%
            elif 0.50 < choice_2 <= 0.65:
                inner_block = anvil.Block('minecraft', 'gravel')
                outer_block = anvil.Block('minecraft', 'andesite')

            # podzol planet 5%
            elif 0.65 < choice_2 <= 0.70:
                inner_block = [anvil.Block('minecraft', 'dirt'),
                               anvil.Block('minecraft', 'coarse_dirt')]
                outer_block = anvil.Block('minecraft', 'podzol')

            # sand planet 15%
            elif 0.70 < choice_2 <= 0.85:
                inner_block = anvil.Block('minecraft', 'sand')
                outer_block = anvil.Block('minecraft', 'sandstone')

            # mycelium/rooted dirt 5%
            elif 0.85 < choice_2 <= 0.90:
                inner_block = [anvil.Block('minecraft', 'dirt'), anvil.Block('minecraft', 'rooted_dirt')]
                outer_block = anvil.Block('minecraft', 'mycelium')


            # terracotta/clay planet 10%
            else:
                inner_block = anvil.Block('minecraft', 'clay')
                outer_block = anvil.Block('minecraft', 'terracotta')

        # stone planet 20%
        elif 0.7 < choice_1 <= .90:
            choice_2 = random.random()
            outer_block = [anvil.Block('minecraft', 'stone'), anvil.Block('minecraft', 'stone'),
                           anvil.Block('minecraft', 'stone'), anvil.Block('minecraft', 'stone'),
                           anvil.Block('minecraft', 'andesite'), anvil.Block('minecraft', 'diorite')]
            inner_block = [anvil.Block('minecraft', 'stone'), anvil.Block('minecraft', 'tuff'),
                           anvil.Block('minecraft', 'deepslate'), anvil.Block('minecraft', 'calcite'),
                           anvil.Block('minecraft', 'granite')]
            # coal planet 30%
            if choice_2 <= 0.3:
                inner_block.append(anvil.Block('minecraft', 'coal_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_coal_ore'))

            # iron planet 15%
            elif 0.30 < choice_2 <= 0.45:
                inner_block.append(anvil.Block('minecraft', 'iron_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_iron_ore'))

            # copper planet 15%
            elif 0.45 < choice_2 <= 0.60:
                inner_block.append(anvil.Block('minecraft', 'copper_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_copper_ore'))

            # redstone planet 10%
            elif 0.60 < choice_2 <= 0.70:
                inner_block.append(anvil.Block('minecraft', 'redstone_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_redstone_ore'))

            # lapiz planet 10%
            elif 0.70 < choice_2 <= 0.80:
                inner_block.append(anvil.Block('minecraft', 'lapis_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_lapis_ore'))


            # gold planet 10%
            elif 0.80 < choice_2 <= 0.90:
                inner_block.append(anvil.Block('minecraft', 'gold_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_gold_ore'))

            # emerald planet 7%
            elif 0.90 < choice_2 <= 0.97:
                inner_block.append(anvil.Block('minecraft', 'emerald_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_emerald_ore'))

            # diamond planet 3%
            else:
                inner_block.append(anvil.Block('minecraft', 'diamond_ore'))
                inner_block.append(anvil.Block('minecraft', 'deepslate_diamond_ore'))

        else:
        # other 10 %
            choice_2 = random.random()
            # ice planet
            if choice_2 <= 0.2:
                inner_block = anvil.Block('minecraft', 'water')
                outer_block = anvil.Block('minecraft', 'ice')

            # lava planet
            elif 0.20 < choice_2 <= 0.40:
                inner_block = anvil.Block('minecraft', 'lava')
                outer_block = [anvil.Block('minecraft', 'magma_block'),
                               anvil.Block('minecraft', 'magma_block'),
                               anvil.Block('minecraft', 'magma_block'),
                               anvil.Block('minecraft', 'cracked_deepslate_bricks'),
                               anvil.Block('minecraft', 'cracked_deepslate_tiles'),
                               anvil.Block('minecraft', 'deepslate_bricks'),
                               anvil.Block('minecraft', 'deepslate_tiles')]


            # slime planet
            elif 0.40 < choice_2 <= 0.60:
                inner_block = [anvil.Block('minecraft', 'slime_block'), anvil.Block('minecraft', 'honey_block')]
                outer_block = inner_block

            # deep_dark planet
            elif 0.60 < choice_2 <= 0.80:
                inner_block = [anvil.Block('minecraft', 'sculk'),
                               anvil.Block('minecraft', 'sculk_sensor'),
                               anvil.Block('minecraft', 'sculk_catalyst'),
                               anvil.Block('minecraft', 'stone_brick'),
                               anvil.Block('minecraft', 'obsidian'),
                               anvil.Block('minecraft', 'sculk_shrieker')
                                            ]
                outer_block = [anvil.Block('minecraft', 'sculk'), anvil.Block('minecraft', 'sculk_sensor'),
                               anvil.Block('minecraft', 'stone_brick'), anvil.Block('minecraft', 'obsidian')]

            # ocean planet
            else:
                outer_block = [anvil.Block('minecraft', 'prismarine'), anvil.Block('minecraft', 'prismarine'),
                               anvil.Block('minecraft', 'sea_lantern')]
                inner_block = [anvil.Block('minecraft', 'dark_prismarine'), anvil.Block('minecraft', 'prismarine')]

        return inner_block, outer_block, soil_planet




