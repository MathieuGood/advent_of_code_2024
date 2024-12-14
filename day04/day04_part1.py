import csv
import re


word_matrix: list[str] = []
with open("day04_data.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        word_matrix.append(row)

word_matrix = [
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

word_matrix = [
    "AXXXX",
    "XTXXX",
    "XXIXX",
    "XXXCX",
    "XXXXA",
]


def build_word_matrix_col(word_matrix: list[str]) -> list[str]:
    word_matrix_col: list[str] = []
    for i in range(len(word_matrix)):
        col_string = ""
        for j in range(len(word_matrix[i])):
            print(j, word_matrix[j][i])
            col_string += word_matrix[j][i]
        word_matrix_col.append(col_string)

    print("Rows :", len(word_matrix))
    print("Cols :", len(word_matrix_col))
    return word_matrix_col


def get_word_matrix_size(matrix: list[str]) -> tuple[int, int]:
    return (len(matrix[0]), len(matrix))


def is_inside_matrix_bounds(matrix, row_index: int, col_index: int) -> bool:
    max_row_index, max_col_index = get_word_matrix_size(matrix)
    print(f"Checking if {row_index} and {col_index} are inside matrix bounds")
    return 0 <= row_index < max_row_index and 0 <= col_index < max_col_index


def build_word_matrix_diag(word_matrix: list[str]) -> list[str]:
    word_matrix_diag: list[str] = []
    for row_index in range(len(word_matrix)):
        for col_index in range(len(word_matrix[0])):
            diagonal_string: str = word_matrix[row_index][col_index]
            diag_cell_row_index = row_index + 1
            diag_cell_col_index = col_index + 1
            while is_inside_matrix_bounds(
                word_matrix, diag_cell_row_index, diag_cell_col_index
            ):
                diagonal_string += word_matrix[diag_cell_row_index][diag_cell_col_index]
                print(f"{diagonal_string}")
                diag_cell_row_index += 1
                diag_cell_col_index += 1
            word_matrix_diag.append(diagonal_string)
            print(f"While loop ended with output_string = {diagonal_string}")
            return word_matrix_diag


word_matrix_diag = build_word_matrix_diag(word_matrix)
word_matrix_col = build_word_matrix_col(word_matrix)


word_matrix.extend(word_matrix_col)
print("Max length :", len(word_matrix))
for one in word_matrix:
    print(one)


# Build matrix with :
#  -> Rows (ok)
#  -> Cols (ok)
#  -> Diagonals (TODO)

# Find occurences in each line of each matrix :
#  -> Reading left to right
#  -> Reading right to left (TODO : Reverse characters in a string)


word_occurences = 0
for row in word_matrix:
    word_occurences += len(re.findall("XMAS", row))

print(word_occurences)
