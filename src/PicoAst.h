//
// Created by ritwi on 6/18/2022.
//

#include "unordered_map"

#ifndef PIPICOPICO_PICOAST_H
#define PIPICOPICO_PICOAST_H

namespace LuaLanguage {

    class PicoVariable{

    };

    class PicoFunc{

    };

    class PicoAst {
    public:
        PicoAst();

        std::unordered_map<std::string,PicoFunc> functions;
        std::unordered_map<std::string,PicoVariable> globals;
        static void print();
    };

} // LuaLanguage

#endif //PIPICOPICO_PICOAST_H
