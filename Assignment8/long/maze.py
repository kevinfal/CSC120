"""
    File: maze.py
    Author: Kevin Falconett
    Purpose: Provides class Maze that represents a maze
             
"""

class Maze:
    def __init__(self, edge_list):
        self._maze = self._build_maze(edge_list)


    
    def _build_maze(self, edge_list):
        
        returned = dict()

        for edges in edge_list:
            edge1 = edges[0]
            edge2 = edges[1]

            returned.setdefault(edge1,[]).append(edge2)
        
        return returned

    def solve(self, source, finish):
        if source == finish:
            return finish
        elif source not in self._maze:
            return None
        else:
            taken = [source]
            paths = self._maze[source]
            taken.extend(self.solve(paths[0], finish))
            return taken
                
            

            



def create_edge_list(filename):
    
    returned = []
    file = open(filename)
    for line in file:
        line = line.split()
        returned.append(line)
    return returned



def main():
    edges = create_edge_list("custom.txt")
    maze = Maze(edges)
    print(maze.solve('a','d'))

if __name__ == "__main__":
    main()