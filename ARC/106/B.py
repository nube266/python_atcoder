def connected_components(graph):
    seen = set()

    def component(n):
        nodes = set([n])
        while nodes:
            n = nodes.pop()
            seen.add(n)
            nodes |= set(graph[n]) - seen
            yield n
    for n in graph:
        if n not in seen:
            yield component(n)


def create_sub_graph(gen):
    return [list(x) for x in gen]


N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

graph = {}
for i in range(1, N + 1):
    graph[i] = []

for i in range(M):
    c, d = map(int, input().split())
    tmp = graph[c]
    tmp.append(d)
    graph[c] = tmp
    tmp = graph[d]
    tmp.append(c)
    graph[d] = tmp

sub_graphs = create_sub_graph(connected_components(graph))

for sub_graph in sub_graphs:
    sum1 = 0
    sum2 = 0
    for node in sub_graph:
        sum1 += a[node - 1]
        sum2 += b[node - 1]
    if sum1 != sum2:
        print("No")
        exit()
print("Yes")
