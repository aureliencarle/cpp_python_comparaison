import random

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('size',type=int, help='number of events')
args = parser.parse_args()

# Nom du fichier à générer
exposant = args.size
filename = f"numbers_10{exposant}.txt"

with open(filename, 'w') as file:
    for _ in range(10**exposant):
        numbers = [str(random.randint(-100, 100)) for _ in range(3)]
        file.write(";".join(numbers) + "\n")

print(f"Fichier '{filename}' généré avec succès.")