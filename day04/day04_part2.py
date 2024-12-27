import csv
import re


word_matrix: list[str] = []
with open("day04_data.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        word_matrix.append(row[0])


test_word_matrix = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]


print(f"Matrix size : {len(word_matrix)} rows x {len(word_matrix[0])} cols")

# Function to check if a 3x3 matrix matches the XMAS pattern

# Loop over all 3x3 matrixes from the source word_matrix


def get_3by3_matrixes(word_matrix: list[str]) -> list[list[str]]:
    sub_matrixes = []
    for row_index in range(len(word_matrix) - 4):
        for col_index in range(len(word_matrix[0]) - 4):
            sub_matrix = [
                [
                    word_matrix[row_index][col_index],
                    word_matrix[row_index][col_index + 1],
                    word_matrix[row_index][col_index + 2],
                ],
                [
                    word_matrix[row_index + 1][col_index],
                    word_matrix[row_index + 1][col_index + 1],
                    word_matrix[row_index + 1][col_index + 2],
                ],
                [
                    word_matrix[row_index + 2][col_index],
                    word_matrix[row_index + 2][col_index + 1],
                    word_matrix[row_index + 2][col_index + 2],
                ],
            ]
            sub_matrixes.append(sub_matrix)
    return sub_matrixes


sub_matrixes = get_3by3_matrixes(test_word_matrix)

for matrix in sub_matrixes:
    for row in matrix:
        print(row)
    print("\n")
