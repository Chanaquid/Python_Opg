def transform(s1, s2):
    
    l1 = list(map(int, s1.split()))
    l2 = list(map(int, s2.split()))
    
    l3 = zip(l1, l2)
    return [a * b for a, b in l3]

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
