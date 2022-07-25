//
// Created by ritwi on 7/25/2022.
//

#include "button.h"
#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "button.pio.h"

PIO pio = pio0;
uint offset = pio_add_program(pio, &buttonio_program);
uint sm = pio_claim_unused_sm(pio, true);
uint32_t lastInput = 0;

uint32_t btn(){
    return lastInput; //TODO fix this, for now 0
}

uint32_t btn(int k){
    return lastInput & (1 << (k - 1));
}

void button_end_frame(){
    //bitwise or all the input from the pio
    lastInput = 0;
    while(!pio_sm_is_rx_fifo_empty(pio,sm)){
        lastInput = lastInput | pio_sm_get(pio,sm);
    }
}

void button_init(){
    pio = pio0;
    offset = pio_add_program(pio, &buttonio_program);
    sm = pio_claim_unused_sm(pio, true);
    buttonio_program_init(pio, sm, offset, 16,2000);
}
