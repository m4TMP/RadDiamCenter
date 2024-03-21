class GraphUnOriented:
    def __init__(self, vertex):
        self.data = [set() for b in ' ' * vertex]

    def addEdge(self, a, b):
        self.data[a].add(b)
        self.data[b].add(a)

    def find_shortest_path_length(self, start, end):
        if start >= len(self.data) or end >= len(self.data):
            return -1

        queue = [(start, 0)]
        visited = set()

        while queue:
            current_vertex, distance = queue.pop(0)

            if current_vertex == end:
                return distance

            if current_vertex not in visited:
                visited.add(current_vertex)

                for neighbor in self.data[current_vertex]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))

        return -1


inp = """
1 -- 2
2 -- 3
3 -- 4
3 -- 5
3 -- 6
6 -- 7
3 -- 8
1 -- 9
9 -- 10
1 -- 11
11 -- 12
12 -- 13
13 -- 14
12 -- 15
14 16
15 17
8 18
4 19
5 20
7 21
""".replace(' -- ', ' ')

edges = [b.split() for b in inp.split('\n') if b]
# vertexNames = sorted(set(inp.replace(' ', '').replace('\n', '')))
vertexNames = sorted(set([b1 for b1 in [b.strip() for b in inp.replace('\n', ' ').split(' ')] if b1]))

print('vertexNames', vertexNames)

print(edges)
print(len(edges))
print(vertexNames)
print(len(vertexNames))

g = GraphUnOriented(len(vertexNames))

for edge in edges:
    g.addEdge(vertexNames.index(edge[0]), vertexNames.index(edge[1]))

r = -1
d = -1
c = {}

print('  ' + ' '.join([f'{b:>2}' for b in vertexNames]) + '   e', end='')
print('   ' * 2 + '  ' + ' '.join([f'{b:>2}' for b in vertexNames]))
for a in vertexNames:
    print(a, end=' ')
    e = 0
    for b in vertexNames:
        if a == b:
            print('   ', end='')
        else:
            dist = g.find_shortest_path_length(vertexNames.index(a), vertexNames.index(b))
            e = max(e, dist)
            if dist == -1:
                print(f'  ', end=' ')
            else:
                print(f'{dist:2}', end=' ')

    d = max(d, e)
    if r >= e or r == -1:
        r = e
        if str(e) in c.keys():
            c[str(e)].append(a)
        else:
            c[str(e)] = [a]

    print(' ', e, '   ' * 2 + f'{a}', end='')

    for b in vertexNames:
        if a == b:
            print('   ', end='')
        else:
            dist = g.find_shortest_path_length(vertexNames.index(a), vertexNames.index(b))
            if dist == 1:
                print(' 1 ', end='')
            else:
                print(' . ', end='')
    print()

print('\n')
print('rad   :', r)
print('dist  :', d)
print('center:', ', '.join(c[str(r)]))
