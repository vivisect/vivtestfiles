#include <windows.h>
#include <stdio.h>

// cl hellodll.c /link /DLL /out:pe/hellodll_i386.dll

__declspec(dllexport)
int foo(char *buf, int size) {
    int i = 0;
    for ( i = 0; i < size; i++ ) {
        buf[i] = 0;
    }
    return size;
}

__declspec(dllexport)
int bar() {
    printf("woot!\n");
    return(0);
}
