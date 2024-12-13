import re

computer_memory: str = None

with open("day03_data.txt") as txtfile:
    computer_memory = txtfile.read()


valid_sequences: list[str] = re.findall(
    r"(mul\([0-9]+,[0-9]+\))",
    computer_memory,
)
print(valid_sequences)

sum = 0
for sequence in valid_sequences:
    number1, number2 = sequence.lstrip("mul(").rstrip(")").split(",")
    sum += int(number1) * int(number2)

print(sum)
