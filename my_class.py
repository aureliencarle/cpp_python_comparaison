import numpy as np

# fichier : my_class.py
class MyClass:
    def __init__(self):
        pass

    def sum_of_squares(self, n):
        sum = 0
        for i in range(n):
            sum += i**2
        return sum

    def run_loop(self, name):
        numbers_list = []

        with open(name, 'r') as file:
            for line in file:
                numbers = list(map(int, line.strip().split(';')))
                numbers_list.append(numbers)
        for n in numbers_list:
            x = np.sqrt(n[0]* n[0] + n[1]* n[1] +n[2]* n[2])

    def run_numpy_loop(self,name):
        numbers_array = np.loadtxt(name, delimiter=';', dtype=int)

        for n in numbers_array:
            x = np.sqrt( n[0]* n[0] + n[1]* n[1] +n[2]* n[2])

    def run_numpy(self, name):
        n = np.loadtxt(name, delimiter=";", dtype=int)
        x = np.sqrt(n[:, 0] ** 2 + n[:, 1] ** 2 + n[:, 2] ** 2)