import itertools

def crack_password(cipher, start, end):
    password_list = list(itertools.permutations(cipher))
    password_string = "".join(cipher)
    print("The original permutation is:", password_string)
    for password in password_list:
        if start <= int(password_string) <= end:
            return "".join(password)
    return "No password found in this range"

def crack_password_without_range(cipher):
    password_list = list(itertools.permutations(cipher))
    password_string = "".join(cipher)
    print("The original permutation is:", password_string)
    for password in password_list:
        if password_string == "".join(password):
            return "".join(password)
    return "No password found"

# example usage
cipher = ['1', '2', '3']
print(crack_password(cipher, 123, 321)) # this will return '123'
print(crack_password_without_range(cipher)) # this will return '123'