class CovidBot:
    # Initializing variables
    """ This class will be responsible for processing covid robot input and return an output
        with the final position of the robot """

    def __init__(self, coordinates, position, movement):
        self.input_coordinates = coordinates.split(coordinates[1])
        self.input_position = position.split(position[1])
        self.x_axis = int(self.input_position[0])
        self.y_axis = int(self.input_position[1])
        self.x_max = int(self.input_coordinates[0])
        self.y_max = int(self.input_coordinates[1])
        self.orientation = self.input_position[2]
        self.input_movement = movement
        self.check_input()
        self.left_orientation = {"N": "W", "W": "S", "S": "E", "E":"N"}
        self.right_orientation = {"N": "E", "E": "S", "S": "W", "W":"N"}

    def move_position(self):
        """ Method to move position of the robot within the grid coordinates """
        if self.orientation == "N" and self.y_max > self.y_axis:
            self.y_axis += 1
        elif self.orientation == "E" and self.x_max > self.x_axis:
            self.x_axis += 1
        elif self.orientation == "S" and self.y_axis > 0:
            self.y_axis -= 1
        elif self.orientation == "W" and self.x_axis > 0:
            self.x_axis -= 1

    def check_input(self):
        """ Method to check if given inputs for the robot position are not out of the grid """
        if int(self.input_position[0]) > int(self.input_coordinates[0]) or \
                int(self.input_position[1]) > int(self.input_coordinates[1]):
            print("Robot Position out of grid coordinates")
            exit()
    
    def process_input(self):
        """ Method to compute the final position the robot will go to and return the output """
        for i in range(len(self.input_movement)):
            if self.input_movement[i] == 'L':
                self.orientation = self.left_orientation.get(self.orientation)
            elif self.input_movement[i] == 'R':
                self.orientation = self.right_orientation.get(self.orientation)
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
