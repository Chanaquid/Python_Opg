def reverse_dictionary(d):
    #return {v: k for k, vs in d.items() for v in vs}
    reversed = {}
    for k, vs in d.items():
        for v in vs:
            if v in reversed:
                reversed[v].append(k)
            else:
                reversed[v] = [k]
    return reversed

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
