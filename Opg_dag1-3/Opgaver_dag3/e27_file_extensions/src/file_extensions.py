def file_extensions(filename):
    no_extension = []
    with_extension = {}
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '.' in line:
                base, ext = line.rsplit('.', 1)
                if ext not in with_extension:
                    with_extension[ext] = [line]
                else:
                    with_extension[ext].append(line)
            else:
                no_extension.append(line)
    
    return (no_extension, with_extension)

def main():
    no_ext, ext_dict = file_extensions("src/filenames.txt")
    print(f"{len(no_ext)} files with no extension")
    for ext in sorted(ext_dict.keys()):
        print(f"{ext} {len(ext_dict[ext])}")

if __name__ == "__main__":
    main()
