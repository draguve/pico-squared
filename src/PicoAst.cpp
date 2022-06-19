//
// Created by ritwi on 6/18/2022.
//

#include <iostream>
#include "PicoAst.h"

namespace LuaLanguage {
    PicoAst::PicoAst() = default;

    PicoNumber::PicoNumber() {
        picoType = Number;
    }

    PicoFunc::PicoFunc(){
        picoType = Function;
    }

    PicoBool::PicoBool() {
        picoType = Bool;
    }

    PicoString::PicoString() {
        picoType = String;
    }

    PicoTable::PicoTable() {
        picoType = Table;
    }

    PicoArray::PicoArray(){
        picoType = Array;
    }
} // LuaLanguage