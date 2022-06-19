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

        std::any visitFunctionDeclaration(LuaParser::FunctionDeclarationContext *ctx) override;
        std::any visitNumber(LuaParser::NumberContext *ctx) override;
    };

} // LuaLanguage

#endif //PIPICOPICO_VISITOR_H
