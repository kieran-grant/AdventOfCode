def solution():
    with open("./input.txt") as f:
        content = f.read().splitlines()

    i = 3
    trees = 0
    for line in content[1:]:
        i = i % len(line)
        if line[i] == "#":
            trees+=1
        i += 3
    
    print(f"Trees encountered: {trees}")


if __name__ == "__main__":
    solution()
