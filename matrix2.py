import random
import math
import matplotlib.pyplot as plt   # Added for histogram

rows = 80
cols = 5

# Function to generate Poisson random number (λ = 3)
def poisson(lam=3):
    L = math.exp(-lam)
    k = 0
    p = 1
    while p > L:
        k += 1
        p *= random.random()
    return k - 1

matrix = []

for _ in range(rows):
    row = []
    for _ in range(cols):

        # Auto-select distribution randomly (0,1,3)
        dist_type = random.choice([0, 1, 3])

        if dist_type == 0:
            # Normal distribution (0–40)
            value = int(random.gauss(20, 7))
            value = max(0, min(40, value))

        elif dist_type == 1:
            # Uniform distribution (41–70)
            value = random.randint(41, 70)

        elif dist_type == 3:
            # Poisson distribution (λ=3)
            value = poisson(3)
            value = 71 + value
            value = max(71, min(95, value))

        row.append(value)

    matrix.append(row)

print("Generated 80x5 Marks Matrix:")
print(matrix)


# ===============================
# Histogram Implementation
# ===============================

# Flatten matrix (convert 80x5 into 400 values)
all_marks = []
for row in matrix:
    for mark in row:
        all_marks.append(mark)

# Create histogram
plt.figure(figsize=(8,5))
plt.hist(all_marks, bins=15, edgecolor='black')

plt.title("Histogram of Marks (Mixed Distributions)")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()