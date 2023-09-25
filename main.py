import anvil
from world import World as wd
import random


region = anvil.EmptyRegion(0, 0)
subfloor = wd.plane(1)
floor = wd.plane(2)

p_count = 100
region_origin = (0, 0)
rand_size_list = []
rand_coords = []
for planet in range(0, p_count):
    rand_size = random.randint(4, 20)
    rand_size_list += [rand_size]
    rand_x = random.randint(region_origin[0] + rand_size, region_origin[0] + 511 - rand_size)
    rand_y = random.randint(-35 + rand_size, 200 - rand_size)
    rand_z = random.randint(region_origin[1] + rand_size, region_origin[1] + 511 - rand_size)
    rand_coords += [(rand_x, rand_y, rand_z)]

print(rand_coords)


bedrock = anvil.Block('minecraft', 'bedrock')
water = anvil.Block('minecraft', 'water')
oak_log = anvil.Block('minecraft', "oak_log")
oak_leaves = anvil.Block('minecraft', "oak_leaves")

region = wd.apply_block(region, (0, -63, 0), subfloor, bedrock)
region = wd.apply_block(region, (0, -62, 0), floor, water)

for i in range(len(rand_coords)):
    inner, outer = wd.sphere(rand_size_list[i])
    region = wd.apply_block(region, rand_coords[i], inner, oak_log)
    region = wd.apply_block(region, rand_coords[i], outer, oak_leaves)

filename = 'region/r.0.0.mca'
region.save(filename)



