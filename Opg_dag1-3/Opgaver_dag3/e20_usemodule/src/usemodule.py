try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    hypotenuse = triangle.hypothenuse(3, 4)
    print(hypotenuse)
    area = triangle.area(3, 4)
    print(area)

if __name__ == "__main__":
    main()
