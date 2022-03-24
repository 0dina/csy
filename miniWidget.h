#ifndef _BarGraph_H_
#define _BarGraph_H_

#include <iostream>
#include "ArduiPi_OLED_lib.h"
#include "ArduiPi_OLED.h"

//class bargraph: public ArduiPi_OLED{
class bargraph{
private:
    int x;
    int y;
    int color;
    int width;
    int height;
    int dataValue;

public:
    ArduiPi_OLED display;

public:
    bargraph(int x, int y, int w, int h);
    void setValue(int value);
    void clear(void);

};

#endif
