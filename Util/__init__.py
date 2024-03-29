import string
import random


def get_random_string(N):
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=N))


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))
