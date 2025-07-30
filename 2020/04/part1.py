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

required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
optional_fields = set(['cid'])
amount_valid = len([passport for passport in passports if required_fields.issubset(passport.keys())])
print(amount_valid)
