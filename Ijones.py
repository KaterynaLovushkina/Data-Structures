from collections import defaultdict

from Stack import Stack
from Plate import Plate



class Ijones():
    def __init__(self,file_name_in,file_name_out):

        with open(file_name_in, 'r+') as f:
            lines = f.readlines()
            width, height = lines[0].split()
            self.grid = []
            self.dest = []
            self.height = int(height)
            self.width = int(width)

            for line in lines[1:]:
                self.grid.append(list(line.rstrip()))

        self.candidates = defaultdict(list)
        self.pathes = []
        self.file_name_out = file_name_out
        if self.width != 1:
            self.dest.append((0, self.width - 1))
        if self.width != 1 and self.height != 1:
            self.dest.append((self.height - 1, self.width - 1))


    def get_proper_plates(self,row_col:tuple):
        row,col = row_col
        if col == self.width-1:
            return []
        if (row,col) not in self.candidates.keys():
            for i in range(0, self.height):
                for j in range(col + 1, self.width):
                    if self.grid[i][j] == self.grid[row][col] or row == i and j == col + 1:
                        self.candidates[(row,col)].append((i, j))
        return self.candidates[(row,col)]

    def get_path(self,node):
        path=[]
        while node != None:
            path.append(node.value)
            node =node.parent
        reverse_path=path[::-1]
        return reverse_path


    def dfs(self,start_r,start_c):
        my_queue=Stack()
        node = Plate(self.grid[start_r][start_c], (start_r, start_c))
        my_queue.push(node)
        while my_queue.size != 0:
            queue_node= my_queue.pop()
            if queue_node.pos in self.dest:
                self.pathes.append(self.get_path(queue_node))
            else:
                for plate in self.get_proper_plates(queue_node.pos):
                    node = Plate(self.grid[plate[0]][plate[1]], plate, queue_node)
                    my_queue.push(node)

    def call_dfs(self):
        for i in range(self.height):
            self.dfs(i,0)
        for path in self.pathes:
            print(*path)
        count = len(self.pathes)
        Ijones.write_to_file(self.file_name_out,count)

    @staticmethod
    def write_to_file(file_name, count):
        file = open(file_name, 'w+')
        try:
            file.write("Count of pathes: ")
            file.write(str(count))
        finally:
            file.close()

if __name__ == '__main__':
    ijones = Ijones("resources/ijones1.in", "ijones.out")

    ijones.call_dfs()





