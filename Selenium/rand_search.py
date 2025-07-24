import random
import string

def random_pair():
    # Create a pool of characters: lowercase letters, uppercase letters, and digits
    pool = string.ascii_lowercase + string.digits
    
    # Select two random characters from the pool
    return ''.join(random.choices(pool, k=2))

# Example usage
print(random_pair())