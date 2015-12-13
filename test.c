/* Test source code file for pybugger */

#include <stdio.h>

int main()
{
    long tmp = 0;
    long sum = 0;
    int i;

    // comment #1
    while (tmp < 10) {
        tmp++;
    }
    sum += ((tmp+3) * (tmp/3)) / 2;

    // comment #2
    tmp = 0;
    if (tmp < 20) {
        tmp++;
    }

    // comment #3
    switch(tmp) {
        case 0:
            break;
        case 1:
            break;
        default:
            tmp *= 100;
            break;
    }

    for (i=0; i<tmp; i++) {
        // do stuff
        // compute things
    }

    return 0;
}
