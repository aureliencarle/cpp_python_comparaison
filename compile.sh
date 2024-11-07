c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) my_class.cpp bindings.cpp -o my_module$(python3-config --extension-suffix)
