"""
input: number of available blocks
output: number of blocks left over after building tallest possible valid structure

Explicit rules:
    - blocks are cubes
    - top layer is a single block
    - no gaps between blocks(?)
    - upper layer block must be supported by 4 blocks in a lower layer(?)
    - lower layer block can support more than 1 block in upper layer(?)

Implicit rules:
    - not sure at all what these would be
    - no horizontal gaps between blocks obviously since physics doesn't allow for vertical gaps anyway

Questions:
    - can a block go on a crevice?
    - what does it mean to be supported by 4 blocks in a lower layer??
    - 

Data structures:
    - maybe a nested list

Algo:
    - start by building layers
    - stop if we don't have enough to build valid layers


"""

def calculate_leftover_blocks(n):
    remaining_blocks = n
    curr_layer_n = 0
    blocks_req = (curr_layer_n + 1)**2

    while remaining_blocks >= blocks_req:
        remaining_blocks -= blocks_req
        curr_layer_n += 1
        blocks_req = (curr_layer_n + 1)**2

        
    return remaining_blocks

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True