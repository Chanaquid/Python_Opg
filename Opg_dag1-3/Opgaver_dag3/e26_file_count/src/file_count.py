import sys

def file_count(filename):
    line_count = 0
    word_count = 0
    char_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)
    
    return (line_count, word_count, char_count)

def main():
    for filename in sys.argv[1:]:
        line_count, word_count, char_count = file_count(filename)
        print(f"{line_count}\t{word_count}\t{char_count}\t{filename}")

if __name__ == "__main__":
    main()
