import re
# Day 1
# Rex Oliver
nums = {"one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
        }

firstdigit = 0
lastdigit = 0

total = 0
total_append = 0
matches = []

# Attempting sliding window solution: 
# Sliding window deemed too hard since it's late at night, regex it is: 
# learned a bunch about regex too

pattern = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|[1-9])')


with open("./input.txt", "r") as file:
    for line in file:

        
        matches.append(pattern.search(line).group())
        matches.append(pattern.search(line[::-1]).group())
        firstdigit = int(matches[0]) if matches[0].isdigit() else nums.get(matches[0], 0)
        lastdigit = int(matches[1]) if matches[1].isdigit() else nums.get(matches[1], 0)
        total_append = (firstdigit * 10) + lastdigit 
        # append local first and last calibration numbers to total
        total += total_append
        
        print(f'matches: {matches} firstdigit: {firstdigit} seconddigit: {lastdigit} total append: {total_append} total: {total}')
        matches = []
file.close()
print(total)
