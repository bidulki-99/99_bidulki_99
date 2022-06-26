int z[1000001];

void z(string s) {
  int n = s.size();
    z[0] = n;
    for (int i = 1, l = 0, r = 0; i < n; i++) {
      if (i <= r)
        z[i] = min(r - i, z[i - l]);

      while (s[i + z[i]] == s[z[i]])
        z[i]++;

      if (i > r)
        l = i;	

      r = max(r, i + z[i] - 1);
    }
}
