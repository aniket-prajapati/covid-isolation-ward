import unittest
from covid_robot import CovidBot


class Testing(unittest.TestCase):
    def test_input(self):
        grid_coordinates = '5 5'
        robot_position = '1 2 N'
        robot_movement = 'LMLMLMLMM'
        output = '1 3 N'
        covid_bot = CovidBot(grid_coordinates, robot_position, robot_movement)
        process_output = covid_bot.process_input()
        print(process_output)
        self.assertEqual(output, process_output, "should be 1 3 N")


if __name__ == '__main__':
    unittest.main()
