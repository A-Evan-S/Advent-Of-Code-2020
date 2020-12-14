import math
class Ship:
    directions = {'E':0,'N':90,'W':180,'S':270}

    def __init__(self):
        self.direction = 0.0
        self.pos = [0,0]

    def turn_left(self, angle):
        self.direction = (self.direction + angle + 360) % 360

    def turn_right(self, angle):
        self.direction = (self.direction - angle + 360) % 360

    def forward(self, d):
        self.pos[0] += d * math.cos(math.pi * self.direction/180)
        self.pos[1] += d * math.sin(math.pi * self.direction / 180)

    def move(self, direction, d):
        if direction == 'E':
            self.pos[0] += d
        elif direction == 'W':
            self.pos[0] -= d
        elif direction == 'N':
            self.pos[1] += d
        elif direction == 'S':
            self.pos[1] -= d

class Waypoint:

    def __init__(self):
        self.pos = [10,1]

    def move(self, direction, d):
        if direction == 'E':
            self.pos[0] += d
        elif direction == 'W':
            self.pos[0] -= d
        elif direction == 'N':
            self.pos[1] += d
        elif direction == 'S':
            self.pos[1] -= d

    def turn(self, direction, amount, ship):
        if direction == 'R':
            amount *= -1
        dist_to_ship = math.sqrt((self.pos[0])**2 + (self.pos[1])**2)
        curr_angle = math.atan2(self.pos[1],self.pos[0]) * 180 / math.pi
        new_angle = curr_angle + amount
        self.pos[0] = round(dist_to_ship * math.cos(new_angle * math.pi / 180))
        self.pos[1] = round(dist_to_ship * math.sin(new_angle * math.pi / 180))

class Ship2:
    def __init__(self):
        self.pos = [0,0]

    def move(self, waypoint, distance):
        x_dif = waypoint.pos[0]
        y_dif = waypoint.pos[1]
        self.pos[0] += distance * x_dif
        self.pos[1] += distance * y_dif

def main():
    input = []
    with open('day12_input.txt') as f:
        for line in f:
            input.append(line.strip())
    print("Part 1:", part1(input))
    print("Part 2:", part2(input))

def part1(input):
    my_ship = Ship()
    for line in input:
        command = line[0]
        val = int(line[1:])
        if command in 'NSEW':
            my_ship.move(command, val)
        elif command == 'L':
            my_ship.turn_left(val)
        elif command == 'R':
            my_ship.turn_right(val)
        elif command == 'F':
            my_ship.forward(val)
        else:
            raise RuntimeError("Invalid command")
    return abs(my_ship.pos[0]) + abs(my_ship.pos[1])

def part2(input):
    my_ship = Ship2()
    waypoint = Waypoint()
    for line in input:
        command = line[0]
        val = int(line[1:])
        if command in 'NSEW':
            waypoint.move(command, val)
        elif command in 'LR':
            waypoint.turn(command, val, my_ship)
        elif command == 'F':
            my_ship.move(waypoint, val)
        else:
            raise RuntimeError("Invalid command")
    return abs(my_ship.pos[0]) + abs(my_ship.pos[1])

if __name__ == '__main__':
    main()

