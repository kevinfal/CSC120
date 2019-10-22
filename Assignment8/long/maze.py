"""
    File: maze.py
    Author: Kevin Falconett
    Purpose: Provides class Maze that represents a maze
             the way the maze is represented is a dictionary
             with edges as keys and other edges it connects to as
             values
"""

class Maze:
    def __init__(self, edge_list):
        self._maze = self._build_maze(edge_list)
    
    def _build_maze(self, edge_list):
        """
        builds a "maze", constructs a dictionary with
        an edge as key and it's connecting edges as
        values
        :param edge_list: (List[][char]) list of lists with
                          [edge, connecting edge]
        :return: (dict) with edges as keys and their connecting
                 in arrays as values
        """
        returned = dict()
        for edges in edge_list:
            edge1 = edges[0]
            edge2 = edges[1]
            # if edge1 is not already in edges, will create []
            # and append, else it just appends
            returned.setdefault(edge1,[]).append(edge2)
        
        return returned

    def solve(self, source, finish):
        """
        solves the maze and returns the path
        that it took to get from source to
        finish
        :param source: (char) place to navigate from
        :param finish: (char) end destination to get to
        :return: (List[char]) of edges visited to get to finish
        """
        # if navigated to finish, or already at it
        if source == finish:
            return finish
        else:
            # if navigated to a dead end
            if source not in self._maze:
                return None
            else:
                taken = [source]
                paths = self._maze[source]  # all paths that source leads to
                for path in paths:
                    # if we haven't reached the end yet
                    if finish not in taken:
                        added = self.solve(path, finish)
                        # if path is not a dead end, then add to taken
                        if added is not None:
                            taken.extend(added)
                return taken


def create_edge_list(filename):
    """
    parses through a maze file and constructs
    a list[][char] of edges
    :param filename: (str) name of file
    :return: list[][char] of edges
    """
    returned = []
    file = open(filename)
    for line in file:
        line = line.split()
        # after splitting, line will be [edge1, edge2]
        returned.append(line)
    return returned



def main():
    """
    prompts user for file and solves the maze in the file
    :return:
    """
    try:
        edges = input("File: ")
        maze = Maze(edges)
        print(maze.solve('a','d'))
    except:
        print("invalid file")

if __name__ == "__main__":
    main()