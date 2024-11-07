import time
from my_class import MyClass as MyClassPy
import my_module  # Le module C++ compilé
import matplotlib.pyplot as plt
#
#import mplcyberpunk
#plt.style.use("cyberpunk")


# Test de la classe Python
def test_python(x):
    obj = MyClassPy()
    start = time.time()
    obj.run_loop(x)
    end = time.time()
    print(f"Python : {end - start} secondes")
    return end - start


# Test de la classe Python
def test_numpy_python(x):
    obj = MyClassPy()
    start = time.time()
    obj.run_numpy_loop(x)
    end = time.time()
    print(f"Numpy : {end - start} secondes")
    return end - start

# Test de la classe C++
def test_cpp(x):
    obj = my_module.MyClass()
    start = time.time()
    obj.run_loop(x)
    end = time.time()
    print(f"C++ : {end - start} secondes")
    return end - start


if __name__ == "__main__":

    # Valeurs de n pour les puissances de 10
    n_range =  range(1,8)
    n_values = [f'numbers_10{n}.txt' for n in n_range]
    x_values = [10**n for n in n_range]

    # Hypothèse : résultats des fonctions (exemple de valeurs, à adapter selon les résultats réels)
    python_results = [test_python(n) for n in n_values]
    numpy_results = [test_numpy_python(n) for n in n_values]
    #jax_results = [test_jax_python(n) for n in n_values]
    cpp_results = [test_cpp(n) for n in n_values]

    factor_numpy_cpp = [numpy / cpp for numpy, cpp in zip(numpy_results, cpp_results)]
    factor_python_cpp = [
        python / cpp for python, cpp in zip(python_results, cpp_results)
    ]

    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(
        x_values,
        factor_numpy_cpp,
        label="Factor numpy(conda)/c++",
        marker="+",
        linestyle="-",
        color="blue",
    )
    plt.plot(
        x_values,
        factor_python_cpp,
        label="Factor python/c++",
        marker="+",
        linestyle="-",
        color="red",
    )
    #plt.plot(
    #    n_values,
    #    factor_jax_cpp,
    #    label="Factor jax/c++",
    #    marker="o",
    #    linestyle="-",
    #    color="green",
    #)
    # Mise en forme
    plt.xscale("log")
    #plt.yscale("log")
    plt.xlabel("Events (log scale)")
    plt.ylabel("Time Factor (log scale)")
    plt.title(r"$\sum_{i=0}^3 x_i^2, \forall x_i \in [-100,100]$")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()
