import csv


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


def get_3by3_matrixes(
    word_matrix: list[str],
) -> list[list[list[str], list[str], list[str]]]:
    sub_matrixes = []
    for row_index in range(len(word_matrix) - 2):
        for col_index in range(len(word_matrix[0]) - 2):
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


def is_xmas_3by3_matrix(matrix: list[list[str], list[str], list[str]]) -> bool:
    # Top left to bottom right diagonal
    diagonal1: str = matrix[0][0] + matrix[1][1] + matrix[2][2]
    # Top right to bottom left diagonal
    diagonal2: str = matrix[0][2] + matrix[1][1] + matrix[2][0]
    return is_mas_string(diagonal1) and is_mas_string(diagonal2)


def is_mas_string(mas_string: str) -> bool:
    return mas_string.upper() == "MAS" or mas_string[::-1].upper() == "MAS"


sub_matrixes = get_3by3_matrixes(word_matrix)

xmas_occurences = 0
for matrix in sub_matrixes:
    print(matrix)
    if is_xmas_3by3_matrix(matrix):
        xmas_occurences += 1

print(f"{xmas_occurences} occurences of XMAS in the matrix")