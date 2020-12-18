import re

def solution():
    with open("./input.txt") as f:
        content = f.readlines()

    valid = 0
    for line in content:
        res = re.search("(\d+)-(\d+) ([a-z]{1}): (\w*)", line)
        index1 = int(res.group(1)) - 1
        index2 = int(res.group(2)) - 1
        char = res.group(3)
        password = res.group(4)

        if (password[index1] == char or password[index2] == char) and (password[index1] != password[index2]):
            valid += 1

    print(f"Number of valid passwords: {valid}")

if __name__ == "__main__":
    solution()
