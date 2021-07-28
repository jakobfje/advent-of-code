import pprint
import re

def getLines(path):
    f = open(path)
    lines = f.read().splitlines()
    f.close()
    return lines

def getPassports(input):
    passport = []
    passIdx = 0
    passport.append({})
    for line in input:
        if line != "":
            for entry in line.split(' '):
                passport[passIdx][entry.split(':')[0]] = entry.split(':')[1]
        else:
            passIdx = passIdx + 1
            passport.append({})

    return passport

def task1(input):
    passports = getPassports(input)
    return len([p for p in passports if ((len(p) == 8) or (len(p) == 7 and not 'cid' in p))])

def heightOk(hgt):
    if len(hgt) == 4 and 'in' in hgt:
        if int(hgt[0:2]) >= 59 and int(hgt[0:2]) <= 76:
            return True
    elif len(hgt) == 5 and 'cm' in hgt:
        if int(hgt[0:3]) >= 150 and int(hgt[0:3]) <= 193:
            return True

    return False
    
def task2(input):
    passports = getPassports(input)
    cnt = 0
    for p in passports:
        if (len(p) == 8) or (len(p) == 7 and not 'cid' in p):
            if (int(p['byr']) >= 1920 and int(p['byr']) <= 2002 and
                    int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020 and
                    int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030):
                if heightOk(p['hgt']):
                    if re.search("[#][a-f0-9]{6}", p['hcl']):
                        if (p['ecl'] == 'amb' or p['ecl'] == 'blu' or p['ecl'] == 'brn' or 
                                p['ecl'] == 'gry' or p['ecl'] == 'grn' or 
                                p['ecl'] == 'hzl' or p['ecl'] == 'oth'):
                            if len(p['pid']) == 9 and re.search("[0-9]{9}", p['pid']):
                                cnt = cnt + 1
                                print(p)
        #                     else:
        #                         print("Invalid pid")
        #                 else:
        #                     print("Invalid ecl")
        #             else:
        #                 print("Invalid hcl")
        #         else:
        #             print("Invalid hgt")
        #     else:
        #         print("Invalid yr")
        # else:
        #     print("Invalid count")

    return cnt

input = getLines("04input.txt")

print("Answer 1: " + str(task1(["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"])))
print("Answer 1: " + str(task1(input)))
print()
print("Answer 2: " + str(task2(["eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "",
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
    "",
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "",
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007",
    "",
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f",
    "",
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "",
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022",
    "",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"])))
print("Answer 2: " + str(task2(input)))