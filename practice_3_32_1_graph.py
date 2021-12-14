from pythonds.basic import Queue
from collections import defaultdict
from time import time


class Vertex:

    def __init__(self, key, value=None) -> None:
        self.key = key
        self.value = value
        self.adjacents = {}

        self.color = "white"
        self.prev_vertex = None

    def add_adjacents(self, adj, weight: int = 0):
        self.adjacents[adj] = weight

    def get_adjacents(self):
        return self.adjacents.keys()

    def get_weight(self, adj):
        return self.adjacents.get(adj)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def set_prev_vertex(self, prev_vertex):
        self.prev_vertex = prev_vertex

    def __repr__(self):
        return f"{self.key}: {[adj.key for adj in self.adjacents]}"


class Graph:
    def __init__(self):
        self.vertexes = {}
        self.graph_size = 0
        self.start_vertex = None

    def add_vertex(self, key, value=None) -> Vertex:
        self.vertexes[key] = Vertex(key, value)
        self.graph_size += 1
        return self.vertexes[key]

    def add_edge(self, sv: str, dv: str, weight: int = 0):
        if sv in self.vertexes and dv in self.vertexes:
            self.vertexes[sv].add_adjacents(self.vertexes[dv], weight)
        else:
            raise IndexError(f"Error")

    def get_vertex(self, key):
        return self.vertexes.get(key)

    def get_vertexes(self):
        return [val for val in self.vertexes.values()]

    def set_start_vertex(self, key):
        self.start_vertex = key

    def bfs(self):
        if self.start_vertex:
            q = Queue()
            q.enqueue(self.vertexes[self.start_vertex])

            while not q.isEmpty():
                curr_v = q.dequeue()
                curr_v.set_color("grey")
                for adj in curr_v.adjacents:
                    if adj.color == "white":
                        adj.set_color("grey")
                        adj.set_prev_vertex(curr_v)
                        q.enqueue(adj)
                curr_v.set_color("black")
        else:
            raise IndexErrore("start vertex was not set")

    def traverese_bfs(self, ver):
        if ver in self.vertexes and self.start_vertex:
            ver = self.vertexes[ver]
            while ver.prev_vertex:
                print(ver.key)
                ver = ver.prev_vertex
            print(self.vertexes[self.start_vertex].key)

    def creation_dict_from_file(self, file_name: str):
        with open(f'{file_name}.txt') as file_:
            text = file_.read()
        list_words = text.split()
        dict_comb = defaultdict(list)

        # list_c = [0, 1, 2, 3]
        for j in list_words:
            self.add_vertex(j)
            for i in range(len(j)):

                key = j[:i] + "_" + j[i+1:]

                if key in dict_comb:
                    continue

                for word in list_words:
                    word_r = word[:i] + "_" + word[i+1:]
                    if key == word_r:
                        dict_comb[key].append(word)

                if len(dict_comb[key]) == 1:
                    dict_comb.pop(key)
        return dict_comb

    def build_graph_from_file(self, file_name: str):
        dict_key_word = self.creation_dict_from_file(file_name)
        print(dict_key_word)
        for list_comb_word in dict_key_word.values():
            star_ind = 1
            for j in list_comb_word:
                for h in list_comb_word[star_ind:]:
                    self.add_edge(j, h)
                    self.add_edge(h, j)
                star_ind += 1

    def __contains__(self, key):
        return key in self.vertexes

    def __iter__(self):
        return iter(self.vertexes.values())


start_t = time()
g = Graph()

# for i in range(1, 11):
#     g.add_vertex(i)
#
# g.add_edge(1, 3)
# g.add_edge(1, 5)
# g.add_edge(3, 1)
# g.add_edge(2, 3)
# g.add_edge(2, 4)

g.build_graph_from_file("text")

g.set_start_vertex("OWLS")
g.bfs()
g.traverese_bfs("CATS")
# for el in g.get_vertexes():
#     print(el)
print(time() - start_t)
# print(g.get_vertexes())
