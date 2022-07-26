//
// Created by ritwi on 7/25/2022.
//

#include <pico/printf.h>
#include "button.h"
#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "button.pio.h"

PIO pio = pio0;
uint offset;
uint sm;
uint32_t lastInput;

uint32_t btn(){
    return lastInput;
}

bool btn_k(int k){
    return 0 < (lastInput & (1 << k));
}

void button_end_frame(){
    //bitwise or all the input from the pio
    lastInput = 0;
    while(!pio_sm_is_rx_fifo_empty(pio,sm)){
        lastInput = lastInput | pio_sm_get(pio,sm);
    }
}

void button_init(){
    const uint POWER_PIN = 22;
    gpio_init(POWER_PIN);
    gpio_set_dir(POWER_PIN, GPIO_OUT);
    gpio_put(POWER_PIN, 1);
    pio = pio0;
    offset = pio_add_program(pio, &buttonio_program);
    sm = pio_claim_unused_sm(pio, true);
    buttonio_program_init(pio, sm, offset, 16,2000);
}
