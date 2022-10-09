from priority_queue import PriorityQueue
import numpy as np

class Graph:

    def __init__(self, file_name):

        with open(file_name, 'r+') as f:
            lines = f.readlines()
            num_nodes, num_es = lines[0].split()
            self.adjacency_list = {node: set() for node in range(1, int(num_nodes) + 1)}

            self.clients = [int(client) for client in lines[1].split()]
            self.routes = [r for r in range(1, int(num_nodes) + 1) if r not in self.clients]
            print(self.routes)
            for line in lines[2:]:
                startnode, endnode, latency = (int(x) for x in line.split())
                self.add(startnode, endnode, latency)


    def add(self,startnode, endnode, latency):
        self.adjacency_list[startnode].add((endnode, latency))
        self.adjacency_list[endnode].add((startnode, latency))

    def dijikstra(self, start):
        node_table = {node : np.inf for node in range(1, len(self.adjacency_list)+1)}
        node_table[start] = 0
        visited = {}
        pr_que =PriorityQueue()
        pr_que.push(start, 0)
        while pr_que.size > 0:
            node = pr_que.pop()
            visited[node] = True
            for neighbor, weight in self.adjacency_list[node]:
                if neighbor not in visited:
                    old_dist = node_table[neighbor]
                    updated_dist = node_table[node] + weight
                    if updated_dist < old_dist:
                        node_table[neighbor] = updated_dist
                        if pr_que.find(neighbor, weight) is False:
                            pr_que.push(neighbor, updated_dist)

        return node_table

    def find_max_delay(self):

        list_max_delays = {}
        while len(self.routes) > 0:
            route = self.routes.pop()
            client_table = {key: value for key, value in self.dijikstra(route).items() if key in self.clients}
            print(route , ' : ', client_table)
            max_delay = max(client_table.values())
            list_max_delays[route] = max_delay

        min_delay = min(list_max_delays.values())
        server = list(list_max_delays.keys())[list(list_max_delays.values()).index(min_delay)]

        Graph.write_to_file('gamsrv.out',min_delay)
        return 'The best route for server : ', server


    @staticmethod
    def write_to_file(file_name, delay):
        file = open(file_name, 'w+')
        try:
           file.write(str(delay))
        finally:
            file.close()

    def print(self):
        for i in range(len(self.adjacency_list)):
            print(i+1, ' : ', self.adjacency_list[i+1])


if __name__ == '__main__':
    gr = Graph('gamsrv.in')
    gr.print()
    print()
    print(gr.find_max_delay())
