def parse_into_list(file):
    a = {}
    f = open(file, "r")
    for line in f:
        w = line.split()
        k = int(w[0])
        v = []
        for i in range(2, len(w)):
            v.append(int(w[i].strip(",")))
        a[k] = v
    return a

def walk(adj):
    color = [x for x in range(len(adj))]
    #done = False
    #while not done:
        #done = True
    for i in range(10000):
        for node in adj:
            for neighbor in adj[node]:
                color[node] = min(color[neighbor], color[node])
                color[neighbor] = min(color[neighbor], color[node])
    print(color)
    s = set(color)
    return len(s)



print(walk(parse_into_list("day12input.txt")))
