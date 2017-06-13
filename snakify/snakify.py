import re

from num2words import num2words
from slugify import slugify


def snakify(key):
    # convert camelCase to snake_case
    key = key[0] + re.sub(r'([^A-Z])([A-Z][^A-Z])', r'\1_\2', key[1:])

    # avoid starting with a number
    match = re.match(r'^\d+', key)
    if match:
        num = match.group(0)
        word = num2words(int(num))
        key = word + '_' + key[len(num):]

    # slugify
    key = key.replace('-', '_')
    key = slugify(key, ok='_', only_ascii=True)

    return key
