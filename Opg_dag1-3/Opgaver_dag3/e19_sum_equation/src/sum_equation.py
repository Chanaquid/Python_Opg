def sum_equation(L):
    
    if not L:
        return "0 = 0"
    equation = " + ".join(str(i) for i in L) + f" = {sum(L)}"
    return equation

def main():
    print(sum_equation([1, 5, 7]))

if __name__ == "__main__":
    main()
