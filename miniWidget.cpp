#include <iostream>
#include "ArduiPi_OLED_lib.h"
#include "ArduiPi_OLED.h"
#include "miniWidget.h"

void bargraph :: setValue(int value){
    display.drawRect(x, y, width,height, WHITE);
    display.display();
}

bargraph :: bargraph(int x, int y, int w, int h){
    this->x = x;
    this->y = y;
    width = w;
    height = h;
}
