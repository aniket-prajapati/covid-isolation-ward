class CovidBot:

    def __init__(self, coordinates, position, movement):
        self.x_axis = None
        self.y_axis = None
        self.orientation = None
        self.input_coordinates = coordinates
        self.input_position = position
        self.input_movement = movement
        self.parse_input()

    def rotate_left(self):
        if self.orientation == "N":
            self.orientation = "W"
        elif self.orientation == "W":
            self.orientation = "S"
        elif self.orientation == "S":
            self.orientation = "E"
        elif self.orientation == "E":
            self.orientation = "N"

    def rotate_right(self):
        if self.orientation == "N":
            self.orientation = "E"
        elif self.orientation == "E":
            self.orientation = "S"
        elif self.orientation == "S":
            self.orientation = "W"
        elif self.orientation == "W":
            self.orientation = "N"

    def move_position(self):
        if self.orientation == "N":
            self.y_axis += 1
        elif self.orientation == "E":
            self.x_axis += 1
        elif self.orientation == "S":
            self.y_axis -= 1
        elif self.orientation == "W":
            self.x_axis -= 1

    def parse_input(self):
        self.input_coordinates = self.input_coordinates.split(self.input_coordinates[1])
        self.input_position = self.input_position.split(self.input_position[1])
        self.x_axis = int(self.input_position[0])
        self.y_axis = int(self.input_position[1])
        self.orientation = self.input_position[2]

        if int(self.input_position[0]) > int(self.input_coordinates[0]) or \
                int(self.input_position[1]) > int(self.input_coordinates[1]):
            print("Robot Position out of grid coordinates")
            exit()
    
    def process_input(self):
        for i in range(len(self.input_movement)):
            if self.input_movement[i] == 'L':
                self.rotate_left()
            elif self.input_movement[i] == 'R':
                self.rotate_right()
            else:
                self.move_position()

        return "%s %s %s" % (self.x_axis, self.y_axis, self.orientation)


if __name__ == '__main__':

    input_coordinates = input("Please Provide upper right coordinates of the grid: ")
    input_position = input("Please Provide Robot's position: ")
    input_movement = input("Please Provide Robot's movement: ")

    covid_bot = CovidBot(input_coordinates, input_position, input_movement)
    process_output = covid_bot.process_input()
    print(process_output)
