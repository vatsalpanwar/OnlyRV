#include <iostream>
#include "DNest4/code/DNest4.h"
#include "MyModel.h"
#include "Data.h"
#include "Lookup.h"

using namespace DNest4;

int main(int argc, char** argv)
{
    Data::get_instance().load("RV.txt");
    Lookup::get_instance().load();
    DNest4::start<MyModel>(argc, argv);
    return 0;
}

