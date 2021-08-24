def upper_bound(arr, target):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start+end) // 2
        print(mid, arr[mid])
        if target >= arr[mid]:
            start = mid + 1
        else:
            end = mid
    return end

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(upper_bound(arr, target))