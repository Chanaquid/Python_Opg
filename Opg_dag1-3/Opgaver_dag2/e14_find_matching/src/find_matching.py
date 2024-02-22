def find_matching(L, pattern):
    return [index for index, word in enumerate(L) if pattern in word]

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
