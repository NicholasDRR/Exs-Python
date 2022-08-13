from enum import Enum, auto


class Direction(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Direction):
        raise ValueError('Cannot move in this direction!')
    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Direction.right))
    print(move(Direction.down))
    print(move(Direction.up))
    print(move(Direction.left))
print()
for direction in Direction:
    print(direction)
