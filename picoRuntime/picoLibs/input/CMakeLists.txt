add_library(picoInput button.cpp button.h)

pico_generate_pio_header(picoInput ${CMAKE_CURRENT_LIST_DIR}/button.pio)

target_link_libraries(picoInput PRIVATE
        pico_stdlib
        hardware_pio
        )
