def main():
    for i in range(1,11):
        triple_calc = triple(i)
        square_calc = square(i)
        if square_calc > triple_calc:
            break
        else:
            print(f"triple({i})=={triple_calc} square({i})=={square_calc}")
            

def triple(x):
    return x * 3

def square(x):
    return x**2

if __name__ == "__main__":
    main()
