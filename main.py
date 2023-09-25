import anvil
import multiprocessing
from world import World as wd

import random

# open region files
files_completed = 0
region_radius = 2
files_total = (region_radius * 2)**2

def main(region_radius):
    print("in  main")
    for i in range(-region_radius, region_radius):
        for j in range(-region_radius, region_radius):
            create_region_file(i, j)

def create_region_file(i, j):
    print("making file")
    region = anvil.EmptyRegion(i, j)
    region_origin = (i * 512, j * 512)

    # define block objects
    bedrock = anvil.Block('minecraft', 'bedrock')
    water = anvil.Block('minecraft', 'water')
    oak_log = anvil.Block('minecraft', "oak_log")
    oak_leaves = anvil.Block('minecraft', "oak_leaves")

    # make an array of coordinates for the location of each sphere
    rand_size_list, rand_coords = wd.planet_array(50, region_origin)

    # add floor (bedrock and water, can switch to air later)
    subfloor = wd.plane(1)
    floor = wd.plane(2)
    region = wd.apply_block(region, (region_origin[0], -63, region_origin[1]), subfloor, bedrock)
    region = wd.apply_block(region, (region_origin[0], -62, region_origin[1]), floor, water)

    # create spheres at previously defined locations and fill blocks
    for n in range(len(rand_coords)):
        inner, outer = wd.sphere(rand_size_list[n])
        region = wd.apply_block(region, rand_coords[n], inner, oak_log)
        region = wd.apply_block(region, rand_coords[n], outer, oak_leaves)

    # region file
    filename = 'region/r.' + str(i) + '.' + str(j) + '.mca'
    region.save(filename)

main(region_radius)








