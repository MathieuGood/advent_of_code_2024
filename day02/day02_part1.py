import csv


reports = []

with open("day02_data.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        reports.append([int(number) for number in row])


def is_valid_interval(number1: int, number2: int) -> bool:
    interval = 4
    return 0 < abs(number1 - number2) < interval


def is_report_safe(report: list[int]) -> bool:
    prev_number: int = None
    is_increasing: bool = None

    for index, number in enumerate(report):
        # First round: set prev_number
        if prev_number == None:
            prev_number = number
            continue

        # Second round: define if increasing or decreasing
        if is_increasing == None:
            if is_valid_interval(number, prev_number):
                is_increasing = number > prev_number
                prev_number = number
                continue
            else:
                print(f"Report {report} UNSAFE after first round")
                return False

        if is_increasing:
            if number > prev_number and is_valid_interval(number, prev_number):
                prev_number = number

                continue
            else:
                print(f"Report {report} UNSAFE")
                return False

        if not is_increasing:
            if number < prev_number and is_valid_interval(number, prev_number):
                prev_number = number

                continue
            else:
                print(f"Report {report} UNSAFE")
                return False

    print(f"Report {report} SAFE")
    return True


safe_reports_number = 0
for report in reports:
    if is_report_safe(report):
        safe_reports_number += 1
print(safe_reports_number)

# print("----")
# is_report_safe([7, 6, 4, 2, 1])
# print("----")
# is_report_safe([1, 2, 7, 8, 9])
# print("----")
# is_report_safe([9, 7, 6, 2, 1])
# print("----")
# is_report_safe([1, 3, 2, 4, 5])
# print("----")
# is_report_safe([8, 6, 4, 4, 1])
# print("----")
# is_report_safe([1, 3, 6, 7, 9])
