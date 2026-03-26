import string

_password = input("Enter your password: ")

_upperCase = any(c in string.ascii_uppercase for c in _password)
_lowerCase = any(c in string.ascii_lowercase for c in _password)
_special = any(c in string.punctuation for c in _password)
_digits = any(c in string.digits for c in _password)

_characters = [_upperCase, _lowerCase, _special, _digits]

_length = len(_password)

_score = 0

try:
    with open('common.txt', 'r', encoding='utf-8') as f:
        _common = f.read().splitlines()
except FileNotFoundError:
    _common = []

if _password in _common:
    print("Password was found in a common list. Score: 0 / 7")
    exit()

if _length > 8:
    _score += 1
if _length > 12:
    _score += 1
if _length > 16:
    _score += 1
if _length > 21:
    _score += 1
print(f"Password length is {str(_length)}, adding {str(_score)} points!")

if sum(_characters) > 1:
    _score += 1
if sum(_characters) > 2:
    _score += 1
if sum(_characters) > 3:
    _score += 1
print(f"Password has {str(sum(_characters))} different character types, adding {str(sum(_characters) - 1)} points!")

if _score < 6:
    print(f"The password is quite weak! Score : {str(_score)} / 7")
elif _score == 6:
    print(f"The password is ok! Score: {str(_score)} / 7")
elif _score > 6 and _score < 8:
    print(f"The password is pretty good! Score: {str(_score)} / 7")
elif _score > 8:
    print(f"The password is strong! Score: {str(_score)} / 7")
