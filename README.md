# Rubik's Cube Solver

## Overview
This project provides tools for solving the Rubik's Cube using different algorithms.

Supported Algorithms:
1. __Breadth-First Search (BFS):__
* Returns the goal state of the cube using BFS.
* Displays the initial state of the cube, the moves applied, the related states to the moves, the number of nodes explored, and the time taken to find the solution.

2. __Iterative Deepening Search (IDS):__
* Returns the goal state of the cube using IDS.
* Displays the initial state of the cube, the current search depth, and the number of nodes explored at that depth.

3. __A star:__
* Utilizes the A* algorithm to determine the goal state of the cube, displaying the initial state, applied moves, and the associated state transformations for each move. The first presented state, post moves list, is the normalized version of the initial state.

## Requirements

* Python 3

## Modules

1. __goaltry.py:__
* Defines a set of moves for the Rubik's Cube and their corresponding transformations.

2. __RCSolver.py:__
* Contains the main logic for solving the Rubik's Cube using different algorithms.
* Introduces the cubesolver class and various methods for solving the cube.

## How to Run
Execute the run.sh script with two arguments. The exact nature of these arguments is determined by the RCSolver.py script.


Example:
```bash
./run.sh [initial_state] [algorithm_choice]
```
* Replace [initial_state] with the starting configuration of your Rubik's Cube.
* Replace [algorithm_choice] with the desired algorithm (bfs, ids, or astar).

Example:
```bash
./run.sh "WWRGBOYRWBGOYRGOBYWBRGO" "bfs"
```

This would solve the cube starting from the given initial state using the BFS algorithm.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
