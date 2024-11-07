// fichier : bindings.cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h> // Nécessaire pour les conversions de conteneurs
#include "my_class.h"

namespace py = pybind11;

PYBIND11_MODULE(my_module, m)
{
    py::class_<MyClass>(m, "MyClass")
        .def(py::init<>())    // Constructeur par défaut
        .def(py::init<int>()) // Constructeur avec un argument
        .def("sum_of_squares", &MyClass::sum_of_squares)
        .def("get_value", &MyClass::get_value)
        .def("run_loop", &MyClass::run_loop)
        .def("process_dict", &MyClass::process_dict, "Traitement du dictionnaire"); // Binding de la méthode
}
