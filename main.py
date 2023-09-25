import anvil
import multiprocessing
from world import World as wd
import time
import random

# open region files
start_time = time.time()
files_completed = 0
region_radius = 2
files_total = (region_radius * 2)**2

def main(region_radius):
    if __name__ == "__main__":
        print("Starting Planetoids Generator!")
        file_gen_list = []
        for i in range(-region_radius, region_radius):
            for j in range(-region_radius, region_radius):
                file_gen_list += [(i, j)]

        split = len(file_gen_list) // 2

        p1 = multiprocessing.Process(target=process_regions, args=(file_gen_list[0:split],))
        p2 = multiprocessing.Process(target=process_regions, args=(file_gen_list[split:],))

        p1.start()
        p2.start()

        p1.join()
        p2.join()
        print("Done!")

def process_regions(process_list):
    for region in process_list:
        create_region_file(region[0], region[1])


def create_region_file(i, j):
    print("Making file: " + str(i) + " " + str(j))
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
    print("--- %s seconds ---" % (time.time() - start_time))

main(region_radius)








