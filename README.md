# Notes
## Building antlr def to test and see in the ui
    antlr ./Lua.g4                --> to build java source
    javac Lua*.java               --> to compile
    grun Lua chunk -gui           --> to test and show the tree in the ui