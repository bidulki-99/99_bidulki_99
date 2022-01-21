dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if mat[i][j][k] == 1:
                queue.append([i, j, k])


def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and mat[nx][ny][nz] == 0:
                mat[nx][ny][nz] = mat[x][y][z] + 1
                queue.append([nx, ny, nz])
