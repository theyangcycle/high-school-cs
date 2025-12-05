import random

def random_case(text):
    result = []
    count = 0
    last_case = None

    for c in text:
        if not c.isalpha():
            result.append(c)
            continue

        if last_case == "upper" and count >= 2:
            new_case = "lower"
        elif last_case == "lower" and count >= 2:
            new_case = "upper"
        else:
            new_case = random.choice(["upper", "lower"])

        if new_case == "upper":
            result.append(c.upper())
        else:
            result.append(c.lower())

        if new_case == last_case:
            count += 1
        else:
            count = 1
            last_case = new_case

    return ''.join(result)

print(random_case(input()))