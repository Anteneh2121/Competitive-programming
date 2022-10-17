def countSwaps(a):
    # Write your code here
    n = len(a)
    numSwaps = 0
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                swapped = True
                numSwaps+=1
                a[j], a[j+1] = a[j+1], a[j]
        if not swapped:
            break
    print(f'Array is sorted in {numSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
