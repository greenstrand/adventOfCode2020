from solvers import BaseSolver
import re

PATTERN = r"(?P<field>\w{3}):([^ \n]+)"


FIELDS = {
    "byr": "Birth Year",
    "iyr": "Issue Year",
    "eyr": "Expiration Year",
    "hgt": "Height",
    "hcl": "Hair Color",
    "ecl": "Eye Color",
    "pid": "Passport ID",
    # "cid": "Country ID",
}

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
fd = lambda v: re.match(r"^\d{4}$", v)
within = lambda v, a, b: (v) >= a and (v) <= b


def is_height(v):
    m = re.match(r"^([0-9.]+)(in|cm)$", v)
    if m:
        val = float(m.group(1))
        return within(val, 150, 193) if "cm" in v else within(val, 59, 76)
    return False


FIELD_CHECK = {
    "byr": (lambda v: fd(v) and within(int(v), 1920, 2002)),
    "iyr": (lambda v: fd(v) and within(int(v), 2010, 2020)),
    "eyr": (lambda v: fd(v) and within(int(v), 2020, 2030)),
    "hgt": is_height,
    "hcl": (lambda v: re.match(r"^#[0-9a-f]{6}$", v)),
    "ecl": (lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")),
    "pid": (lambda v: re.match(r"^\d{9}$", v)),
    # "cid": lambda v: True,
}


def check_fields(psp):
    diff = set(FIELD_CHECK) - set(psp)
    if diff:
        return False
    fields = {
        field: FIELD_CHECK[field](value)
        for field, value in psp.items()
        if field in FIELD_CHECK
    }
    # if not all(fields.values()):
    #     print({field: psp[field] for field, val in fields.items() if not val})
    return all(fields.values())


class Solver(BaseSolver):
    @staticmethod
    def process_input(f):
        text = f.read().strip()

        def extract_field(passport):
            fields = {
                match.group(1): match.group(2)
                for match in re.finditer(PATTERN, passport)
            }
            return fields

        passports = text.split("\n\n")
        return [extract_field(p) for p in passports]

    @staticmethod
    def part_1(data):
        return len([p for p in data if not (set(FIELDS) - set(p))])

    @staticmethod
    def part_2(data):
        return len([p for p in data if check_fields(p)])
