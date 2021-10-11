# 🛣️ Shortest Path Finding Visualizer

`Shortest Path Finding Visualizer` is the simple window application, which visualizes the shortest path between two squares on the grid.

# 📜 Table of contents
* [About The Project](#about-the-project)
* [Visualization example](#visualization)
* [Installation](#installation)
* [Usage](#usage)
* [Technologies](#technologies)
* [License](#license)


<h1 id="about-the-project"> 📘 About The Project </h1>
The player sets the start and end of the path, moreover it can build walls to make the path to the goal more difficult and after the player selects the algorithm, application starts to visualize the shortest path from the start to the end.

## Implemented algorithms:
- <strong>BFS
- Dijkstra
- Bellman-Ford
- A*</strong>

In BFS and A* algorithms distance from each square to adjacent squares is 1.

<p> In Dijkstra's algorithm for each square a number between 0 and 40 is drawn. To move to some square B from any adjacent square A the distance of drawn number from B square must be covered.</p>

<p> In Bellman-Ford algorithm there is exactly the same mechanism as in Dijkstra's algorithm, but the numbers are drown from [-6, 999].
There is a chance that the negative cycle will occure. In that case there is no shortest path and the map will reset to its initital state. </p>

## Why did I build this project?
I did the Shortest Path Finding Visualizer project to get to know better the most popular and probably the most useful algorithms of finding the shortest paths.

<h1 id="visualization"> 📈 Visualization example </h1>
The following visalization shows <strong>A* algorithm</strong> during the proccess of finding the shortest path.
<p>Want to see other algorithms running? Install the app and try it for yourself!</p>

![A_star](https://user-images.githubusercontent.com/67509491/136714105-2d5445c6-c317-430d-a419-0c0081261867.gif)


<h1 id="installation"> 🔧 Installation </h1>
To run visualization app you need to have <strong>Pygame</strong> and <strong>Pygame GUI</strong> installed.

<p>If you don't have it installed, open command prompt and enter the following commands.</p>

```bash
pip install pygame
```

```bash
pip install pygame_gui
```

<p>Now, you have all required modules to run visualizer. Just download the repository, open your command prompt in the repository and <strong>run main.py</strong> by typing:</p>

```bash
python main.py
```

<h1 id="usage"> 📋 Usage </h1>

1. Choose squares for the start and end of the path, then left-click on these squares to apply changes. The start and end squares should change their colors to yellow and purple.

2.  Left-click the square, on which you want to build the wall. (The start and end squares must be chosen).

3. Select the algorithm you want to see running and hit the appropriate button.

4. Reset the map to its initial state by clicking the <strong>RESET button</strong>.

5. Return to first bullet point and visualize again or quit the application.


<h1 id="technologies"> 👨‍💻 Technologies </h1>

Project is created with:
- **Python**: version 3.8.8
- **Pygame**: version 2.0.2
- **Pygame GUI** : version 0.5.7

<h1 id ="license"> ⚖️ License </h1>

![GitHub](https://img.shields.io/github/license/CN-28/Shortest-Path-Finding-Visualizer)
