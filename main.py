import anvil
import multiprocessing
from world import World as wd
import time
import numpy as np
import random

# open region files
start_time = time.time()
files_completed = 0
region_radius = 3
files_total = (region_radius * 2)**2

def main(region_radius):
    if __name__ == "__main__":
        print("Starting Planetoids Generator!")
        file_gen_list = []
        for i in range(-region_radius, region_radius):
            for j in range(-region_radius, region_radius):
                file_gen_list += [(i, j)]

        thread_count = multiprocessing.cpu_count()-1
        file_assign = np.array_split(file_gen_list, thread_count)

        all_processes = []
        for thread_num in range(thread_count):
            p = multiprocessing.Process(target=process_regions, args=(file_assign[thread_num],))
            all_processes.append(p)
            p.start()

        for p in all_processes:
            p.join()
        print("Done!")

def process_regions(process_list):
    for region in process_list:
        create_region_file(region[0], region[1])


def create_region_file(i, j):
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
    wd.make_planets(region, rand_size_list, rand_coords)

    # region file
    filename = 'region/r.' + str(i) + '.' + str(j) + '.mca'
    region.save(filename)

    i_str = str(i)
    if i >= 0:
        i_str = "+" + str(i)
    j_str = str(j)
    if j >= 0:
        j_str = "+" + str(j)

    print("--- Finished region " + i_str + '\t' + j_str + " in %s seconds ---" % (time.time() - start_time))

main(region_radius)








