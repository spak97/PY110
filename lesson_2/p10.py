import random

def gen_uuid():
    # set a str of 0-9 a-f
    hchars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []
    # push random char into lists of sizes 8, 4, 4, 4, 12
    for section in sections:
        chars = [random.choice(hchars) for _ in range(section)]
        uuid.append(''.join(chars))
    # join lists with "-"
    return '-'.join(uuid)
    # return completed list

