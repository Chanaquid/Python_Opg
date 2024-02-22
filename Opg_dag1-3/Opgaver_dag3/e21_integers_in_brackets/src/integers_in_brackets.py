import re

def integers_in_brackets(s):
    pattern = r'\[\s*([+-]?\d+)\s*\]'
    matches = re.findall(pattern, s)
    
    return [int(match) for match in matches]

def main():
    print(integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()
