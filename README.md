# AI-Agent-for-Optimal-Path-Finder
Optimal Path between two points taking altitude difference into account

Language: Python 3.7
Libraries: None

Brief Description:

** Negotiated over BFS,UCS and A* algorithm to elect the best for finding shortest path
** Instigated altitude difference threshold to restricts movements and depict output as a path through a grid

Project description:

In this project, we twist the problem of path planning a little bit just to give you the opportunity to deepen your understanding of search algorithms by modifying search techniques to fit the criteria of a realistic problem. To give you a realistic context for expanding your ideas about search algorithms, we invite you to take part in a Mars exploration mission. The goal of this mission is to send a sophisticated mobile lab to Mars to study the surface of the planet more closely. We are invited to develop an algorithm tofind the optimal path for navigation of the rover based on a particular objective. The input of our program includes a topographical map of the mission site, plus some information about intended landing site and target locations and some other quantities that control the quality of the solution. The surface of the planet can be imagined as a surface in a 3-dimensional space. A popular way to represent a surface in 3D space is using a mesh-grid with a Z value assigned to each cell that identifies the elevation of the planet at the location of the cell. At each cell, the rover can move to each of 8 possibleneighborcells: North, North-East, East, South-East, South, South-West, West, and North-West. Actions are assumed to be deterministic and error-free (the rover will always end up atthe intended neighborcell). The rover is not designed to climb across steep hills and thus moving to a neighboring cell which requires the rover to climb up or down a surface which is steeper than a particular threshold value is not allowed. This maximum slope (expressed as a difference in Z elevation between adjacent cells) will be given as aninput along with the topographical map.

Process:
Path Finder.py - RUn the code with a predefined path as input and choose the way you want the output as.
Problem Statement.pdf - Full rules set and description.
