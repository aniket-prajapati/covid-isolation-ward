# covid-isolation-ward
FOOD &amp; MEDICINE DELIVERY ROBOT FOR COVID ISOLATION WARD

Programming a robot which can deliver food and medicine to patients affected by COVID who have been isolated into a seperate ward. A person sitting outside the isolation ward will send instructions though wireless signals to navigate the robot near the patient's bed.

The COVID isolation ward's floor is divided up into a grid to simplify the navigation. The robot's position in the grid is represented by three characters. The first two represent the x and y coordinates while the last character represents one of the four cardinal compass points. An example of this is 0, 0, N, which would mean the robot is in the bottom left corner, facing North.

Now the person sitting outside the ward can control the navigation of the robot by sending a stream of letters. The possible letters are 'L', 'R' and 'M'. The letter 'L' and 'R' will make the robot spin 90 degrees left and right respectively without moving from the current position, while the letter 'M' will make it move forward by on grid point.

Assume the square directly North from (x, y) is (x, y+1).

Below described is the input and output format for the navigational system.

Input:
Each input has 3 lines. 

The first line of input will give the upper right coordinates of the grid representing the COVID ward's floor, the lower left coordinates are assumed as 0,0.

The second line of input will give the robot's position. The input will have two integers and a letter separated by spaces, which corresponds to the x and y coordinates of the robot and the robot's orientation.

The third line of input will have the instruction for the robot to navigate. 

Output:
The output should print the final coordinates of the robot and it's orientation.

Sample Input and Output

Example: 1

Test Input:
5 5
1 2 N
LMLMLMLMM

Expected Output:
1 3 N

Example: 2

Test Input:
5 5
3 3 E
MMRMMRMRRM

Expected Output:
5 1 E
