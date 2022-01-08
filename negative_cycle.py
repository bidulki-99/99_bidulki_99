def bellman_ford(graph, start):
    dist = [0] * (N + 1)

    for i in range(N):
        for cur_node, next_node, cost in graph:
                if dist[cur_node] > dist[next_node] + cost:
                    dist[cur_node] = dist[next_node] + cost
                    if i == N - 1:
                        return 'YES'       
    return 'NO'