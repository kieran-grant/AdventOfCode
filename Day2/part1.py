import re

def solution():
    with open("./input.txt") as f:
        content = f.readlines()

    valid = 0
    for line in content:
        res = re.search("(\d+)-(\d+) ([a-z]{1}): (\w*)", line)
        mi = int(res.group(1))
        ma = int(res.group(2))
        char = res.group(3)
        password = res.group(4)

        count = password.count(char)
        if count >= mi and count <= ma:
            valid += 1

    print(f"Number of valid passwords: {valid}")

if __name__ == "__main__":
    solution()
