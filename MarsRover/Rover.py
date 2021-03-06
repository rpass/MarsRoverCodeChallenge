from MarsRover.DangerousMoveException import DangerousMoveException


class Rover:
    def __init__(self, position, bearing, safe_zone):
        self.position = position
        self.bearing = bearing
        self.safeZone = safe_zone
        self.command_sequence = []

    def is_position_safe(self, position):
        return self.safeZone.is_coordinate_in_safe_zone(position)

    def move(self):
        if self.bearing == "N":
            next_position = (self.position[0], self.position[1] + 1)

        elif self.bearing == "E":
            next_position = (self.position[0] + 1, self.position[1])

        elif self.bearing == "S":
            next_position = (self.position[0], self.position[1] - 1)

        elif self.bearing == "W":
            next_position = (self.position[0] - 1, self.position[1])

        if not self.is_position_safe(next_position):
            raise DangerousMoveException(self.position, self.safeZone, next_position)
        self.position = next_position

    def turn_left(self):
        nwse = "NWSE"
        self.bearing = shift_right_bearing_in_sequence(self.bearing, nwse)

    def turn_right(self):
        nesw = "NESW"
        self.bearing = shift_right_bearing_in_sequence(self.bearing, nesw)

    def save_command_sequence(self, command_sequence):
        self.command_sequence = command_sequence

    def execute_command_sequence(self):
        for command in self.command_sequence:
            if command == 'M':
                self.move()
            elif command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()

    def format_current_position(self):
        return "%s %s %s" % (self.position[0], self.position[1], self.bearing)

    def report_current_position(self):
        print(self.format_current_position())


def shift_right_bearing_in_sequence(current_bearing, nwse):
    index_of_current_bearing = nwse.find(current_bearing)
    index_of_bearing_left_of_current = (index_of_current_bearing + 1) % len(nwse)
    return nwse[index_of_bearing_left_of_current]
