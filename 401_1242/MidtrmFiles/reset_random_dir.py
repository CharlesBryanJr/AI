import random
def reset_random_dir(self):
    self.random_dir = {1, 2, 3, 4}
    self.random_dir = set(random.sample(list(self.random_dir), len(self.random_dir)))
    return None
