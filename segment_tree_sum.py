def segment_init(start, end, node):
    if start == end:
        tree[node] = a[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = segment_init(start, mid, node * 2) + segment_init(mid + 1, end, node * 2 + 1)
    return tree[node]

def segment_sum(start, end, node, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return segment_sum(start, mid, node * 2, left, right) + segment_sum(mid + 1, end, node * 2 + 1, left, right)

def segment_update(start, end, node, index, diff):
    if index < start or index > end:
        return
    
    tree[node] += diff
    if start == end:
        return

    mid = (start + end) // 2
    segment_update(start, mid, node * 2, index, diff)
    segment_update(mid + 1, end, node * 2 + 1, index, diff)