import anvil
import multiprocessing
from world import World as wd
import time
import numpy as np
import random

# start program timer & set program variables
start_time = time.time()
region_radius = 4
water_floor = False
planet_count = 150


def main(region_radius):
    if __name__ == "__main__":
        print("Starting Planetoids Generator!")

        # generate the coordinates for all the region
        file_gen_list = []
        for i in range(-region_radius, region_radius):
            for j in range(-region_radius, region_radius):
                file_gen_list += [(i, j)]

        # set up multiprocessing
        thread_count = multiprocessing.cpu_count()-1
        file_assign = np.array_split(file_gen_list, thread_count)
        all_processes = []

        # generate overworld files and wait until finished
        for thread_num in range(thread_count):
            p = multiprocessing.Process(target=process_overworld, args=(file_assign[thread_num],))
            all_processes.append(p)
            p.start()
        for p in all_processes:
            p.join()
        print("Overworld Complete!")

        # start generating nether planets
        print("Starting to generate nether!")



# function that helps setup multiprocessing
def process_overworld(process_list):
    for region in process_list:
        create_overworld_files(region[0], region[1])

# function that populates the overworld region files
def create_overworld_files(i, j):
    region = anvil.EmptyRegion(i, j)
    region_origin = (i * 512, j * 512)

    # make an array of coordinates for the location of each sphere
    rand_size_list, rand_coords = wd.planet_array(planet_count, region_origin)

    # add floor
    if water_floor:
        region = wd.apply_block(region, (region_origin[0], -63, region_origin[1]),
                                wd.plane(1), anvil.Block('minecraft', 'bedrock'))
        region = wd.apply_block(region, (region_origin[0], -62, region_origin[1]),
                                wd.plane(2), anvil.Block('minecraft', 'water'))
    else:
        region = wd.apply_block(region, (region_origin[0], -63, region_origin[1]),
                                wd.plane(1), anvil.Block('minecraft', 'air'))

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

    print("--- Finished overworld region " + i_str + '\t' + j_str + " in %s seconds ---" % (time.time() - start_time))

def process_nether(process_list):
    for region in process_list:
        create_nether_files(region[0], region[1])

def create_nether_files(i, j):
    region = anvil.EmptyRegion(i, j)
    region_origin = (i * 512, j * 512)

    # region file
    filename = 'DIM-1/region/r.' + str(i) + '.' + str(j) + '.mca'
    region.save(filename)

    i_str = str(i)
    if i >= 0:
        i_str = "+" + str(i)
    j_str = str(j)
    if j >= 0:
        j_str = "+" + str(j)

    print("--- Finished nether region " + i_str + '\t' + j_str + " in %s seconds ---" % (time.time() - start_time))

main(region_radius)








