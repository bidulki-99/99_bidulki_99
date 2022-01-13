def bellman_ford(graph, start):
    dist, pred = {}, {}
    for node in graph:
        dist[node] = float('inf')
        pred[node] = None
    dist[start] = 0

    for i in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if dist[neighbor] > dist[node] + graph[node][neighbor]:
                    dist[neighbor] = dist[node] + graph[node][neighbor]
                    pred[neighbor] = node

    for node in graph:
        for neighbor in graph[node]:
            if dist[neighbor] > dist[node] + graph[node][neighbor]:
                return -1

    return dist