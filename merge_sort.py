def merge_sort(start, end):

    if start < end:
        mid = (start + end) >> 1
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if s[a] <= s[b]:
                temp.append(s[a])
                a += 1
            else:
                temp.append(s[b])
                b += 1
            
        if a <= mid:
            temp = temp + s[a:mid + 1]
        if b <= end:
            temp = temp + s[b:end + 1]

        for i in range(len(temp)):
            s[start + i] = temp[i]
