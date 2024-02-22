import re

def red_green_blue(filename="src/rgb.txt"):

    formatted_lines = []
    
    with open(filename, 'r') as file:
        next(file)
        
        pattern = re.compile(r'^\s*(\d+)\s+(\d+)\s+(\d+)\s+(.*?)\s*$')
        re.search(pattern, '0 0 0 black')
        for line in file:
            match = pattern.search(line)
            if match:
                r, g, b, name = match.groups()
                formatted_lines.append(f'{r}\t{g}\t{b}\t{name}')
                
    return formatted_lines


def main():
    colors = red_green_blue("src/rgb.txt")
    print(colors[0])

if __name__ == "__main__":
    main()
