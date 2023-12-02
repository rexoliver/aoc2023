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
# Attempting sliding window solution: 
# Sliding window deemed too hard since it's late at night, regex it is: 
# learned a bunch about regex too. 

# AND I LEARNED A VALUABLE LESSON ABOUT AOC: 
# I looked at the input immediatelly after reading part 1, saw the numbers
# spelled out literally, and implemented a part 2 solution 
# instead of a part 1 solution. 
#
# No wonder my output would not work!!!
#  
# Lesson: Solve for the first problem, not the second.  

def get_num(str):
    if str.isdigit():
        return int(str)
    return nums[str]



def solve(regex):
    firstdigit = 0
    lastdigit = 0
    total = 0
    matches = []
    with open("./input.txt", "r") as file:
        for line in file:
            matches = re.findall(regex, line)
            firstdigit = get_num(matches[0])
            lastdigit = get_num(matches[-1])
            total += (firstdigit * 10) + lastdigit 
            
    file.close()
    return total

def main():
    compiled_regex_p1 = re.compile(r'([1-9])')
    compiled_regex_p2 = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))')
    
    print(f'Total Part 1: {solve(compiled_regex_p1)}')
    print(f'Total Part 2: {solve(compiled_regex_p2)}')

if __name__ == "__main__":
    main()
