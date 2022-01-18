def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [i for i in range(n+1)]
edge = []
edge.sort()
result = 0

for i in edge:
    cost, x, y = i

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost
