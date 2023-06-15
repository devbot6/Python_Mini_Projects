import random

def random_walk(n):
    """Simulate a random walk of n steps."""
    position = 0
    for i in range(n):
        if random.random() < 0.5:
            position -= 1
        else:
            position += 1
    return position

def average_distance(n, num_trials):
    """Calculate the average distance from the starting point over num_trials random walks of n steps."""
    total_distance = 0
    for i in range(num_trials):
        distance = random_walk(n)
        total_distance += abs(distance)
    return total_distance / num_trials

# Example usage:
n = 1000
num_trials = 10000
avg_dist = average_distance(n, num_trials)
print(f"Average distance from starting point after {n} steps and {num_trials} trials: {avg_dist:.2f}")
