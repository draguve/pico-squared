//
// Created by ritwi on 6/18/2022.
//

#include "Visitor.h"
#include "PicoAst.h"

namespace LuaLanguage {

    PicoAst picoAst;

    std::any Visitor::visitBlock(LuaParser::BlockContext *ctx) {
        return LuaBaseVisitor::visitBlock(ctx);
    }

    std::any Visitor::visitChunk(LuaParser::ChunkContext *ctx) {
        return picoAst;
    }
} // LuaLanguage