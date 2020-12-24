from collections import defaultdict

from aoc_utils import timed


def main():
    input = []
    with open('day24_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))


def part1(input):
    tiles = create_tiles(input)
    return list(tiles.values()).count(True)


def part2(input):
    tiles = create_tiles(input)
    for _ in range(100):
        step(tiles)
    return list(tiles.values()).count(True)


def parse_line(line):
    directions = []
    while len(line) > 0:
        if line.startswith('e') or line.startswith('w'):
            directions.append(line[0])
            line = line[1:]
        else:
            directions.append(line[0:2])
            line = line[2:]
    return directions


def create_tiles(input):
    tiles = defaultdict(lambda: False)
    for line in input:
        row, col = 0, 0
        for direction in parse_line(line):
            if direction == 'e':
                col += 1
            elif direction == 'w':
                col -= 1
            elif direction == 'ne':
                col += row % 2
                row -= 1
            elif direction == 'nw':
                row -= 1
                col -= row % 2
            elif direction == 'se':
                col += row % 2
                row += 1
            elif direction == 'sw':
                row += 1
                col -= row % 2
        tiles[row, col] = not tiles[row, col]
    return tiles


def step(tiles):
    num_neighbors = defaultdict(lambda: 0)
    for tile in tiles.keys():
        if tiles[tile]:
            row, col = tile
            if row % 2 == 0:
                neighbors = [(0, 1), (0, -1), (-1, 0), (-1, -1), (1, 0), (1, -1)]
            else:
                neighbors = [(0, 1), (0, -1), (-1, 0), (-1, 1), (1, 0), (1, 1)]
            num_neighbors[row, col] += 0
            for neighbor in neighbors:
                num_neighbors[row + neighbor[0], col + neighbor[1]] += 1
    for tile in num_neighbors.keys():
        if tiles[tile]:
            if num_neighbors[tile] == 0 or num_neighbors[tile] > 2:
                tiles[tile] = False
        else:
            if num_neighbors[tile] == 2:
                tiles[tile] = True


if __name__ == '__main__':
    main()
