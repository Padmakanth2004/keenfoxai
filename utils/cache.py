cache_store = {}

def get_cached_response(prompt):
    return cache_store.get(prompt)

def set_cached_response(prompt, response):
    cache_store[prompt] = response