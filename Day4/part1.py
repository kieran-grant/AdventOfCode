REQUIRED = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def solution():
    passports = []
    with open("./input.txt") as f:
        content = f.readlines()
        buff = []
        for line in content:
            if line.strip():
                line = line.strip().split(" ")
                for item in line:
                    buff.append(item)
            else:
                passports.append(buff)
                buff = []
        passports.append(buff)

    valid_passports = 0
    print( f"Num passports: {len(passports)}")
    for pp in passports:
        keys = []
        for item in pp:
            k,v = item.split(":")
            keys.append(k)

        valid = True
        for req in REQUIRED:
            if req not in keys:
                valid = False

        if valid:
            valid_passports += 1

    print(f"Valid passports: {valid_passports}")

if __name__ == "__main__":
    solution()
