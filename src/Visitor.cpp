//
// Created by ritwi on 6/18/2022.
//

#include "Visitor.h"
#include "PicoAst.h"

namespace LuaLanguage {

    void Visitor::visitGlobalBlock(LuaParser::BlockContext *ctx) {
        antlr4::tree::AbstractParseTreeVisitor::visitChildren(ctx);
    }

    std::any Visitor::visitFunctionDeclaration(LuaParser::FunctionDeclarationContext *ctx) {
        PicoFunc thisFunc;
        thisFunc.name = ctx->funcname()->NAME()[ctx->funcname()->NAME().size()-1]->getText();
        return thisFunc;
    }

    std::any Visitor::visitGlobalChunk(LuaParser::ChunkContext *ctx) {
        visitGlobalBlock(ctx->block());
        return picoAst;
    }

    std::any Visitor::visitNumber(LuaParser::NumberContext *ctx) {
        auto toReturn = new PicoNumber();
        if(ctx->INT()){
            toReturn->number = std::stoi(ctx->INT()->getText());
        }
        if(ctx->FLOAT()){
            toReturn->isInteger = false;
            toReturn->number = std::stod(ctx->FLOAT()->getText());
        }
        if(ctx->HEX()){
            toReturn->number = std::stoi(ctx->HEX()->getText().substr(2), nullptr,16);
        }
        if(ctx->BINARY()){
            toReturn->number = std::stoi(ctx->BINARY()->getText().substr(2), nullptr,2);
        }
        std::cout << toReturn->number << "\n";
        if(ctx->HEX_FLOAT()){
            //What
        }
        if(ctx->BINARY_FLOAT()){
            //How
        }
        return toReturn;
    }
} // LuaLanguage