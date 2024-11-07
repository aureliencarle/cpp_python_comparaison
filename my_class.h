// fichier : my_class.h
#ifndef MY_CLASS_H
#define MY_CLASS_H

#include <unordered_map>
#include <string>

class MyClass
{
public:
    // Constructeurs
    MyClass();      // Constructeur par défaut
    MyClass(int v); // Constructeur avec un argument

    // Méthodes
    double sum_of_squares(int n);
    int get_value() const;
    void run_loop(std::string const& file) const;
    int process_dict(const std::unordered_map<std::string, int> &data);

private:
    int value;
};

#endif // MY_CLASS_H
