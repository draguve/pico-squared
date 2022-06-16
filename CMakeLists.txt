# minimum required CMAKE version
project(PiPicoPico)
CMAKE_MINIMUM_REQUIRED(VERSION 3.7 FATAL_ERROR)

cmake_policy(SET CMP0114 OLD)
cmake_policy(SET CMP0054 OLD)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

# compiler must be 17
set(CMAKE_CXX_STANDARD 17)

# required if linking to static library
add_definitions(-DANTLR4CPP_STATIC)

# using /MD flag for antlr4_runtime (for Visual C++ compilers only)
set(ANTLR4_WITH_STATIC_CRT OFF)

# Specify the version of the antlr4 library needed for this project.
# By default the latest version of antlr4 will be used.  You can specify a
# specific, stable version by setting a repository tag value or a link
# to a zip file containing the libary source.
# set(ANTLR4_TAG 4.10.1)
# set(ANTLR4_ZIP_REPOSITORY https://github.com/antlr/antlr4/archive/refs/tags/4.10.1.zip)

# add external build for antlrcpp
include(ExternalAntlr4Cpp)
# add antrl4cpp artifacts to project environment
include_directories(${ANTLR4_INCLUDE_DIRS})

# set variable pointing to the antlr tool that supports C++
# this is not required if the jar file can be found under PATH environment
#set(ANTLR_EXECUTABLE /home/user/antlr-4.10.1-complete.jar)
# add macros to generate ANTLR Cpp code from grammar
find_package(ANTLR REQUIRED)

# Call macro to add lexer and grammar to your build dependencies.
antlr_target(Lua Lua.g4 LEXER PARSER LISTENER VISITOR PACKAGE LuaLanguage)


# include generated files in project environment
include_directories(${ANTLR_Lua_OUTPUT_DIR})

# add generated grammar to demo binary target
add_executable(demo
        ${ANTLR_Lua_CXX_OUTPUTS}
        main.cpp)

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)
target_link_libraries(demo PRIVATE antlr4_static Threads::Threads)
