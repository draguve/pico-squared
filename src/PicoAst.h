//
// Created by ritwi on 6/18/2022.
//

#include "unordered_map"
#include "fixed/fixed.h"

typedef numeric::fixed<16,16> fixed;

#ifndef PIPICOPICO_PICOAST_H
#define PIPICOPICO_PICOAST_H

namespace LuaLanguage {
    enum ValueTypes{
        Nil=0,
        Number=1,
        String=2,
        Function=4,
        Bool=8,
        Table=16,
        Array=32,
    };

    class PicoVariable{
        bool valueTypeChanges = false;
    };

    class PicoValue{
    public:
        int picoType = Nil;
    };

    class PicoNumber : public PicoValue{
    public:
        fixed number;
        bool isInteger = true;
        PicoNumber();
    };

    class PicoString : public PicoValue{
    public:
        PicoString();
    };

    class PicoBool : public PicoValue{
    public:
        PicoBool();
    };

    class PicoTable : public PicoValue{
    public:
        PicoTable();
        bool onlyNumberAccess = true;
        bool onlyStringAccess = true;
        int numberOfUniqueAccess = 0;
        std::unordered_map<std::string ,PicoValue> data;
    };

    class PicoArray : public PicoValue{
    public:
        int maxSize = 0;
        PicoArray();
    };

    class PicoStat{

    };

    class PicoFunc : public PicoValue{
    public:
        PicoFunc();
        std::string name;
        int numberOfParameters = 0;
        std::unordered_map<std::string,PicoVariable> parameters;
        std::unordered_map<std::string,PicoVariable> lambda;
        std::vector<PicoStat> stats;
    };

    class PicoAst {
    public:
        PicoAst();
        std::unordered_map<std::string,PicoFunc> functions;
        std::unordered_map<std::string,PicoVariable> globals;
    };

} // LuaLanguage

#endif //PIPICOPICO_PICOAST_H
