import re

computer_memory: str = None

with open("day03_data.txt") as txtfile:
    computer_memory = txtfile.read()


valid_sequences: list[str] = re.findall(
    r"(mul\([0-9]+,[0-9]+\))|(don't\(\))|(do\(\))",
    computer_memory,
)

sum = 0
sequences_enabled = True
for sequence in valid_sequences:
    # sequence[1] is presence of a "don't"
    if sequence[1] != "":
        sequences_enabled = False
        print(f"After {sequence} switching to {sequences_enabled}")
        continue
    # sequence[2] is presence of a "do"
    elif sequence[2] != "":
        sequences_enabled = True
        print(f"After {sequence} switching to {sequences_enabled}")
        continue

    if sequences_enabled:
        print(sequence)
        number1, number2 = sequence[0].lstrip("mul(").rstrip(")").split(",")
        sum += int(number1) * int(number2)

print(sum)
