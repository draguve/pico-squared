//
// Created by ritwi on 6/18/2022.
//

#include "unordered_map"

#ifndef PIPICOPICO_PICOAST_H
#define PIPICOPICO_PICOAST_H

namespace LuaLanguage {
    enum ValueTypes{
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
        int picoType = 0;
    };

    class PicoNumber : public PicoValue{
        
    };

    class PicoString : public PicoValue{

    };

    class PicoBool : public PicoValue{

    };

    class PicoTable : public PicoValue{
    public:
        bool onlyNumberAccess = true;
        bool onlyStringAccess = true;
        int numberOfUniqueAccess = 0;
        std::unordered_map<std::string ,PicoValue> data;
    };

    class PicoArray : public PicoValue{
    public:
        int maxSize;
    };

    class PicoStat{

    };

    class PicoFunc : public PicoValue{
    public:
        std::string name;
        int numberOfParameters;
        std::unordered_map<std::string,PicoVariable> parameters;
        std::vector<PicoStat> stats;
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
