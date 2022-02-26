int mat[1111][1111];
int n, m;

int sum(int x, int y) {
    int ret = 0;
    for (int i = x; i > 0; i -= (i & -i))
        for (int j = y; j > 0; j -= (j & -j))
            ret += mat[i][j];
    return ret;
}

void update(int x, int y, int val) {
    for (int i = x; i <= n; i += (i & -i))
        for (int j = y; j <= n; j += (j & -j))
            mat[i][j] += val;
}

int main() {
     cin >> n >> m;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            int temp;
            cin >> temp;
            update(i, j, temp);
        }
}
