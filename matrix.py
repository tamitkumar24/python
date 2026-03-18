import random
import math
import matplotlib.pyplot as plt

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

# Step 1: Generate matrix
matrix = []

for _ in range(rows):
    row = []
    for _ in range(cols):
        dist_type = random.choice([0, 1, 3])
        if dist_type == 0:
            value = int(random.gauss(20, 7))
            value = max(0, min(40, value))
        elif dist_type == 1:
            value = random.randint(41, 70)
        elif dist_type == 3:
            value = poisson(3)
            value = 71 + value
            value = max(71, min(95, value))
        row.append(value)
    matrix.append(row)

print("Generated 80x5 Marks Matrix:")
print(matrix)

# ===============================
# Step 2: Create Target Column y
# ===============================

dataset = []

for row in matrix:
    m1, m2, m3, m4, m5 = row

    noise = random.gauss(0,1)

    y = 3.1*m1 + 4.5*m2 + 5.1*m3 + 6.5*m4 + 6*m5 + noise

    dataset.append([m1,m2,m3,m4,m5,y])

print("\nDataset with target column (first 5 rows):")
for row in dataset[:5]:
    print(row)

# ===============================
# Step 3: Split Dataset
# ===============================

random.shuffle(dataset)

train_size = int(0.70 * len(dataset))
val_size = int(0.15 * len(dataset))

train_data = dataset[:train_size]
val_data = dataset[train_size:train_size+val_size]
test_data = dataset[train_size+val_size:]

print("\nDataset Split")
print("Training size:", len(train_data))
print("Validation size:", len(val_data))
print("Test size:", len(test_data))

# ===============================
# Step 4: Separate X and Y
# ===============================

X_train = [row[:5] for row in train_data]
y_train = [row[5] for row in train_data]

X_val = [row[:5] for row in val_data]
y_val = [row[5] for row in val_data]

X_test = [row[:5] for row in test_data]
y_test = [row[5] for row in test_data]

print("\nFirst Training Sample")
print("X:", X_train[0])
print("y:", y_train[0])
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

# ===============================
# Step 2: Standardization (Z-score)
# ===============================

# Flatten matrix to compute mean and std
all_values = [val for row in matrix for val in row]
mean = sum(all_values) / len(all_values)
std = (sum((x - mean)**2 for x in all_values) / len(all_values))**0.5

# Create standardized matrix
standardized_matrix = []
for row in matrix:
    standardized_row = [(x - mean)/std for x in row]
    standardized_matrix.append(standardized_row)

print("\nStandardized Matrix (Z-scores):")
for row in standardized_matrix[:5]:  # Print first 5 rows for brevity
    print(row)

# ===============================
# Step 3: Heatmap
# ===============================

plt.figure(figsize=(10,8))
plt.imshow(standardized_matrix, cmap='coolwarm', aspect='auto')
plt.colorbar(label='Standardized Marks (Z-score)')
plt.title("Heatmap of Standardized Marks")
plt.xlabel("Subjects")
plt.ylabel("Students")
plt.show()