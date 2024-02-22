def merge(L1, L2):
    
    L = L1 + L2
    n = len(L)
    for i in range(n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

def main():
    print(merge([2, 6, 5], [4, 1, 3]))

if __name__ == "__main__":
    main()
