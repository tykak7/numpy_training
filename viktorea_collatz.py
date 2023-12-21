# Vhodným způsobem zobrazte (v jednom okně) pomocí knihovny matplotlib:
#
#  Histogram s počtem koků pro čísla od 1 do 10^6
# Pro čísla od 1 do 10^6 zobrazte počet kroků
# Zobrazte pro každé číslo v rozsahu 1-10^6  (osa X) nejvyšší dosaženou hodnotu během iterování k  číslu 1 (např. pro číslo 12 to bude hodnota 16)

import matplotlib.pyplot as plt

def collatz_steps(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Task 1: Histogram with number of steps for numbers from 1 to 10^6
hist_data = [collatz_steps(i) for i in range(1, 10**6 + 1, 1000)]

# Task 2: Display the number of steps for numbers from 1 to 10^6
x_values = list(range(1, 10**6 + 1, 1000))
y_values = [collatz_steps(i) for i in x_values]

# Task 3: Highest value reached during the iteration for each number
max_values = [max(collatz_sequence(i)) for i in range(1, 10**6 + 1, 1000)]

# Create a single window with subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 8))

# Plot 1: Histogram
ax1.hist(hist_data, bins=50, edgecolor='black')
ax1.set_title('Histogram of Collatz steps.')
ax1.set_xlabel('Number of Steps')
ax1.set_ylabel('Frequency')

# Plot 2: Number of steps
ax2.plot(x_values, y_values, marker='.', linestyle='None', color='blue')
ax2.set_title('Number of steps in Collatz')
ax2.set_xlabel('Number')
ax2.set_ylabel('Number of steps')

# Plot 3: Highest value reached
ax3.plot(x_values, max_values, marker='.', linestyle='None', color='green')
ax3.set_title('Highest value reached in Collatz sequence')
ax3.set_xlabel('Number')
ax3.set_ylabel('Highest value reached')

# Adjust layout for better visualization
plt.tight_layout()

# Show the plots
plt.show()

