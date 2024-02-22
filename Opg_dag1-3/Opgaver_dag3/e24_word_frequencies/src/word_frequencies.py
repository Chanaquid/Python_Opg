def word_frequencies(filename):
    freqs = {}
    
    strip_chars = """!"#$%&'()*,-./:;?@[]_"""
    
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                cleaned_word = word.strip(strip_chars).lower()
                if cleaned_word:
                    freqs[cleaned_word] = freqs.get(cleaned_word, 0) + 1   
    return freqs

def main():
    filename = "src/alice.txt"
    frequencies = word_frequencies(filename)
    
    for word, count in sorted(frequencies.items()):
        print(f"{word}\t{count}")

if __name__ == "__main__":
    main()
