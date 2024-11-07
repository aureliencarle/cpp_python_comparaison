/*
// fichier : my_class.cpp
#include <pybind11/pybind11.h>
#include "my_class.h"
#include <chrono>
#include <cmath>

namespace py = pybind11;

class MyClass
{
public:
    // Constructeur
    MyClass() {}

    // Méthode simple pour calculer la somme des carrés
    double sum_of_squares(int n)
    {
        double sum = 0;
        for (int i = 0; i < n; ++i)
        {
            sum += std::pow(i, 2);
        }
        return sum;
    }
};

PYBIND11_MODULE(my_module, m)
{
    py::class_<MyClass>(m, "MyClass")
        .def(py::init<>())
        .def("sum_of_squares", &MyClass::sum_of_squares);
}
*/

// fichier : my_class.cpp
#include "my_class.h"
#include <cmath>
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>

// Constructeur par défaut
MyClass::MyClass() : value(0) {}

// Constructeur avec un argument
MyClass::MyClass(int v) : value(v) {}

// Méthode pour calculer la somme des carrés jusqu'à un certain nombre
double MyClass::sum_of_squares(int n)
{
    double sum = 0;
    for (int i = 0; i < n; ++i)
    {
        sum += std::pow(i, 2);
    }
    return sum;
}

// Méthode pour obtenir la valeur de l'attribut `value`
int MyClass::get_value() const
{
    return value;
}

void MyClass::run_loop(std::string const& file) const
{
    std::ifstream infile(file);
    std::string line;
    std::vector<std::vector<int>> numbersList;
    
    while (getline(infile, line)) {
        std::stringstream ss(line);
        std::string number;
        std::vector<int> numbers(3);
        
        // Séparer les nombres par ';'
        int n = 0;
        while (getline(ss, number, ';')) {    
            numbers[n]=stoi(number);
            n++;
        }
        // Ajouter à la liste principale
        numbersList.push_back(numbers);
    }
    std::cout << numbersList[0][0] << numbersList[0][1] << numbersList[0][2] << std::endl;

    for (size_t n = 0; n< numbersList.size() ; ++n)
    {
        double x = std::sqrt(numbersList[n][0]*numbersList[n][0]+numbersList[n][1]*numbersList[n][1]+numbersList[n][2]*numbersList[n][2]);
    }
}

// Méthode pour traiter le dictionnaire et retourner la somme des valeurs
int MyClass::process_dict(const std::unordered_map<std::string, int> &data)
{
    int sum = 0;
    for (const auto &pair : data)
    {
        sum += pair.second;
    }
    return sum;
}