def solution(right=3, down=1):
    with open("./input.txt") as f:
        content = f.read().splitlines()
    
    i = 0
    trees = 0
    for line in content[::down]:
        i = i % len(line)
        if line[i] == "#":
            trees += 1
        i += right
    
    print(f"Right = {right}, down = {down}. Trees encountered: {trees}")
    return trees

if __name__ == "__main__":
    a = solution(1,1)
    b = solution(3,1)
    c = solution(5,1)
    d = solution(7,1)
    e = solution(1,2)
    print(f"Product of trees = {a * b * c * d * e}")
