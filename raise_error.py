def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")

check_age(-7)