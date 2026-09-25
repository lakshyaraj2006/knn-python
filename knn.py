import csv
import math
from pathlib import Path

# Function to load dataset
def load_dataset(filename: str) -> list:
    data = []

    ext = Path(filename).suffix.lstrip(".")

    if (ext != "csv"):
        print("Cannot load non csv files")
    else:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                data.append({
                    "x1": row["sepal_length"],
                    "x2": row["sepal_width"],
                    "species": row["species"]
                })

    return data


if __name__ == "__main__":
    data = load_dataset("iris.csv")

    # Take x1 and x2 as input
    print("Enter the data to get predicted species: ")

    try:
        x1 = float(input("Enter sepal length: "))
        x2 = float(input("Enter sepal width: "))
    except ValueError:
        print("Please enter floating point numbers")
        exit()
    
    distances = []

    for row in data:
        euclidean_dist = math.sqrt(
            (x1 - float(row['x1']))**2 + (x2 - float(row['x2']))**2
        )
        distances.append((euclidean_dist, row['species']))

    distances.sort(key=lambda x: x[0])

    try:
        k = int(input("Enter the number of nearest neighbors: "))
    except ValueError:
        print("Number of neighbors must be an integer")
        exit()

    neighbors = distances[:k]

    print("\nNearest neighbors")

    for distance, species in neighbors:
        print(f"Distance: {distance}, Species: {species}")

    votes = {}

    for distance, species in neighbors:
        votes[species] = votes.get(species, 0) + 1

    prediction = max(votes, key=votes.get)

    print("\nVotes:", votes)
    print("\nPredicted species:", prediction)

