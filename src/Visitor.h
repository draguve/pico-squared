//
// Created by ritwi on 6/18/2022.
//

#ifndef PIPICOPICO_VISITOR_H
#define PIPICOPICO_VISITOR_H
#include "LuaBaseVisitor.h"

namespace LuaLanguage {

    class Visitor : public LuaBaseVisitor {

    public:
        std::any visitChunk(LuaParser::ChunkContext *ctx) override;
        std::any visitBlock(LuaParser::BlockContext *ctx) override;
    };

} // LuaLanguage

#endif //PIPICOPICO_VISITOR_H
