from urllib.request import urlopen

INPUT_URL = "https://adventofcode.com/2024/day/1/input"

def main():
    data = urlopen(INPUT_URL)
    list1 = []
    list2 = []
    distance_sum = sum(abs(value1 - value2) for value1, value2 in zip(sorted(list1), sorted(list2)))
    return distance_sum

if __name__ == "__main__":
    main()
