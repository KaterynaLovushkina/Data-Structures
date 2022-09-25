import re

import numpy as np

from pr_queue import PriorityQueue

class Graph:

    def __init__(self,file,row,col ):
        matcher = re.compile("[A-Z]")
        list_weight = []
        self.matrix =[]
        try:
            with open(file, 'r') as f:
                for item in f.read():
                    if matcher.match(item):
                        list_weight.append(item)
            while list_weight != []:
                self.matrix.append(list_weight[:row])
                list_weight = list_weight[col:]
        finally:
           f.close()

    def flood_fill_dfs(self, x, y, old_color, new_color ,visited ={}):
        if x >= len(self.matrix) or y>=len(self.matrix) or x<0 or y<0:
           return
        if self.matrix[x][y] != old_color:
           return
        if (x,y) in visited:
           return
        visited[(x,y)] = True
        self.matrix[x][y] = new_color
        self.flood_fill_dfs(x + 1, y, old_color,new_color)
        self.flood_fill_dfs(x - 1, y, old_color, new_color)
        self.flood_fill_dfs(x, y + 1, old_color, new_color)
        self.flood_fill_dfs(x , y - 1, old_color, new_color)

    def flood_fill_bfs(self,x, y, old_color, new_color ,visited ={}):
        qu = PriorityQueue()
        qu.push(x,y)
        visited[(x,y)] = True

        while qu.size != 0:
            cord_x, cord_y= qu.pop()
            self.matrix[cord_x][cord_y] = new_color
            if  self.is_valid(cord_x + 1,cord_y) :
                if self.matrix[cord_x + 1][cord_y] == old_color and (cord_x + 1, cord_y) not in visited:
                    visited[(cord_x + 1, cord_y)] = True
                    qu.push(cord_x + 1, cord_y)
            if self.is_valid(cord_x - 1, cord_y):
                if self.matrix[cord_x - 1][cord_y] == old_color and (cord_x - 1, cord_y) not in visited:
                    visited[(cord_x - 1, cord_y)] = True
                    qu.push(cord_x - 1, cord_y)
            if self.is_valid(cord_x, cord_y +1):
                 if self.matrix[cord_x][cord_y + 1] == old_color and (cord_x, cord_y + 1) not in visited:
                    visited[(cord_x, cord_y + 1)] = True
                    qu.push(cord_x, cord_y + 1)
            if self.is_valid(cord_x, cord_y-1):
                if self.matrix[cord_x][cord_y - 1] == old_color and (cord_x, cord_y - 1) not in visited:
                    visited[(cord_x, cord_y - 1)] = True
                    qu.push(cord_x, cord_y - 1)

        self.store_in_new_file('outfile.txt')


    def is_valid(self,x,y):
        if x >= len(self.matrix) or y >= len(self.matrix) or x <0 or y <0:
            return False
        else:
            return True

    def print_graph(self):
        for row in self.matrix:
            for element in row:
                print("{:2}".format(element), end=' ')
            print()
        print()

    def store_in_new_file(self, output_file):
        matrix = np.array(self.matrix)
        # file =open(output_file, 'w+')
        # file.write(str(matrix))
        with open(output_file, 'w+') as f:
            f.write(np.array2string(matrix, separator=', '))


if __name__ == '__main__':
    graph = Graph('input.txt', 10, 10)
    graph.print_graph()
    print()
    graph.flood_fill_bfs(1,7,'X','O')
    graph.flood_fill_bfs(3, 0, 'W', 'L')
    graph.print_graph()
