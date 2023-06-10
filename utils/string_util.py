import random
import string


def random_string(length, prefix="", letters=True, digits=True, punctuation=False):
    sample_str = ""
    if letters:
        sample_str += string.ascii_letters
    if digits:
        sample_str += string.digits
    if punctuation:
        sample_str += string.punctuation
    return prefix + "".join(random.choices(sample_str, k=length))
