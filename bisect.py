def bisect(arr, target): #lower_bound랑 동일 왜냐하면 등호조건이 들어가기 때문
    start, end = 0, len(arr)
    while start < end:
        mid = (start+end) // 2
        if target > arr[mid]:
            start = mid+1
        else:
            end = mid
    return end

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(bisect(arr, target))