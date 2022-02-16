def solution(arr):
    sum = 0
    pre = 0
    for idx, a in enumerate(arr):

        idx = a.index(max(a))
        if idx == pre:
            a[idx] = 0
            idx = a.index(max(a))
        print(a)
        print(idx)
        sum += max(a)
        pre = idx

    return sum

print(solution([[1,2,3,5],[5,6,7,100],[4,3,2,1]]))