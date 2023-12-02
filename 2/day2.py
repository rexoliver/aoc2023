# Rex Oliver
# Day 2 AOC
import re

def get_color_number(text):
    ret = []
    if text.find("red")>= 0:
        ret.append("red")
    if text.find("blue")>= 0:
        ret.append("blue")
    if text.find("green")>= 0:
        ret.append("green")
    
    ret.append(int(re.search(r'\d+', text).group()))
    print(ret)
    return ret



def main():
    targetred = 12
    targetgreen = 13
    targetblue = 14

    red = 0
    green = 0
    blue = 0
    total = 0
    matches = []
    with open("./input.txt", "r") as file:
        for pos, line in enumerate(file):
            matches = re.findall(r'\d+\s\w+', line)
            for i in matches: 
                currmatch = get_color_number(i)
                if currmatch[0] == "red":
                    red = max(red, currmatch[1])
                elif currmatch[0] =="blue":
                    blue = max(blue, currmatch[1])
                elif currmatch[0]== "green": 
                    green = max(green, currmatch[1])
                

            print(matches)
            # add current line to total  
            if red <= targetred and green <= targetgreen and blue <= targetblue:
                total += pos
            red = 0
            green = 0
            blue = 0

    print(total)

if __name__ == "__main__":
    main()