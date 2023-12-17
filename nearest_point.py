##  Use NumPy to load the points.csv file, which contains on each line the coordinates of the points in 2D Euclidean space.

##  Without using loops, just using NumPy functions, load the file and find the point that is closest to point [0;0].



import numpy as np

# Load the points from the file into the numpy array
try:
    points = np.loadtxt('\\points.csv', delimiter=' ', dtype=float)

    if points.size == 0:
        print("No data in the file.")
    else:
        # computing the Euclidean distances from the origin to each point
        # distances = sqrt[ (x2-x1)^2 + (y2-y1)^2 ]
        distances = np.sqrt(np.sum((points - [0, 0]) ** 2, axis=1))
        # (points - [0, 0]) : coordinate difference of the point to be checked from the point [0, 0]
        # ** 2: Squaring the obtained differences.
        # np.sum(..., axis=1): Sums the squares of the differences on each row (by axis).


        # Find the index of the point with the smallest distance to the origin
        min_distance_index = np.argmin(distances)

        # Print the coordinates of the nearest point
        print(f"The coordinates of the nearest point are: {points[min_distance_index]}")

except Exception as e:
    print(f"An error occurred while reading a file: {e}")
