import sys

grid_size = int(sys.argv[1])
distance: float = 1.6

with open(f'data/input_{grid_size ** 2}.txt', 'w') as f:
    for i in range(grid_size):
        for j in range(grid_size):
            f.write(f'{distance * j} {distance * i}\n')
