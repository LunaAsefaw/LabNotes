 ![Kartoza](img/kartoza.png)
# Week one and two
Tasks for the first two weeks:

1. Make a Simple Africa map for journal article
2. Sign up to GitHub, fork the repo and add changes or recommendations to the Handbook cartography guideline
3. Contribute to OSM and HOT tasks 

## Simple Africa Map:
![Workflow](img/simplemap.drawio.png) 

Kartoza references relating to this project:
1. QGIS Road to Nerdvana Episode 15: Making a small scale map of Africa:
https://www.youtube.com/watch?v=LJIiZfA7Iio
2. Modules 3, 5 and 6 (Symbology, Labelling and Composer)

![output](img/Final_attempt2.png)

## Github Exercise:
1. Fork the Handbook
2. Clone Repo and open on VS code
3. Add the cartography guidelines on the markdown (Follow markdown syntax)
4. To view markdown easily, install Markdown PDF or Markdown All in One and use Ctrl+Shift+V or ‘preview’ icon to see the changes you added in a markdown format
5. Save work and make a pull request

## OSM:
1. Login to account
2. Use search bar to navigate to AOI.
3. Edit> Edit by id
4. If editing polygons, choose area and trace the boundaries and add a tag. Insert ‘Yes’ if you do not know what kind of building the digitised building is, otherwise select from the drop down.
5. Save your work every 10/20 edits with a meaningful name.

Notes from Intern Hang:
1. Keep lab notes for every exercise we get, specifically focussing on steps followed, resources used and corrections made.
2. Make sure you always fork and only do a pull request on the upstream folder, the push request is on your forked repo, not the original. 
3. Cool extensions to have: Github pull request, Markdown All in One, Spell check


# Week 3

Intern Hang Notes:

## Binary number system:
Computer works like light switches, 0-> off and 1-> on. 

Counting systems start from 0, so 16 options could have 15 as a maximum because 0 is a minimum number (like an array when coding)

1010 means 10.
1010 has four numbers, and you multiply the first place value (from left to right) by two so 1010:

fourth number is 2<sup>3</sup>=8, 

third number is  2<sup>2</sup>=4, 

second number is  2<sup>1</sup>=2, 

first number is  2<sup>0</sup>=1, 

Then to get the value 10: (8x1)+(4x0)+(2x1)+(1x0)=10

So when the question is convert 10 to binary:
1.  Think of the suitable decimal position, if we use just three, it would be 4+2+1= 7 and that is less than 10 so increase the decimal position to 4, that would be 8+4+2+1 which is greater than 10, so we are using 4 positions.
2.  Then you think of the multiplication of the positions that would add up to 10: If you said (8x0)+(4x1)+(1x2)+(1x1)=7 so that wont work. Then try (8x1)+(4x0)+(2x1)+(1x0), which adds up to 10. 

Practice questions:
1. Convert 23 to binary:
   
   1.1. 23 so position would be 16+8+4+2+1=31 since if you used 3 positions, it would be less than 23.

   1.2. Then the multiplication sum: 
   
   16x1:1  
   
   8x0: 0
   
   4x1: 1
   
   2x1:  1
   
   <u>1x1: 1</u>

So 23 in binary would be 10111.

Then converting binary to regular numbers:

(16x1)+(8x0)+(4x1)+(2x1)+(1x1)=23

## Hexadecimal number system:
Hexadecimal uses the numbers 0-9. Now if you want to write 10, you're using the first two symbols, which means you have exhausted the list available since we are meant to have 16 symbols. Therefore, after 9, we use A-F. 

8 4 2 1 ----> Hex

0 0 0 0 ----> 0

0 0 0 1 ----> 1

0 0 1 0 ----> 2

0 0 1 1 ----> 3

0 1 0 0 ----> 4

1 0 0 1 ----> 9

1 0 1 0 ----> A (because we reached a point of repetition of numbers)

1 0 1 1 ----> B

1 1 1 1 ----> F (15)

Example:
Convert 1100111010011010<sub>2</sub> to Hex
 
Step 1: Divide into groups of 4:

1100 1110 1001 1010

Step 2: Represent the groups by hex

1100 is 8x1+4x1= 12 and that's C

1110 is 8x1+4x1+2x1= 14 and that's E

1001 is 8x1 + 1= 9

1010 is 8x1 +2x1= 10 and that's A
 so 1100111010011010<sub>2</sub> is CE9A<sub>16</sub>

Therefore, the list for hexadecimal number system wil be: 16<sup>0</sup> which ranges from 0-F then 16<sup>1</sup> which ranges 1(0-F)-F(F-F) then 16<sup>2</sup> and so forth.

## Computer Hardware
Component | Icon       | Description
----------|------------|------------------------
   CPU (Central Processing Unit)|![CPU](img/CPU.png)| This is an electronic machinery that carries out instructions from the programs that allow a computer to perform tasks. So this helps make the computations.
   GPU (Graphic Processing Unit) | ![GPU](img/GPU.png)| This works similarly to a CPU but is designed to accelerate graphics rendering.
   RAM (Random Access Memory)| ![RAM](img/RAM.png)| Short term memory where data is stored as the processor needs. Difference between this and ROM is that RAM allows reading and writing while ROM only reads.
   SSD (Solid State Drives)| ![SSD](img/SSD.png)| These are storage drives that are smaller and faster than hard disk drives.
   HDD (Hard Disk Drives| ![HDD](img/HDD.png)| Non-volatile data storage device. Non-volatile means that the data is maintained even when the storage device is switched off.
   Bus |![Bus](img/Bus.png)| These are used to send control signals and data between the processor and other components.

   ## Scratch

   ![Flowchart](img/scratch.drawio.png)
   
   # Week4
   
   ## Python
   
  Properties:
  1. High-level: Python is a very high-level programming language because its syntax so closely resembles the English language. High-level means it is more readible to people. 
  2. General purpose: It is not designed only for a specific purpose, for example: SQL is strictly for handling databases.
  3. Dynamic: Dynamic languages are those whose variables can take on any type at runtime, and usually can even hold multiple values of different types over their lifespan.
  
  Programming concepts:
  1. Variable: Used to store data. Unlike other languages, python can read data type without user specifying data type during variable creation. Eg:
  a= 'abc' -> already registered as string.
  2. If statements: These are used to dictate the output based on different conditions. If condition met -> outcome A, else -> outcome B. If 'And' is used, all the conditions must be met to return true. If 'Or' is used, at least one condition should be met to return true.
  3. Loops: These run until a specified condition is met. For loop differs from while loop in that the intialisation and incrementation happens atthe beginning of the loop.
  4. Functions: This is a block of code that is used to perform a task and can be used multiple times as long as it is called in the code. There are two types: One that requires input during the call and those that do not need inputs (variables) when called.

Duties for the week:
1. Watched tutorials on the Kartoza Intern site.
2. Completed the EMC testing exercise for R1-R7.
3. Signed up for an online python platform (Edabit) that allows user to take on different challenges with different levels of difficulty and get points for solving the python challenges. This will help me get used to the syntax of python and train my mind to think a certain way when I code.


# Week 5

Additional python concepts and tips:
1. When slicing, the outter boundary is an exclusive boundary. E.g: a=[1,2,3] so a[0:2] returns [1,2].
2. {} for sets (removes duplicates), [] for array, () for list
3. When you have variables and methods, class is recommended. 

PostgreSQL notes:

![DB](img/Database.png) 
