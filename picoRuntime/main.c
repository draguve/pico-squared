﻿//#include "EPD_Test.h"   //Examples
#include "DEV_Config.h"
#include "GUI_Paint.h"
#include "ImageData.h"
#include "Debug.h"
#include <stdlib.h>
#include "LCD_1in8.h"
#include "button.h"


bool reserved_addr(uint8_t addr) {
    return (addr & 0x78) == 0 || (addr & 0x78) == 0x78;
}


int main(void)
{
    DEV_Delay_ms(100);
    printf("LCD_1in8_test Demo\r\n");
    if(DEV_Module_Init()!=0){
        return -1;
    }

    /* LCD Init */
    printf("1.8inch LCD demo...\r\n");
    LCD_1IN8_Init(HORIZONTAL);
    LCD_1IN8_Clear(WHITE);

    //LCD_SetBacklight(1023);
    UDOUBLE Imagesize = LCD_1IN8_HEIGHT*LCD_1IN8_WIDTH*2;
    UWORD *BlackImage;
    if((BlackImage = (UWORD *)malloc(Imagesize)) == NULL) {
        printf("Failed to apply for black memory...\r\n");
        exit(0);
    }
    // /*1.Create a new image cache named IMAGE_RGB and fill it with white*/
    Paint_NewImage((UBYTE *)BlackImage,LCD_1IN8.WIDTH,LCD_1IN8.HEIGHT, 0, WHITE);
    Paint_SetScale(65);
    Paint_Clear(WHITE);
    Paint_SetRotate(ROTATE_0);
    Paint_Clear(WHITE);

    // /* GUI */
    printf("drawing...\r\n");
    // /*2.Drawing on the image*/

    Paint_DrawPoint(2,1, BLACK, DOT_PIXEL_1X1,  DOT_FILL_RIGHTUP);//240 240
    Paint_DrawPoint(2,6, BLACK, DOT_PIXEL_2X2,  DOT_FILL_RIGHTUP);
    Paint_DrawPoint(2,11, BLACK, DOT_PIXEL_3X3, DOT_FILL_RIGHTUP);
    Paint_DrawPoint(2,16, BLACK, DOT_PIXEL_4X4, DOT_FILL_RIGHTUP);
    Paint_DrawPoint(2,21, BLACK, DOT_PIXEL_5X5, DOT_FILL_RIGHTUP);

    Paint_DrawLine( 10,  5, 40, 35, MAGENTA, DOT_PIXEL_2X2, LINE_STYLE_SOLID);
    Paint_DrawLine( 10, 35, 40,  5, MAGENTA, DOT_PIXEL_2X2, LINE_STYLE_SOLID);

    Paint_DrawLine( 80,  20, 110, 20, CYAN, DOT_PIXEL_1X1, LINE_STYLE_DOTTED);
    Paint_DrawLine( 95,   5,  95, 35, CYAN, DOT_PIXEL_1X1, LINE_STYLE_DOTTED);

    Paint_DrawRectangle(10, 5, 40, 35, RED, DOT_PIXEL_2X2,DRAW_FILL_EMPTY);
    Paint_DrawRectangle(45, 5, 75, 35, BLUE, DOT_PIXEL_2X2,DRAW_FILL_FULL);

    Paint_DrawCircle(95, 20, 15, GREEN, DOT_PIXEL_1X1, DRAW_FILL_EMPTY);
    Paint_DrawCircle(130, 20, 15, GREEN, DOT_PIXEL_1X1, DRAW_FILL_FULL);


    Paint_DrawString_CN(1,40, "»¶Ó­Ê¹ÓÃ",  &Font24CN, BLUE, WHITE);
    Paint_DrawString_EN(1, 83, "Pico-LCD-1.8", &Font12, WHITE, BLUE);
    Paint_DrawString_EN (1,96 ,"160x128 Pixel", &Font12, WHITE,  BLACK);
    Paint_DrawString_EN(1, 110, "ST7735S Controller", &Font12, RED, WHITE);

    // /*3.Refresh the picture in RAM to LCD*/
    LCD_1IN8_Display(BlackImage);
    DEV_Delay_ms(2000);


    /* Module Exit */
    free(BlackImage);
    BlackImage = NULL;


    DEV_Module_Exit();
    return 0;
}
