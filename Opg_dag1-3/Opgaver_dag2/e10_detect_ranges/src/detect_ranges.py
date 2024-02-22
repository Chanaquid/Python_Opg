def detect_ranges(L):
    sorted_L = sorted(L)
    
    result = []
    
    start = sorted_L[0]
    end = start
    
    for i in range(1, len(sorted_L)):
        if sorted_L[i] == sorted_L[i-1] + 1:
            end = sorted_L[i]
        else:
            if start != end:
                result.append((start, end + 1))
            else:
                result.append(start)
            start = sorted_L[i]
            end = start
    if start != end:
        result.append((start, end + 1))
    else:
        result.append(start)
    
    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
