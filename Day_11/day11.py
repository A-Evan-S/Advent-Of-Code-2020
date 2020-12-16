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
    while True:
        changed = step(seats)
        if not changed:
            break
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def display_seats(seats):
    for row in seats:
        for c in row:
            print(c, end='')
        print()

def step(seats):
    neighbor_arr = [[0 for _ in range(len(seats[0]))] for _ in range(len(seats))]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            r = row-1
            c = col-1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1
            r += 1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1
            r+= 1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1
            c += 1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1
            c += 1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1
            r -= 1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1
            r -= 1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1
            c -= 1
            if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                if seats[r][c] == '#':
                    neighbor_arr[row][col] += 1

    changed = False

    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == 'L' and neighbor_arr[row][col] == 0:
                seats[row][col] = '#'
                changed = True
            elif seats[row][col] == '#' and neighbor_arr[row][col] >= 4:
                seats[row][col] = 'L'
                changed = True

    return changed

def part2(input):
    seats = [[c for c in line] for line in input]
    while True:
        changed = step2(seats)
        if not changed:
            break
    count = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                count += 1
    return count

def step2(seats):
    neighbor_arr = [[0 for _ in range(len(seats[0]))] for _ in range(len(seats))]
    adj = [(0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,-1),(-1,0),(-1,1)]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            for a in adj:
                r = row
                c = col
                while True:
                    r -= a[0]
                    c -= a[1]
                    if 0 <= r < len(seats) and 0 <= c < len(seats[0]):
                        if seats[r][c] == '#':
                            neighbor_arr[row][col] += 1
                            break
                        elif seats[r][c] == 'L':
                            break
                    else:
                        break

    changed = False

    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if seats[row][col] == 'L' and neighbor_arr[row][col] == 0:
                seats[row][col] = '#'
                changed = True
            elif seats[row][col] == '#' and neighbor_arr[row][col] >= 5:
                seats[row][col] = 'L'
                changed = True

    return changed

if __name__ == '__main__':
    main()
