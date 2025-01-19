# Project 1: Search in Pac-Man

<p align="center">
    <img alt="Pacman Maze" src="images/pacman-large-search.gif" width="400px">
    </br>
    All those colored walls,</br>
    Mazes give Pac-Man the blues,</br>
    So teach them to search.
</p>

## Introduction

In this project, your Pac-Man agent will find paths through their maze world,
both to reach a particular location and to collect food efficiently.
You will build general search algorithms and apply them to different Pac-Man scenarios.

The code for this project consists of several Python files,
some of which you will need to read and understand in order to complete the assignment, and some you can glance over.

### Submission

You will fill in portions of
[`pacai/student/search.py`](https://github.com/linqs/pacman/blob/main/pacai/student/search.py)
and [`pacai/student/searchagents.py`](https://github.com/linqs/pacman/blob/main/pacai/student/searchagents.py)
during this assignment.
You should **only** submit these two files.

For instructions on submission,
refer back to the [P0 README](../p0/README.md).
for example, you may submit with the command:
```sh
python3 -m autograder.run.submit pacai/student/search.py pacai/student/searchAgents.py
```

### Evaluation

Your code will be autograded for technical correctness.
Please _do not_ change the names of any provided functions or classes within the code,
or you will wreak havoc on the autograder (and points will be deducted!).
However, you are allowed to add any new classes or function that you need.
The correctness of your implementation -- not the autograder's output -- will be the final judge of your score.
If necessary, we will review and grade assignments individually to ensure that you receive due credit for your work.
This assignment is graded out of 25 points.
20 points will be for correctness as determined by the autograder and the point system given below for each problem.
5 points will be for style, which the autograder will also check.
You can run the style checker using the `run_style.sh` script in the project root.

### Academic Dishonesty

We will be checking your code against other submissions in the class for logical redundancy.
If you copy someone else's code and submit it with minor changes, we will know.
These cheat detectors are quite hard to fool, so please don't try.
We trust you all to submit your own work only; _please_ don't let us down.
If you do, we will pursue the strongest consequences available to us.

### Getting Help

You are not alone!
If you find yourself stuck on something, contact the course staff for help.
Office hours, section, and Piazza are there for your support; please use them.
If you can't make our office hours, let us know and we will schedule more.
We want these projects to be rewarding and instructional, not frustrating and demoralizing.
But, we don't know when or how to help unless you ask.
One more piece of advice: if you don't know what a variable does or what kind of values it takes, print it out.

### Code

All the code for this (and later projects) is available in this repository:
[https://github.com/linqs/pacman](https://github.com/linqs/pacman).
The only files you should edit are located in the
[pacai.student](https://linqs.github.io/pacman/docs/latest/pacai/student/index.html) package.
You should **not** use any third-party libraries,
but the [Python Standard Library](https://docs.python.org/3/library/) is fair-game.
If a bug is found in the code (non-student) code,
then the class will be alerted and you will have to pull the changes from this repository.

Any commands provided throughout these instructions are to be executed from the project root directory
(the one with the `README.md` and `LICENSE.md` files).

There are many files that will be used throughout this quarter-long project.
Below are a few that you should focus on for this assignment.

- Agents
  - [pacai.agents.base.BaseAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/base.html#pacai.agents.base.BaseAgent)
  - [pacai.agents.search.base.SearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/base.html#pacai.agents.search.base.SearchAgent)
- Actions / Directions
  - [pacai.core.directions.Directions](https://linqs.github.io/pacman/docs/latest/pacai/core/directions.html#pacai.core.directions.Directions)
  - [pacai.core.actions.Actions](https://linqs.github.io/pacman/docs/latest/pacai/core/actions.html#pacai.core.actions.Actions)
- States
  - [pacai.core.gamestate.AbstractGamestate](https://linqs.github.io/pacman/docs/latest/pacai/core/gamestate.html#pacai.core.gamestate.AbstractGameState)
  - [pacai.bin.pacman.PacmanGameState](https://linqs.github.io/pacman/docs/latest/pacai/bin/pacman.html#pacai.bin.pacman.PacmanGameState)
  - [pacai.core.agentstate.AgentState](https://linqs.github.io/pacman/docs/latest/pacai/core/agentstate.html#pacai.core.agentstate.AgentState)
- Search
  - [pacai.core.search.problem.SearchProblem](https://linqs.github.io/pacman/docs/latest/pacai/core/search/problem.html#pacai.core.search.problem.SearchProblem)
  - [pacai.core.search.position.PositionSearchProblem](https://linqs.github.io/pacman/docs/latest/pacai/core/search/position.html#pacai.core.search.position.PositionSearchProblem)
  - [pacai.core.search.food.FoodSearchProblem](https://linqs.github.io/pacman/docs/latest/pacai/core/search/food.html#pacai.core.search.food.FoodSearchProblem)
- Data Structures
  - [pacai.util.stack](https://linqs.github.io/pacman/docs/latest/pacai/util/stack.html)
  - [pacai.util.queue](https://linqs.github.io/pacman/docs/latest/pacai/util/queue.html)
  - [pacai.util.priorityQueue](https://linqs.github.io/pacman/docs/latest/pacai/util/priorityQueue.html)

## Welcome to Pac-Man

Welcome to Pac-Man's world, wakka wakka!

Let's jump right into the assignment and play a game with Pac-man!
To begin a game of Pac-Man, use the following command:
```sh
python3 -m pacai.bin.pacman
```

Pac-Man lives in a shiny blue world of twisting corridors and tasty round treats.
Navigating this world efficiently will be Pac-Man's first step in mastering their domain.
Play a quick game and hopefully... Pac-Man emerges victorious!
Lets try and continue this trend of victories throughout the rest of the quarter.

### First Agent

Since we won't always have direct control over Pac-Man,
let's start working with agents that will control them for us.
The simplest agent, [GoWestAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/gowest.html#pacai.agents.gowest.GoWestAgent),
which always goes West (a trivial reflex agent).

Surprisingly, this agent can occasionally win:
```sh
python3 -m pacai.bin.pacman --layout testMaze --pacman GoWestAgent
```

But, things get ugly for this agent when turning is required:
```sh
python3 -m pacai.bin.pacman --layout tinyMaze --pacman GoWestAgent
```

If (when) Pac-Man gets stuck, you can exit the game by typing CTRL-c into your terminal.
Soon, your agent will solve not only `tinyMaze`, but any maze you want.

Note that `pacai.bin.pacman` supports a number of options that can each be expressed in a long way (e.g., `--layout`) or a short way (e.g., `-l`).
You can see the list of all options and their default values via:
```sh
python3 -m pacai.bin.pacman --help
```

## Finding a Fixed Food Dot using Search Algorithms

The [SearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/base.html#pacai.agents.search.base.SearchAgent)
class plans out a path through Pac-Man's world and then executes that path step-by-step.
The search algorithms for formulating a plan are not implemented -- this is your job.
Before you begin your implementation test that the
[SearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/base.html#pacai.agents.search.base.SearchAgent)
is working correctly by running:
```sh
python3 -m pacai.bin.pacman --layout tinyMaze --pacman SearchAgent --agent-args fn=pacai.core.search.search.tinyMazeSearch
```

The command above tells the [SearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/base.html#pacai.agents.search.base.SearchAgent)
to use [tinyMazeSearch](https://linqs.github.io/pacman/docs/latest/pacai/core/search/search.html#pacai.core.search.search.tinyMazeSearch) as its search algorithm.
Pac-Man should navigate this maze successfully, however, will fail and even perform illegal actions on other layouts:
```sh
python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.core.search.search.tinyMazeSearch
```

This is because [tinyMazeSearch](https://linqs.github.io/pacman/docs/latest/pacai/core/search/search.html#pacai.core.search.search.tinyMazeSearch) is hand made, catered to tiny maze.
Therefore, [tinyMazeSearch](https://linqs.github.io/pacman/docs/latest/pacai/core/search/search.html#pacai.core.search.search.tinyMazeSearch) is not a generic search function and will not work on every maze.

With that in mind, it's time to write full-fledged generic search functions to help Pac-Man plan routes!
Pseudocode for the search algorithms you'll write can be found in the lecture slides and textbook.
Remember that a search node must contain not only a state but also the information necessary to reconstruct the path (plan) which gets to that state.

_Important note:_
All of your search functions need to return a list of _actions_ that will lead the agent from the start to the goal.
These actions all have to be legal moves (valid directions, no moving through walls).

_Hint:_
Each algorithm is very similar.
Algorithms for DFS, BFS, UCS, and A* differ only in the details of how the fringe is managed.
So, concentrate on getting DFS right and the rest should be relatively straightforward.
Indeed, one possible implementation requires only a single generic search method which is configured with an algorithm-specific queuing strategy.
(Your implementation need _not_ be of this form to receive full credit).

_Hint:_
You may find some of the following packages useful:
- [pacai.util.stack](https://linqs.github.io/pacman/docs/latest/pacai/util/stack.html),
- [pacai.util.queue](https://linqs.github.io/pacman/docs/latest/pacai/util/queue.html),
- [pacai.util.prioirtyQueue](https://linqs.github.io/pacman/docs/latest/pacai/util/priorityQueue.html).

### Question 1 (2 points)

Implement the depth-first search (DFS) algorithm in
[pacai.student.search.depthFirstSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.depthFirstSearch).
To make your algorithm _complete_, write the graph search version of DFS, which avoids expanding any already visited states (textbook section 3.5).

Your code should quickly find a solution for the three following mazes:

```sh
python3 -m pacai.bin.pacman --layout tinyMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch
```

```sh
python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch
```

```sh
python3 -m pacai.bin.pacman --layout bigMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch
```

The Pac-Man board will show an overlay of the states explored, and the order in which they were explored (deeper red means earlier exploration).
Is the exploration order what you would have expected?
Does Pac-Man actually go to all the explored squares on their way to the goal?

_Hint:_
If you use a [Stack](https://linqs.github.io/pacman/docs/latest/pacai/util/stack.html#pacai.util.stack.Stack) as your data structure,
the solution found by your DFS algorithm for `mediumMaze` should have a length of 130.
If you are getting 244, you probably pushed the successors onto the fringe in the reverse order provided by
[Actions.getSuccessor()](https://linqs.github.io/pacman/docs/latest/pacai/core/actions.html#pacai.core.actions.Actions.getSuccessor).
Is this a least cost solution?
If not, think about what depth-first search is doing wrong.

### Question 2 (1 point)

Implement the breadth-first search (BFS) algorithm in
[pacai.student.search.breadthFirstSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.breadthFirstSearch).
Again, write a graph search algorithm that avoids expanding any already visited states.
Test your code the same way you did for depth-first search.

```sh
python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.student.search.breadthFirstSearch
```

```sh
python3 -m pacai.bin.pacman --layout bigMaze --pacman SearchAgent --agent-args fn=pacai.student.search.breadthFirstSearch
```

Does BFS find a least cost solution?
If not, check your implementation.

_Hint:_
If Pac-Man moves too slowly for you, increase the fps with `--fps 50`.

_Note:_ If you've written your search code generically, your code should work equally well for the eight-puzzle search problem (textbook section 3.2) without any changes.

```sh
python3 -m pacai.bin.eightpuzzle
```

## Varying the Cost Function

While BFS will find a fewest-actions path to the goal, we might want to find paths that are "best" in other senses.
Consider `mediumDottedMaze` and `mediumScaryMaze`.
By changing the cost function, we can encourage Pac-Man to find different paths.
For example, we can charge more for dangerous steps in ghost-ridden areas or less for steps in food-rich areas,
and a rational Pac-Man agent should adjust its behavior in response.

### Question 3 (2 points)

Implement the uniform-cost graph search algorithm in
[pacai.student.search.uniformCostSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.uniformCostSearch).
You should now observe successful behavior in all three of the following layouts.
Here the agents are all UCS agents that differ only in the cost function they use (the agents and cost functions are written for you).

```sh
python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.student.search.uniformCostSearch
```

```sh
python3 -m pacai.bin.pacman --layout mediumDottedMaze --pacman StayEastSearchAgent
```

```sh
python3 -m pacai.bin.pacman --layout mediumScaryMaze --pacman StayWestSearchAgent
```

_Note:_
Both [StayEastSearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/staydirection.html#pacai.agents.search.staydirection.StayEastSearchAgent)
and [StayWestSearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/staydirection.html#pacai.agents.search.staydirection.StayWestSearchAgent)
use [uniformCostSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.uniformCostSearch).

_Note:_
You should get low and high path costs for [StayEastSearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/staydirection.html#pacai.agents.search.staydirection.StayEastSearchAgent)
and [StayWestSearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/staydirection.html#pacai.agents.search.staydirection.StayWestSearchAgent) respectively.
This is due to their exponential cost functions.

## A* search

### Question 4 (3 points)

Implement A* graph search algorithm in
[pacai.student.search.aStarSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.aStarSearch).
A* takes a heuristic function as an argument.
The heuristics function take two arguments: a state in the search problem (the main argument), and the problem itself (for reference information).
The [null heuristic](https://linqs.github.io/pacman/docs/latest/pacai/core/search/heuristic.html#pacai.core.search.heuristic.null) is a trivial example.

You can test your A* implementation on the original problem of finding a path through a maze to a fixed position using the Manhattan distance heuristic.
This heuristic is implemented for you already as
[pacai.core.search.heuristic.manhattan](https://linqs.github.io/pacman/docs/latest/pacai/core/search/heuristic.html#pacai.core.search.heuristic.manhattan).

```sh
python3 -m pacai.bin.pacman --layout bigMaze --pacman SearchAgent --agent-args fn=pacai.student.search.aStarSearch,heuristic=pacai.core.search.heuristic.manhattan
```

You should see that A* finds the optimal solution slightly faster than uniform cost search.
From around 619 nodes expanded to 538 nodes (ties in priority may vary output).
What happens on `openMaze` for the various search strategies?

## Finding All the Corners

The real power of A* will only be apparent with a more challenging search problem.
Now, it's time to formulate a new problem and design a heuristic for it.

In _corner mazes_, there are four dots, one in each corner.
Our new search problem is to find the shortest path through the maze that touches all four corners (whether the maze actually has food there or not).
Note that for some mazes like `tinyCorners`, the shortest path does not always go to the closest food first!
_Hint_: the shortest path through `tinyCorners` takes 28 steps.

### Question 5 (2 points)

Implement the search problem
[pacai.student.searchAgents.CornersProblem](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.CornersProblem).
You will need to choose a **state representation** that encodes all the information necessary to detect whether all four corners have been reached.
Now, your search agent should solve the following.

```sh
python3 -m pacai.bin.pacman --layout tinyCorners --pacman SearchAgent --agent-args fn=pacai.student.search.breadthFirstSearch,prob=pacai.student.searchAgents.CornersProblem
```

```sh
python3 -m pacai.bin.pacman --layout mediumCorners --pacman SearchAgent --agent-args fn=pacai.student.search.breadthFirstSearch,prob=pacai.student.searchAgents.CornersProblem
```

To receive full credit, you need to define an abstract state representation that _does not_ encode irrelevant information (like the position of ghosts, where extra food is, etc.).
In particular, do not use a Pac-Man [PacmanGameState](https://linqs.github.io/pacman/docs/latest/pacai/bin/pacman.html#pacai.bin.pacman.PacmanGameState) as a search state.
Your code will be very, very slow if you do (and also wrong).

_Hint:_
The only parts of the game state you need to reference in your implementation are the starting Pac-Man position and the location of the four corners.

Our implementation of [breadthFirstSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.breadthFirstSearch)
expands just under 2000 search nodes on `mediumCorners`.
However, heuristics (used with A* search) can reduce the amount of searching required.

### Question 6 (3 points)

Implement a heuristic for [CornersProblem](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.CornersProblem)
in [pacai.student.searchAgents.cornersHeuristic](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.cornersHeuristic).

To test your code run:
```sh
python3 -m pacai.bin.pacman --layout mediumCorners --pacman AStarCornersAgent
```

_Note:_
[pacai.core.search.corners.AStarCornersAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/corners.html#pacai.agents.search.corners.AStarCornersAgent)
is an agent that can accept command line arguments.

```sh
--pacman SearchAgent --agent-args fn=pacai.student.search.aStarSearch,prob=pacai.student.searchAgents.CornersProblem,heuristic=pacai.student.searchAgents.cornersHeuristic
```

Grading:
- 0 points for inadmissible heuristics.
- 1 point for **any** admissible heuristic.
- 2 points for expanding fewer than **1600** nodes.
- 3 points for expanding fewer than **1200** nodes.
- Expand fewer than **800**, and you're doing great!

_Hint:_
Remember, heuristic functions just return numbers, which, to be admissible,
must be lower bounds on the actual shortest path cost to the nearest goal.

## Eating All The Dots

Now we'll solve a hard search problem: eating all the Pac-Man food in as few steps as possible.
For this, a new search problem definition which formalizes the food-clearing problem can be found in
[pacai.core.search.food.FoodSearchProblem](https://linqs.github.io/pacman/docs/latest/pacai/core/search/food.html#pacai.core.search.food.FoodSearchProblem).
A solution is defined to be a path that collects all of the food in the Pac-Man world.

For the present project, solutions do not take into account any ghosts or power pellets.
They only depend on the placement of walls, regular food, and Pac-Man.
Of course ghosts can ruin the execution of a solution!
We'll get to that in the next project :)
If you have written your general search methods correctly,
[aStarSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.aStarSearch) with a null heuristic (equivalent to uniform-cost search)
should quickly find an optimal solution to `testSearch` with no code change on your part (total cost of 7).

```sh
python3 -m pacai.bin.pacman --layout testSearch --pacman AStarFoodSearchAgent
```

_Note:_
[AStarFoodSearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/agents/search/foodsearch.html#pacai.agents.search.foodsearch.AStarFoodSearchAgent)
is an agent with these command line arguments:
```sh
--pacman SearchAgent --agent-args fn=pacai.student.search.aStarSearch,prob=pacai.core.search.food.FoodSearchProblem,heuristic=pacai.student.searchAgents.foodHeuristic
```

You should find that [uniformCostSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.uniformCostSearch)
starts to slow down even for the seemingly simple `tinySearch`.
As a reference, our implementation takes 1.2 seconds to find a path of length 27 after expanding 4847 search nodes.

### Question 7 (5 points)

Implement a heuristic for [FoodSearchProblem](https://linqs.github.io/pacman/docs/latest/pacai/core/search/food.html#pacai.core.search.food.FoodSearchProblem)
in [pacai.student.searchAgents.foodHeuristic](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.foodHeuristic).

Try your agent on `trickySearch`:
```sh
python3 -m pacai.bin.pacman --layout trickySearch --pacman AStarFoodSearchAgent
```

Our [uniformCostSearch](https://linqs.github.io/pacman/docs/latest/pacai/student/search.html#pacai.student.search.uniformCostSearch)
agent finds the optimal solution in about 8.5 seconds, exploring over 16,000 nodes.
If your heuristic is admissible, you will receive the following score, depending on how many nodes your heuristic expands.

Grading:
- 0 points for inadmissible heuristics.
- 1 point for expanding fewer than **15000** nodes (very easy).
- 2 points for expanding fewer than **12000** nodes (easy).
- 3 points for expanding fewer than **9000** nodes (medium).
- 4 points for expanding fewer than **7000** nodes (hard).

Think through admissibility carefully, as inadmissible heuristics may manage to produce fast searches and even optimal paths.
Can you solve `mediumSearch` in a short time?
If so, we're either very, very impressed, or your heuristic is inadmissible.

### Admissibility vs. Consistency?

Technically, admissibility isn't enough to guarantee correctness in graph search -- you need the stronger condition of consistency.
For a heuristic to be consistent, it must hold that if an action has cost _c_, then taking that action can only cause a drop in heuristic of at most _c_.
If your heuristic is not only admissible, but also consistent, you will receive **1 additional point** for this question.

Almost always, admissible heuristics are also consistent, especially if they are derived from problem relaxations.
Therefore, it is probably easiest to start out by brainstorming admissible heuristics.
Once you have an admissible heuristic that works well, you can check whether it is indeed consistent, too.
Inconsistency can sometimes be detected by verifying that your returned solutions are non-decreasing in f-value.
Moreover, if UCS and A* ever return paths of different lengths, your heuristic is inconsistent.
This stuff is tricky.
If you need help, don't hesitate to ask the TAs!

## Suboptimal Search

Sometimes, even with A* and a good heuristic, finding the optimal path through all the dots is hard.
In these cases, we'd still like to find a reasonably good path, quickly.
In this section, you'll write an agent that always eats the closest dot.

### Question 8 (2 points)

Implement the function
[pacai.student.searchAgents.ClosestDotSearchAgent.findPathToClosestDot](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.ClosestDotSearchAgent.findPathToClosestDot).

Our agent solves this maze (suboptimally!) in under a second with a path cost of 350:
```sh
python3 -m pacai.bin.pacman --layout bigSearch --pacman ClosestDotSearchAgent
```

_Hint:_
The quickest way to complete [findPathToClosestDot](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.ClosestDotSearchAgent.findPathToClosestDot)
is to complete [pacai.student.searchAgents.AnyFoodSearchProblem](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.AnyFoodSearchProblem).
Then, solve that problem with an appropriate search function.
The solution should be very short!

Your [ClosestDotSearchAgent](https://linqs.github.io/pacman/docs/latest/pacai/student/searchAgents.html#pacai.student.searchAgents.ClosestDotSearchAgent)
won't always find the shortest possible path through the maze.
If you don't understand why, ask the TAs!
In fact, you can do better if you try.
