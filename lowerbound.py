def lower_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start+end) // 2
        if target > arr[mid]:
            start = mid+1
        else:
            end = mid
    return end

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())
    print(lower_bound(arr, target))