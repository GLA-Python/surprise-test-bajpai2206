from pickle import FALSE


def expanding(lst):
    diff = lst[1]-lst[0]
    for i in range(2,len(lst)):
        if abs(lst[i] - lst[i-1])>diff:
            diff = abs(lst[i] - lst[i-1])
        else:
            return False
    return True

lst = list(map(int,input().split()))
out = expanding(lst)
print(out)
