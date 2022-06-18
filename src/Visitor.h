//
// Created by ritwi on 6/18/2022.
//

#ifndef PIPICOPICO_VISITOR_H
#define PIPICOPICO_VISITOR_H
#include "LuaBaseVisitor.h"
#include "PicoAst.h"

namespace LuaLanguage {

    class Visitor : public LuaBaseVisitor {
    public:
        PicoAst picoAst;
        std::any visitGlobalChunk(LuaParser::ChunkContext *ctx);
        void visitGlobalBlock(LuaParser::BlockContext *ctx);
    };

} // LuaLanguage

#endif //PIPICOPICO_VISITOR_H
