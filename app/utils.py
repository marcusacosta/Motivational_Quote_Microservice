import random

# Keeps track of the last quote served for each category
last_quote_cache = {}

def get_random_quote(category, cache):
    quotes = QUOTES[category]
    last_quote = cache.get(category)
    
    new_quote = random.choice(quotes)
    while len(quotes) > 1 and new_quote == last_quote:
        new_quote = random.choice(quotes)

    cache[category] = new_quote
    return new_quote

from .quotes import QUOTES
