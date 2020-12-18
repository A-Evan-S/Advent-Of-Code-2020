from aoc_utils import timed

def main():
    input = []
    with open('day11_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def part1(input):
    seats = [[c for c in line] for line in input]
    adj_map = build_adjacency_map(seats)
    while step(seats, adj_map, 4):
        pass
    return sum(row.count('#') for row in seats)

def part2(input):
    seats = [[c for c in line] for line in input]
    adj_map = build_adjacency_map2(seats)
    while step(seats, adj_map, 5):
        pass
    return sum(row.count('#') for row in seats)

def display_seats(seats):
    for row in seats:
        for c in row:
            print(c, end='')
        print()

def build_adjacency_map(seats):
    adj_map = {}
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            neighbors = []
            for r in range(-1,2):
                for c in range(-1,2):
                    if r != 0 or c != 0:
                        if 0 <= row+r < len(seats) and 0 <= col+c < len(seats[0]):
                            neighbors.append((row+r, col+c))
            adj_map[(row, col)] = neighbors
    return adj_map

def step(seats, adj_map, num_for_empty):
    neighbor_arr = [[0 for _ in range(len(seats[0]))] for _ in range(len(seats))]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            for neighbor in adj_map[(row,col)]:
                if seats[neighbor[0]][neighbor[1]] == '#':
                    neighbor_arr[row][col] += 1
    changed = False
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == 'L' and neighbor_arr[row][col] == 0:
                seats[row][col] = '#'
                changed = True
            elif seats[row][col] == '#' and neighbor_arr[row][col] >= num_for_empty:
                seats[row][col] = 'L'
                changed = True
    return changed

def build_adjacency_map2(seats):
    adj_map = {}
    adj = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            neighbors = []
            for a in adj:
                r = row
                c = col
                while True:
                    r -= a[0]
                    c -= a[1]
                    if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                        if seats[r][c] != '.':
                            neighbors.append((r,c))
                            break
                    else:
                        break
            adj_map[row, col] = neighbors
    return adj_map

if __name__ == '__main__':
    main()
