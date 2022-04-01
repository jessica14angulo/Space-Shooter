# Space-Shooter

Space-Shooter is a game where you have to shoot/dodge the enemy spaceships using lasers. Can you dodge and destroy all the enemies with your laser before they reach you?

## Getting Started

Make sure you have Python 3.8.0 or newer and Pygame installed and running on your machine. You can install Pygame by opening a terminal and running the following command.
```
For Mac:
pip3 install pygame
For Windows:
pip install pygame
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 Space-Shooter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the Cycles folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Space-Shooter       (source code for game)
  +-- game              (specific game classes)
    +-- assets          (images for the game)
    +-- collide         (handles collisions)
    +-- enemy           (generates enemies)
    +-- laser           (creates lasers)
    +-- player          (player condition)
    +-- ship            (manages the player's shoots)
    +-- sounds          (manages the game sounds)
  +--constants          (constant values)
  +--main.py            (entry point for program)
+-- README.md           (general info)
```

## Required Technologies

* Python 3.8.0
* Pygame 2.1.2

## Rules

- The Player can move from left to right, and up and down.
- The Player tries to shoot so the opponent collides with its laser while avoid opposing laser shots.
- If an enemy collides with your laser it dies.
- If Player gets hit by the enemy's laser, it loses points on the ship's healthbar.
- If the healthbar runs out of green, YOU LOSE!
- If more than 5 enemies get to the end of the screen, YOU LOSE!
- If you kill all the enemy spaceships, you move on to the next level!

## Requirements

- The program must have a README file.
- The program may be any type of game or interactive simulation.
- The program should use classes and instances.
- The program should apply the four principles of programming with classes.
- The program should use the libraries chosen in the course.
- The program should be delivered through a version control system.
- The program should be able to be run from the command line.

## Team

Group name: team-01
- Aaron Bechtel    bechtel.aaron22@gmail.com
- Jared Malan    jared.malan7@gmail.com
- Jessica Angulo    jessica14angulo@gmail.com
- Oscar Peterson    pet21048@byui.edu

<img width="800" alt="Screen Shot 2022-03-30 at 10 07 13 PM" src="https://user-images.githubusercontent.com/94416292/160975459-8a200c3b-c3ec-4302-b21d-325177b3bd77.png">
