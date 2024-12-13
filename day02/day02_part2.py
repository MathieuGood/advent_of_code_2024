import csv


reports: list[list[int]] = []

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

    for number in report:
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
    print(report)
    for i in range(len(report)):
        report_wihout_one_level = report.copy()
        report_wihout_one_level.pop(i)
        if is_report_safe(report_wihout_one_level):
            safe_reports_number += 1
            break
print(safe_reports_number)
