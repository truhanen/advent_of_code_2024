from collections import Counter
from pathlib import Path


def solve(values1: list[int], values2: list[int]) -> tuple[int, int]:
    distance_sum = sum(
        abs(value1 - value2) for value1, value2 in zip(sorted(values1), sorted(values2))
    )

    counts2 = Counter(values2)
    similarity_score = sum(
        value1 * counts2[value1] if value1 in counts2 else 0 for value1 in values1
    )

    return distance_sum, similarity_score


def main():
    input_data_path = Path(__file__).parent / "input_data" / "day01.txt"
    input_data = input_data_path.read_text()
    rows = input_data.split("\n")
    pairs = [tuple(int(v) for v in row.split("   ")) for row in rows]
    values1, values2 = zip(*pairs)

    distance_sum, similarity_score = solve(values1, values2)

    print(f"Distance sum: {distance_sum}\nSimilarity score: {similarity_score}")


if __name__ == "__main__":
    main()
