#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char * argv[]) {
    
    FILE * file = fopen("params_stable_equitable_2.txt", "r"); // pointer
    if (file == NULL) return -1;  //si fichier n'existe pas

    // Lire ligne par ligne
    int n = 0;
    char buffer[100];
    while (fgets(buffer, 100, file) != NULL) { //read and store char (max 100 char) into buffer. at the end-> NULL
        char * espace = strchr(buffer, ' ');
        if ((*(espace+1)) != ' ') {
            double val = atof(espace+1) ;
            printf("%f\n", val) ;
        }
        else {
            double val = atof(espace+2) ;
            printf("%f\n", val) ;
        }

        
    }

    return 0;    
} 