import sys
import math

def summary(filename):
    sum_numbers = 0.0
    numbers = []

    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line)
                sum_numbers += number
                numbers.append(number)
            except ValueError:
                continue

    n = len(numbers)
    if n == 0:
        return (0.0, 0.0, 0.0)  
    average = sum_numbers / n
    variance = sum((x - average) ** 2 for x in numbers) / (n - 1) if n > 1 else 0
    stddev = math.sqrt(variance)

    return (sum_numbers, average, stddev)

def main():
    for filename in sys.argv[1:]:
        sum_numbers, average, stddev = summary(filename)
        print(f"File: {filename} Sum: {sum_numbers:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")

if __name__ == "__main__":
    main()
