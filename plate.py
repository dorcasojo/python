def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    seen_digit = False
    for i, char in enumerate(s):
        if char.isalpha():
            if seen_digit:
                return False  # letter after a digit — not allowed
        elif char.isdigit():
            if not seen_digit and char == "0":
                return False  # first digit can't be 0
            seen_digit = True
        else:
            return False  # punctuation, space, etc.

    return True


main()
