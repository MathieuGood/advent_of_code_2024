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


def build_word_matrix_col(word_matrix: list[str]) -> list[str]:
    word_matrix_col: list[str] = []
    for i in range(len(word_matrix)):
        col_string = ""
        for j in range(len(word_matrix[i])):
            col_string += word_matrix[j][i]
        word_matrix_col.append(col_string)
    return word_matrix_col


def get_word_matrix_size(matrix: list[str]) -> tuple[int, int]:
    return (len(matrix[0]), len(matrix))


def is_inside_matrix_bounds(matrix, row_index: int, col_index: int) -> bool:
    max_row_index, max_col_index = get_word_matrix_size(matrix)
    return 0 <= row_index < max_row_index and 0 <= col_index < max_col_index


# Extract all diagonals from word matrix
def extract_word_matrix_diag(word_matrix: list[str]) -> list[str]:
    word_matrix_diag: list[str] = []
    for col_index in range(len(word_matrix[0])):
        for row_index in range(len(word_matrix)):
            if col_index > 0 and row_index > 0:
                continue
            diagonal_string: str = word_matrix[row_index][col_index]
            diag_cell_row_index = row_index + 1
            diag_cell_col_index = col_index + 1
            while is_inside_matrix_bounds(
                word_matrix, diag_cell_row_index, diag_cell_col_index
            ):
                diagonal_string += word_matrix[diag_cell_row_index][diag_cell_col_index]
                diag_cell_row_index += 1
                diag_cell_col_index += 1
            word_matrix_diag.append(diagonal_string)
    return word_matrix_diag


def reverse_word_matrix(word_matrix: list[str]) -> list[str]:
    reversed_matrix: list[str] = []
    for row in word_matrix:
        reversed_matrix.append(row[::-1])
    return reversed_matrix


word_matrix_diag = extract_word_matrix_diag(word_matrix) + extract_word_matrix_diag(
    reverse_word_matrix(word_matrix)
)
word_matrix_col = build_word_matrix_col(word_matrix)


final_word_matrix = word_matrix + word_matrix_col + word_matrix_diag


word_occurences = 0
for row in final_word_matrix:
    word_occurences += len(re.findall("XMAS", row))
    word_occurences += len(re.findall("XMAS", row[::-1]))

print(f"{word_occurences} occurences of XMAS in the matrix")
