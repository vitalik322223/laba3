import re

def validate_snils(snils):
    snils_digits = re.sub(r'\D', '', snils)
    if len(snils_digits) != 11:
        return False
    control_number = int(snils_digits[-2:])
    snils_number = list(map(int, snils_digits[:-2]))
    result = 0
    for i in range(9):
        result += snils_number[i] * (9 - i)
    result %= 101
    if result == 100:
        result = 0
    if result != control_number:
        return False

    return True

snils = "123-456-789 00" 
print(snils)
if validate_snils(snils):
    print("ok")
else:
    print("error")
