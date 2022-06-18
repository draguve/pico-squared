/* Copyright (c) 2012-2017 The ANTLR Project. All rights reserved.
 * Use of this file is governed by the BSD 3-clause license that
 * can be found in the LICENSE.txt file in the project root.
 */

//
//  main.cpp
//  antlr4-cpp-demo
//
//  Created by Mike Lischke on 13.03.16.
//

#include <iostream>
#include "any"
#include "antlr4-runtime.h"
#include "LuaVisitor.h"
#include "LuaLexer.h"
#include "Visitor.h"
#include "PicoAst.h"

using namespace antlr4;
using namespace LuaLanguage;

int main(int argc, const char* argv[]) {
    std::ifstream stream;

    if(argc<2){
        std::cout << "Please input filename to parse";
    }

    stream.open(argv[1]); //replace with filename from input

    ANTLRInputStream input(stream);
    LuaLexer lexer(&input);
    CommonTokenStream tokens(&lexer);
    LuaParser parser(&tokens);

    LuaParser::ChunkContext* tree = parser.chunk();

    Visitor visitor;
    PicoAst ast = std::any_cast<PicoAst>(visitor.visitChunk(tree));
    ast.print();
}