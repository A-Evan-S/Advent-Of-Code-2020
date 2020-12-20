from aoc_utils import timed
import math, copy

def main():
    with open('day20_input.txt') as f:
        input = f.read()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, None))

def part1(input):
    global picture
    picture = find_picture(input)
    return picture.multiply_corners()

def part2(input):
    if not input:
        global picture
    else:
        picture = find_picture(input)

    image = picture.create_image()

    for _ in range(2):
        for _ in range(4):
            image = rotate_clockwise(image)
            num_found, image = find_monsters(image)
            if num_found != 0:
                return sum(row.count('#') for row in image)
        flip_vertical(image)
    raise Exception('Unable to find monsters')

def flip_vertical(image):
    for row in range(len(image) // 2):
        for col in range(len(image[0])):
            swap(image, row, col, len(image) - 1 - row, col)

def rotate_clockwise(image):
    new_image = [['' for _ in range(len(image[0]))] for _ in range(len(image))]
    for row in range(len(image)):
        for col in range(len(image[0])):
            new_image[col][len(image) - 1 - row] = image[row][col]
    return new_image

def swap(image, r1, c1, r2, c2):
    tmp = image[r1][c1]
    image[r1][c1] = image[r2][c2]
    image[r2][c2] = tmp

class Frame:
    def __init__(self, text):
        rows = text.split('\n')
        self.frame_num = int(rows[0][5:9])
        self.pixels = [[x for x in row] for row in rows[1:]]
        self.size = len(self.pixels)

    def get_top(self):
        return ''.join(self.pixels[0])

    def get_bottom(self):
        return ''.join(self.pixels[-1])

    def get_left(self):
        return ''.join(row[0] for row in self.pixels)

    def get_right(self):
        return ''.join(row[-1] for row in self.pixels)

class Picture:
    def __init__(self, size):
        self.frames = [[None for _ in range(size)] for _ in range(size)]
        self.size = size

    def fits(self, frame, position):
        row, col = position
        if row - 1 >= 0 and self.frames[row - 1][col]:
            if frame.get_top() != self.frames[row - 1][col].get_bottom():
                return False
        if row + 1 < self.size and self.frames[row + 1][col]:
            if frame.get_bottom() != self.frames[row + 1][col].get_top():
                return False
        if col - 1 >= 0 and self.frames[row][col - 1]:
            if frame.get_left() != self.frames[row][col - 1].get_right():
                return False
        if col + 1 < self.size and self.frames[row][col + 1]:
            if frame.get_right() != self.frames[row][col + 1].get_left():
                return False
        return True

    def place(self, frame, position):
        for _ in range(4):
            if self.fits(frame, position):
                self.frames[position[0]][position[1]] = frame
                return True
            frame.pixels = rotate_clockwise(frame.pixels)
        flip_vertical(frame.pixels)
        for _ in range(4):
            if self.fits(frame, position):
                self.frames[position[0]][position[1]] = frame
                return True
            frame.pixels = rotate_clockwise(frame.pixels)
        return False

    def multiply_corners(self):
        return self.frames[0][0].frame_num * self.frames[0][-1].frame_num * self.frames[-1][0].frame_num * \
               self.frames[-1][-1].frame_num

    def create_image(self):
        image = []
        for i in range(self.size * self.frames[0][0].size - 2 * self.size):
            frame_row = i // (self.frames[0][0].size - 2)
            row_index = i % (self.frames[0][0].size - 2) + 1
            row = []
            for frame in self.frames[frame_row]:
                row.extend(frame.pixels[row_index][1:-1])
            image.append(row)
        return image

def test_starting_frame(start_frame, frames, size):
    picture = Picture(size)
    picture.place(start_frame, (0, 0))
    for row in range(size):
        for col in range(size):
            if row != 0 or col != 0:
                found_frame = False
                for i in range(len(frames)):
                    if picture.place(frames[i], (row, col)):
                        frames.pop(i)
                        found_frame = True
                        break
                if not found_frame:
                    return None
    return picture

def find_picture(input):
    frames = []
    for frame_text in input.split('\n\n'):
        frames.append(Frame(frame_text))
    size = int(math.sqrt(len(frames)))

    for i in range(len(frames)):
        test_frames = copy.deepcopy(frames)
        starting_frame = test_frames.pop(i)
        result = test_starting_frame(starting_frame, test_frames, size)
        if result:
            return result
    raise Exception('Unable to solve puzzle')

def find_monsters(image):
    with open('monster.txt') as f:
        monster = [[x for x in row.strip('\n')] for row in f.readlines()]

    num_monsters = 0

    for row in range(len(image) - len(monster)):
        for col in range(len(image[0]) - len(monster[1])):
            found_monster = True
            for r in range(len(monster)):
                for c in range(len(monster[r])):
                    if monster[r][c] == '#':
                        if image[row + r][col + c] != '#':
                            found_monster = False
            if found_monster:
                num_monsters += 1
                for r in range(len(monster)):
                    for c in range(len(monster[r])):
                        if monster[r][c] == '#':
                            image[row + r][col + c] = '0'

    return num_monsters, image

if __name__ == '__main__':
    main()
