#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char * argv[]) {
    
        char * line = "xc     1e2 commoner population" ;
        char * espace = strchr(line,' ');
        double val ;
        if (*(espace+1) != ' '){ 
            val = atof(espace+1);
        }    
        else {
            val=atof(espace+2);
        }
    
    printf("Valeur:%0.3f\n", atof(espace));


        

    return 0;    
} 