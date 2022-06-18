//
// Created by ritwi on 6/18/2022.
//

#include "Visitor.h"
#include "PicoAst.h"

namespace LuaLanguage {

    void Visitor::visitGlobalBlock(LuaParser::BlockContext *ctx) {

        std::vector<LuaParser::StatContext*> stats = ctx->stat();

        for (auto stat : ctx->stat()) {
            if(auto func = dynamic_cast<LuaParser::FunctionDeclarationContext*>(stat)){
                std::cout<<"FunctionDeclaration\n";
            }
            if(auto variable = dynamic_cast<LuaParser::VariableDeclarationContext*>(stat)){
                std::cout<<"Variable\n";
            }
            if(auto functionCall = dynamic_cast<LuaParser::FunctionCallStatContext*>(stat)){
                std::cout<<"FunctionCall\n";
            }
        }
    }

    std::any Visitor::visitGlobalChunk(LuaParser::ChunkContext *ctx) {
        visitGlobalBlock(ctx->block());
        return picoAst;
    }
} // LuaLanguage