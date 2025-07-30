import string

passports = []
with open('input.txt') as f:
    passport = {}
    for line in f:
        if line.strip() == "":
            passports.append(passport)
            passport = {}
            continue

        for key_val in line.strip().split(" "):
            key, val = key_val.split(':')
            passport[key] = val
    passports.append(passport)

def validate(passport):
    try:
        if (byr := int(passport['byr'])) < 1920 or byr > 2002:
            return False

        if (iyr := int(passport['iyr'])) < 2010 or iyr > 2020:
            return False

        if (eyr := int(passport['eyr'])) < 2020 or eyr > 2030:
            return False

        hgt = passport['hgt']
        if (measure := hgt[-2:]) != 'in' and measure != 'cm':
            return False
        if measure == 'cm':
            if (height := int(hgt[:-2])) < 150 or height > 193:
                return False
        if measure == 'in':
            if (height := int(hgt[:-2])) < 59 or height > 76:
                return False

        hcl = passport['hcl']
        if hcl[0] != '#':
            return False
        if not all(c in string.hexdigits for c in hcl[1:]):
            # TODO: check if uppercase?
            return False

        ecl = passport['ecl']
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not ecl in valid_colors:
            return False

        pid = passport['pid']
        if len(pid) != 9:
            return False

        return True
    except Exception as e:
        print(e)
        return False



required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
optional_fields = set(['cid'])
amount_valid = len([passport for passport in passports if validate(passport)])
print(amount_valid)

