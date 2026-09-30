marks = [85, 72, 38, 91, 45, 29, 67, 55]

highest = marks[0]
lowest = marks[0]
total = 0
passed = 0
failed = 0

for mark in marks:

    total = total + mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(marks)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Passed:", passed)
print("Students Failed:", failed)